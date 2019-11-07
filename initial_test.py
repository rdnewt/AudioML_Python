# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:50:06 2019

@author: rrhoa
"""

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

import librosa
import librosa.display
import numpy as np
import os
import re
#from path import Path


filename = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC-50\audio\1-137-A-32.wav"
name = "1-137-A-32"

directory = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC-50\audio"

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
    filename  = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC_capstone\test_files\\" + name + ".png"
    fig.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()    
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S

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
    filename  = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC_capstone\test_files\\" + name + ".png"
    fig.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()    
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S

    
filenames = os.listdir(directory)
test_names = []
for fname in filenames: 
    x = re.match("1-.*",fname)
    if x:
        name = fname.split('.')[0]
        test_names.append(name)

#name = test_names[0]
#create_spectrogram_test(directory+"\\"+name+".wav",name)

for name in test_names:
    create_spectrogram_test(directory+"\\"+name+".wav",name)