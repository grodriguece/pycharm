# import math as m
# # Sample rate(samples per second)
# sr = 8000
# # Frequency(Hertz)
# h = 261.625565
# # ByteBeat
# b = sr/256  # 8bit sound
# # Volume
# v = 127
# t = 0   # time
# while 1:
#     print(int((m.sin(t*2*3.14/(sr*h))+1)*v).to_bytes(2, byteorder="little"))
#     #p rint(int(((t<<1)^((t<<1)+(t>>7)&t>>12))|t>>(4-(1^7&(t>>19)))|t>>7).to_bytes(8,byteorder="big"))
#     t += 1

import numpy as np
from scipy.io.wavfile import write

# Samples per second
sps = 44100

# Frequency / pitch of the sine wave
freq_hz = 440.0

# Duration
duration_s = 5.0

# NumpPy magic
each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)

# Write the .wav file
write('first_sine_wave.wav', sps, waveform_integers)