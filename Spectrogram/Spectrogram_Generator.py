# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:15:10 2020

@author: sjhar
"""

### Spectrogram Module- this will get consolidated into one (or a couple) of functions which will be added to the audioml module
### Output spectrogram dimesnions:
###     430 points along time-axis (x-axis)
###     512 points along frequency-axis (y-axis)

import os
import numpy as np
import scipy.io.wavfile as spwav
import scipy.signal as spsig
import matplotlib.pyplot as plt


## This section is to be modified to grab all the sound clip names in your local file directory
## Rachel, I know you already have a segment of code that does this in your python file uploaded to github
## just need to get all the full path+file strings into the list 'fnames'
directory = r"C:\Users\sjhar\OneDrive\Documents\Classes\ASU\2020 Spring\EEE 489 Senior Design II\Code\Audio Samples"
fnames = os.listdir(directory)
#fnames[:] = [directory+"\\"+name for name in fnames]

# where the spectrograms will be stored
output_path = r"C:\Users\sjhar\OneDrive\Documents\Classes\ASU\2020 Spring\EEE 489 Senior Design II\Code\Spectrograms"


## I played around with these parameters to find a figure size around 400-500 points square, these seemed to work
## Selected 4096 point fft to maintain resolution while "cutting out" the highest half of frequencies in the fft
## Spectrograms were pretty much empty above ~5kHz, so I decided to chop out that data below and maintain 512 points in frequency
pts_fft = 4096  # pts in each fft of the spectrogram, scipy only returns half of these, and then I half that again due to ^^^
step = 512      # chosen to maintain ~400 points on the time axis, was arbitrary but I decided to keep roughly the same number of pts along both axes
pts_overlap = pts_fft-step
spectro_pts_5s = (44100*5)//(step)      # calculates the number of x-axis points in the spectrogram

# the scipy spectrogram chooses to 'cut off' any data points that fall beyond the last complete fft
# this basically calculates the length of array needed so that no data is cut off for a 5 second clip
dat_pts_5s = spectro_pts_5s*step+pts_fft-1



for name in fnames:
    fs,dat = spwav.read(directory+"\\"+name)           #read in .wav file
    
    # this section performs a check to see if the .wav file is stereo (2-channels) 
    # and averages the 2 to a single channel if that is the case
    # can be commented out if all the files are now mono format
    if len(np.shape(dat))==2:
        dat = dat.astype(float)
        dat = (dat[:,0]+dat[:,1])//2
        dat = dat.astype('int16')
    
    # this 'if-else' sets all arrays to the correct length to return a 5-second length spectrogram
    if len(dat) > dat_pts_5s:
        dat = dat[0:dat_pts_5s]
    else:
        dat = np.concatenate((dat,np.zeros(dat_pts_5s-len(dat),'int16')))
    
    # generates spectrogram
    f, t, Sxx = spsig.spectrogram(dat, fs, window='hamming', nperseg=pts_fft, noverlap=pts_overlap)
    
    # clips frequency labels and output spectrogram to half-length
    # fft will calculate for frequencies 0Hz-22050Hz, this clips that to 0Hz-~5500Hz
    # again, very little data was present above ~5kHz, I think this will improve our resolution and remove empty data points
    f = f[0:pts_fft//8]
    Sxx = Sxx[0:pts_fft//8,:]
    #print(np.shape(Sxx))
    
    '''# plot output in standard colormesh chart, should be commented out when running for large batch of data
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Freq (Hz)')
    plt.xlabel('Time (s)')
    plt.show()
    '''
    
    #print(np.shape(Sxx))                   # shows shape of array holding spectro data
    # load spectrogram elements into a single numpy array and transpose Sxx
    # transpose Sxx to allow easier concatenation of new data chunks in main program, CNN needs to be trained with the correctly formatted data
    spectro = np.array((f,t,np.transpose(Sxx)))
    outname = output_path+"\\"+name[0:-4]+"_spectro"        # specify output file full name (path + filename)
    #np.save(outname,spectro)          # save array
    



    
    