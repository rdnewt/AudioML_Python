# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:50:06 2019

@author: rrhoa
"""


import numpy as np
import pandas as pd


directory = r"C:\Users\rrhoa\Documents\UrbanSound8k\audio"
directory2 = r"C:\Users\rrhoa\Documents\Classes\EEE488\AudioML_Python"
directory3 = r"C:\Users\rrhoa\Documents\UrbanSound8k\metadata"


#list all files in audio directory
cross_fold = 1

from GeneralDataGenerator import DataGenerator

def append_ext(fn):
    name = fn.split(".")[0]
    return name+"_spectro.npy"


datadf=pd.read_csv(directory3+"\\UrbanSound8K.csv")
datadf["slice_file_name"]=datadf["slice_file_name"].apply(append_ext)

traindf = datadf[datadf["fold"] != cross_fold]
testdf = datadf[datadf["fold"] == cross_fold]
testClasses = testdf["class"]
traindf = traindf.drop(columns=['fsID','start','end','salience','fold','class'])
testdf = testdf.drop(columns=['fsID','start','end','salience','fold','class'])
trainIDs = traindf["slice_file_name"].tolist()
testIDs = testdf["slice_file_name"].tolist()
trainLabels = traindf.set_index("slice_file_name").to_dict()["classID"]
testLabels = testdf.set_index("slice_file_name").to_dict()["classID"]

dim=(430,512)

train_generator=DataGenerator(
        list_IDs = trainIDs, 
        labels = trainLabels, 
        data_path = 'train_files\\',
        dim=dim,
        batch_size=16,
        n_channels=1,
        n_classes=10, 
        shuffle=False)



from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras import regularizers, optimizers


model = Sequential()
model.add(Conv2D(16, (3, 3), padding='same',
                 input_shape=(dim[0],dim[1],1)))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
model.compile(optimizers.rmsprop(lr=0.0005, decay=1e-6),loss="categorical_crossentropy",metrics=["accuracy"])
model.summary()


#Fitting keras model, no test gen for now
#STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size

model.fit_generator(generator=train_generator,
                    steps_per_epoch=None,
                    epochs=150
)


test_generator=DataGenerator(
        list_IDs = testIDs, 
        labels = testLabels, 
        data_path = 'test_files\\',
        dim=(430,512),
        n_channels=1,
        n_classes=10, 
        shuffle=False)

#STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
model.save("./model/model_v1.h5")

pred=model.predict_generator(test_generator,
                             steps=None,
                             verbose=1)
predicted_class_indices=np.argmax(pred,axis=1)

#Fetch labels from train gen for testing
labels = (train_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]

print(predictions[0:6])

comparison = [predictions[i] == testClasses[i] for i in predicted_class_indices]
accuracy = sum(comparison)/len(comparison)
print(accuracy)

