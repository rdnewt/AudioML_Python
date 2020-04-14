# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:04:54 2020

@author: sjhar
"""

import os
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt



#********Edit path variables below before use to match local environment

# location of audio files
directory = r"C:\Users\sjhar\OneDrive\Documents\Classes\ASU\2020 Spring\EEE 489 Senior Design II\Code\Audio Samples"
# where the spectrograms will be stored
output_path = r"C:\Users\sjhar\OneDrive\Documents\Classes\ASU\2020 Spring\EEE 489 Senior Design II\Code\Spectrograms_revB"

fnames = os.listdir(directory)

pts_fft = 1024
spectro = np.zeros((256,216))

for name in fnames:    
    fs,dat = wav.read(directory+"\\"+name)           #read in .wav file
    
        
    # this section performs a check to see if the .wav file is stereo (2-channels) 
    # and averages the 2 to a single channel if that is the case
    # can be commented out if all the files are now mono format
    if len(np.shape(dat))==2:
        print("")
        dat = dat.astype(float)
        dat = (dat[:,0]+dat[:,1])//2
        dat = dat.astype('int16')
    
    #set sample to correct length by padding zeros
    dat = np.pad(dat, (0,pts_fft-len(dat)%pts_fft))
    
    #generate window
    window = np.hamming(pts_fft)
    
    
    # compute spectrograms and load into spectro field
    for i in range(len(dat)//pts_fft):
        a = np.fft.fft(dat[i:i+pts_fft]*window)
        b = abs(a[0:pts_fft//4])
        b = 20*np.log10(b)
        spectro[:,i] = b
    
    f = np.arange(0,fs/4,fs/pts_fft)
    t = np.arange(0,(fs*5//pts_fft+1)*pts_fft/(fs),pts_fft/fs)
    
    
    '''plt.pcolormesh(t, f, spectro)
    plt.ylabel('Freq (Hz)')
    plt.xlabel('Time (s)')
    plt.show()'''
    
    #for saving files
    outname = output_path+"\\"+name[0:-4]+"_spectro"        # specify output file full name (path + filename)
    np.save(outname,spectro)          # save array
