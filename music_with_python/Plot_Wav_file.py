import pyaudio
import wave
import numpy as np
import sys
from array import array
from struct import pack
import matplotlib.pyplot as plt
chunk=1024
wav = wave.open("sou.wav","r")
s_rate= wav.getframerate()
n_frames= wav.getnframes()
raw=wav.readframes(-1)
print(raw)
raw = np.frombuffer(raw,"Int16")
raw.shape= -1,2
raw = raw.T
t_seq= np.arange(0,n_frames/float(s_rate), 1/float(s_rate))
plt.title("Waveform")
plt.plot(t_seq,raw[1],color="blue")
plt.ylabel("Amplitude")
plt.show()
wav.close()
wav = wave.open("sou.wav","rb")
p= pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wav.getsampwidth()),channels=2,rate=s_rate,output=True)
count=len(raw[0])
i=0
data=wav.readframes(chunk)
while len(data)>0:
    stream.write(data)
    print(data)
    data = wav.readframes(chunk)
stream.stop_stream()