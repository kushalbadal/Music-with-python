import numpy as np
import pyaudio
import math

BITRATE = 44100
WAVEDATA = ''
def note(frequency, length, sample_rate=44100):
    global WAVEDATA
    NUMBEROFFRAMES = int(sample_rate * length)
    RESTFRAMES = NUMBEROFFRAMES % sample_rate
    # generating waves
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(int(math.sin(x / ((sample_rate / frequency) / math.pi)) * 127 + 128))

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)



base_freq = 523.251
l = .2 # basic duration unit
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notes2freq = {notes[i]: base_freq * 2 ** (i / 12.0) for i in range(len(notes))}
print(notes2freq)
tones = [('E', 3 * l), ('D', l), ('C#', 2 * l), ('B', 2 * l), ('A', 2 * l),
         ('B', 2 * l), ('C#', 2 * l), ('D', 2 * l), ('E', 3 * l),
         ('F#', l), ('E', 2 * l), ('D', 2 * l), ('C#', 4 * l)]

samples = []
for tone, duration in tones:
   note(notes2freq[tone], duration)

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(1), channels=2, rate=BITRATE, output=True)
stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
