# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:50:06 2019

@author: rrhoa
"""

import matplotlib.pyplot as plt
from matplotlib import figure

import librosa
import librosa.display
import numpy as np
import os
import re
import pandas as pd


from keras import layers
from keras import models
from keras.layers.advanced_activations import LeakyReLU
from keras.optimizers import Adam
import keras.backend as K

import pylab
import gc

#filename = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC-50\audio\1-137-A-32.wav"
#name = "1-137-A-32"

directory = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC-50\audio"
directory2 = r"C:\Users\rrhoa\Documents\Classes\EEE488\AudioML_Python"

#Function to create spectrogram and place in the test folder
def create_spectrogram_test(filename,name):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72,0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename  = r"C:\Users\rrhoa\Documents\Classes\EEE488\AudioML_Python\test_files\\" + name + ".png"
    fig.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()    
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S

#Function to create spectrogram and place in the train folder
def create_spectrogram_train(filename,name):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72,0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename  = r"C:\Users\rrhoa\Documents\Classes\EEE488\AudioML_Python\train_files\\" + name + ".png"
    fig.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()    
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S

#list all files in audio directory
filenames = os.listdir(directory)

#split file names into test and train based on folds
test_names = []
train_names= []
for fname in filenames: 
    x = re.match("1-.*",fname)
    if x:
        name = fname.split('.')[0]
        test_names.append(name)
    else:
        name = fname.split('.')[0]
        train_names.append(name)

#Creates the spectrograms for training and testing
#only run this part once, otherwise just wastes time
#for name in test_names:
#    create_spectrogram_test(directory+"\\"+name+".wav",name)
    
#for name in train_names:
#    create_spectrogram_train(directory+"\\"+name+".wav",name)


from keras_preprocessing.image import ImageDataGenerator

#Updates file name column to match the spectrogram instead of the audio file
def append_ext(fn):
    name = fn.split(".")[0]
    return name+".png"

#Reads in the ESC-50 metadata
datadf=pd.read_csv('../ESC-50/meta/esc50.csv')
datadf["filename"]=datadf["filename"].apply(append_ext)

traindf = datadf[datadf["fold"] != 1]
testdf = datadf[datadf["fold"] == 1]
print(traindf.head())
print(testdf.head())


datagen=ImageDataGenerator(rescale=1./255.,validation_split=0.25)


train_generator=datagen.flow_from_dataframe(
    dataframe=traindf,
    directory=directory2+"\\train_files",
    x_col="filename",
    y_col="major_category",
    subset="training",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="categorical",
    target_size=(64,64))

valid_generator=datagen.flow_from_dataframe(
    dataframe=traindf,
    directory=directory2+"\\train_files",
    x_col="filename",
    y_col="major_category",
    subset="validation",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="categorical",
    target_size=(64,64))



from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras import regularizers, optimizers
import pandas as pd
import numpy as np

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=(64,64,3)))
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
model.add(Dense(5, activation='softmax'))
model.compile(optimizers.rmsprop(lr=0.0005, decay=1e-6),loss="categorical_crossentropy",metrics=["accuracy"])
model.summary()


#Fitting keras model, no test gen for now
STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
STEP_SIZE_VALID=valid_generator.n//valid_generator.batch_size
#STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
model.fit_generator(generator=train_generator,
                    steps_per_epoch=STEP_SIZE_TRAIN,
                    validation_data=valid_generator,
                    validation_steps=STEP_SIZE_VALID,
                    epochs=150
)
model.evaluate_generator(generator=valid_generator, steps=STEP_SIZE_VALID
)


#Create test dataset to evaluate model
test_datagen=ImageDataGenerator(rescale=1./255.)
test_generator=test_datagen.flow_from_dataframe(
    dataframe=testdf,
    directory=directory2+"\\test_files",
    x_col="filename",
    y_col=None,
    batch_size=32,
    seed=42,
    shuffle=False,
    class_mode=None,
    target_size=(64,64))
STEP_SIZE_TEST=test_generator.n//test_generator.batch_size

#Predict the model for the testing data
test_generator.reset()
pred=model.predict_generator(test_generator,
                             steps=STEP_SIZE_TEST,
                             verbose=1)
predicted_class_indices=np.argmax(pred,axis=1)

#Fetch labels from train gen for testing
labels = (train_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]

testlabels = testdf["major_category"].tolist()
comparison = [predictions[i] == testlabels[i] for i in predicted_class_indices]
accuracy = sum(comparison)/len(comparison)
print(accuracy) #Prints final accuracy of the model based on test data
#Resulted in 49% for fold 1 and 51% for fold 2, at which point I stopped