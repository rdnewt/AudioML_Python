# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:13:49 2020

@author: sjhar
"""

import numpy as np
import scipy.io.wavfile as wav
### our custom module with all of our function
import audioml as aml


pts_fft = 1024
window = np.hamming(pts_fft)

def dataload (filename):
    fs,dat = wav.read(filename)           #read in .wav file
#*    #print(filename, fs)
    # this section performs a check to see if the .wav file is stereo (2-channels) 
    # and averages the 2 to a single channel if that is the case
    # can be commented out if all the files are now mono format
    if len(np.shape(dat))==2:
        dat = dat.astype(float)
        dat = (dat[:,0]+dat[:,1])//2
        dat = dat.astype('int16')
    return dat, fs

def spec_gen(dat, fs):
    dat = np.pad(dat, (0,pts_fft-len(dat)%pts_fft))
    dat_l = len(dat)
    if fs != 44100:
            print ("Error:\n    Loc: audioml.py, class: sample, function: spec_gen\n    Desc: sampling frequency does not equal 44.1kHz\n        Support for other frequencies will be added in version 2.0.")
            return False
    else:
        spec_l = len(dat)//pts_fft
        spec = np.zeros((pts_fft//4,spec_l))
        for i in range(spec_l):
            a = np.fft.fft(dat[i:i+pts_fft]*window)
            b = abs(a[0:pts_fft//4]+1E-15)  #added 1E-10 to values because np.log10(b) was producing a divide by zero warning, 1E-10 far too small to affect output
            b = 20*np.log10(b)
            spec[:,i] = b
            del a, b
        
        f = np.arange(0,fs/4,fs/pts_fft)
        t = np.arange(0,dat_l/fs,pts_fft/fs)
        
        return spec, f, t
