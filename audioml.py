#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:34:35 2020

@author: solasholola
"""

import pyaudio
import wave

FORMAT = pyaudio.paInt16  # Records in 16bits

CHANNELS = 1  # Mono channel

RATE = 44100 # Sample Rate

CHUNK = 1024  #byte size

RECORD_SECONDS = 5

WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format = FORMAT, 
                    channels = CHANNELS,
                    rate = RATE, 
                    input = True,
                    frames_per_buffer = CHUNK,
                    # USB 
                    input_device_index = 0)
                    
print ("recording...")
frames = []
for i in range(0, int((RATE / CHUNK) * RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow = False)
    frames.append(data)
    print ("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

# creates wave file with audio read in
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()