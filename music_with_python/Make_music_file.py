from pydub import AudioSegment
from pydub.playback import play
import wave
import struct


notes5 = {'C5':"C5.wav" , 'C5#':"C5#.wav", 'D5':"D5.wav", 'D5#':"D5#.wav", 'E5':"E5.wav", 'F5':"F5.wav", 'F5#':"F5#.wav", 'G5':"G5.wav", 'G5#':"G5#.wav", 'A5':"A5.wav", 'A5#':"A5#.wav", 'B5':"B5.wav"}
notes4 = {'C4':"C4.wav" , 'C4#':"C4#.wav", 'D4':"D4.wav", 'D4#':"D4#.wav", 'E4':"E4.wav", 'F4':"F4.wav", 'F4#':"F4#.wav", 'G4':"G4.wav", 'G4#':"G4#.wav", 'A4':"A4.wav", 'A4#':"A4#.wav", 'B4':"B4.wav"}

notes2freq={**notes4, **notes5}
print(notes2freq)
tones = input("Enter the notes: \n")
data= ''
output=AudioSegment.empty()
for i in range(len(tones)) :
    if (tones[i]!=' '):
        if(tones[i-1]==' '):
            output=output+AudioSegment.from_file(notes2freq[data])
            data=''
        elif (i+1==len(tones)):
            data = data + tones[i]
            output = output + AudioSegment.from_file(notes2freq[data])
            data=''
        data=data+tones[i]
    else:
        output=output+AudioSegment.empty()
output.export("output.wav", format="wav")

input_file = wave.open(r"output.wav", 'rb')
output_file = wave.open(r"outputmusic.wav", 'wb')
in_params = list(input_file.getparams())
out_params = in_params[:]
out_params[0] = 2
output_file.setparams(out_params)

nchannels, sampwidth, framerate, nframes, comptype, compname = in_params
format = '<{}h'.format(nchannels)

for index in range(nframes):
    frame = input_file.readframes(1)
    data = struct.unpack(format, frame)
    value = data[0]
    value = (value * 2) // 3
    output_file.writeframes(struct.pack('<h', value))

input_file.close()
output_file.close()