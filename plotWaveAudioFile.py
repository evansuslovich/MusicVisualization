import struct
import wave

import matplotlib.pyplot as plt

wavefile = wave.open('./notes/music-loop.wav', 'r')

length = wavefile.getnframes()

# only mono files
if wavefile.getnchannels() == 2:
    print("stereo Files are not supported use mono files")

# gets all frequency levels and sets to raw
raw = []
for i in range(0, 1):
    waveData = wavefile.readframes(1)
    print(waveData)
    data = struct.unpack("<h", waveData)
    print(data)
    raw.append(data[0])


# Sample rate is the number of samples per second that are taken of
# a waveform to create a discrete digital signal
sampleRate = wavefile.getframerate()

# The time broken down
Time = []
for i in range(len(raw)):
    Time.append(i / sampleRate)

plt.title("Waveform of Wave File")
plt.plot(Time, raw, color="black")
plt.ylabel("Amplitude")
plt.show()

