import wave, struct

wavefile = wave.open('notes/piano-C4.wav', 'rb')

length = wavefile.getnframes()
for i in range(0, length):
    waveData = wavefile.readframes(1)
    data = struct.unpack("<h", waveData)
    print(int(data[0]))