# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:50:06 2019

@author: rrhoa
"""

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

new_path = r"C:\Users\rrhoa\Documents\Classes\EEE488\ESC-50\audio\1-137-A-32.wav"

sample_rate, samples = wavfile.read(new_path)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()