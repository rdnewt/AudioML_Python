# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:13:49 2020

@author: sjhar
"""

import numpy as np
from scipy.io import wavfile

### our custom module with all of our function
#import amltools as aml


class sample:
    def __init__(self, data, fs = 44100, start = 0):
        ### all of these will need to be modified to instantiate the class fields in 'shared' gpu/cpu memory
        ### this means the instantiation of the class will serve as the vehicle moving data into gpu-accessible resources
        ### this can be accomplished with pyCUDA directives
        ### requires edits
        self.fs = fs
        self.data = np.copy(data)
        self.start = start
        self.end = start + 5
        #self.hist = audioml.hist_gen(self.fs,self.data)      # xdim, ydim = number of ffts, number of points per fft
        #self.soundtype = audioml.classify(self.hist)
    def update(self, data, fs):
    	temp_spect = audioml.hist_gen(fs, data)
    	len = temp_spect.shape[1]
    	self.hist = np.concatenate((self.hist.copy()[len:],temp_spect))
    	self.soundtype = audioml.classify(self.hist)


fname = 'Audio Samples/9031-3-2-0.wav'
fs, data = wavfile.read(fname)
import os

for filename in os.listdir('Audio Samples'):
    if filename.endswith(".wav"):
        print(os.path.join('Audio Samples', filename))
        fs, data = wavfile.read(os.path.join('Audio Samples', filename))
        print(data.shape,type(data))
        continue
    
    else:
        continue
