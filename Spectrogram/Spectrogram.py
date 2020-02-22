from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
from scipy.io import wavfile
import matplotlib
import numpy as np
import math

import os

def stereo_check(data):
    channels = np.size(data,1)
    if channels == 1:
        return data
    else:
        return combine_channels(data)


def combine_channels(data):
    left_channel  = data[:,[0]]
    print(left_channel.flatten())
    right_channel = data[:,[1]]
    print(right_channel.flatten())
    new_data = left_channel.flatten() + right_channel.flatten()
    return new_data

def five_seconds(data, num_samples):
    if data.size > num_samples:
        new_data = data[range(num_samples)]
    elif data.size < num_samples:
        new_data = np.zeros(num_samples, dtype=int)
        new_data[:data.size] = data
    elif data.size == num_samples:
        new_data = data
    return new_data



directory = "/home/matthew/PycharmProjects/untitled/audio"
filename = "/Laugh.wav"
file = directory + filename


# print(file)
sample_rate, s = wavfile.read(file)
# print(s)
# Check first to see if there are multiple channels or else the spectrogram will mess up.
samples = stereo_check(s)
# print(samples)
# print(samples.size)
# Shorten or expand current data to encompass only 5 seconds
five_sample = sample_rate * 5
new_samples = five_seconds(samples,five_sample)
# print(new_samples.size)


# # fivee = sample_rate * 5 - 1
# # test = samples[range(five_sample)]
# # # print(test.size)
# # # print(test)
# # new_test = five_seconds(test, five_sample)
# print("here")
# print(new_test.size)
# print(new_test)



# print(samples)
# print(test)
# length = s.shape[0] / sample_rate
# print(f"length = {length}s")
# time = np.linspace(0., length, s.shape[0])
# plt.plot(time, s[:,0], label="Left Channel")
# plt.plot(time, s[:,1], label="Right Channel")
# plt.legend()
# plt.xlabel("Time")
# plt.ylabel("Amp")
# plt.savefig("Thisfile.png")

# print(sample_rate)
# print(samples)
# print(numpy.size(samples, 0))
# c = numpy.size(samples, 0) / sample_rate
# print(c)
# print(samples)

nperseg = 256
noverlap = 256 // 8
print("noverlap")
print(noverlap)

x_size = math.floor(five_sample / (nperseg - noverlap))
if nperseg*x_size-noverlap*(x_size-1) > five_sample:
    x_size -= 1

print(x_size)
freq, times, spectro = signal.spectrogram(new_samples, sample_rate, nperseg=nperseg, noverlap=noverlap)

# print(freq)
# print("break")
# print(times)
# print("break")
# print(spectro)
# print("break")
print(times.size)
print(freq.size)
print(spectro.shape)
plt.pcolormesh(times, freq, spectro)
plt.ylabel("freq")
plt.xlabel("time")
plt.savefig("help1.png")


# TODO: figure out how to do large files
directory = "/home/matthew/PycharmProjects/untitled/audio"
filename = "/Laugh.wav"
file = directory + filename
sample_rate, s = wavfile.read(file)
samples = stereo_check(s)
five_sample = sample_rate * 5
# Time to iter through until it's all been done
# overlap each spectro by how many seconds? 1,2,3,4
overlap = 1
sample_overlap = sample_rate * overlap
num_iters = math.ceil(samples.size/(five_sample-sample_overlap))

starting_sample = 0
next_sample = five_sample-sample_overlap
exit_for = False

for k in range(num_iters):
    if exit_for:
        break
    if samples.size < starting_sample+five_sample:
        new_samples = np.zeros(five_sample, dtype=int)
        new_samples[:(samples.size-starting_sample)] = samples[range(starting_sample,samples.size)]
        exit_for = True
    else:
        new_samples = samples[range(starting_sample,starting_sample+five_sample)]
        exit_for = False
    starting_sample += next_sample
    freq, times, spectro = signal.spectrogram(new_samples, sample_rate, nperseg=nperseg, noverlap=noverlap)
    plt.pcolormesh(times, freq, spectro)
    plt.ylabel("freq")
    plt.xlabel("time")
    plt.savefig("help{0}.png".format(k))








new_samples = five_seconds(samples,five_sample)

# TODO: ensure same filesize regardless of nperseg?

# TODO: figure out how to do livestream audio



