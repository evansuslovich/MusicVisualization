import wave
import matplotlib.pyplot as plt
import numpy as np

wavefile = wave.open('notes/piano-C4.wav', 'r')

raw = wavefile.readframes(-1)
raw = np.frombuffer(raw, np.int16)
sampleRate = wavefile.getframerate()

if wavefile.getnchannels() == 2:
    print("stereo Files are not supported use mono files")

Time = np.linspace(0, len(raw) / sampleRate, num=len(raw))
plt.title("Waveform of Wave File")
plt.plot(Time, raw, color="blue")
plt.ylabel("Amplitude")
plt.show()


# length = wavefile.getnframes()
# for i in range(0, length):
#     waveData = wavefile.readframes(1)
#     data = struct.unpack("<h", waveData)
#     print(int(data[0]))
