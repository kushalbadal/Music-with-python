import simpleaudio as sa
import time


#play function
def mplay(fname):
    wave_obj = sa.WaveObject.from_wave_file(fname)
    play_obj = wave_obj.play()
    time.sleep(0.3)
    return 0
notes5 = {'C5':"C5.wav" , 'C5#':"C5#.wav", 'D5':"D5.wav", 'D5#':"D5#.wav", 'E5':"E5.wav", 'F5':"F5.wav", 'F5#':"F5#.wav", 'G5':"G5.wav", 'G5#':"G5#.wav", 'A5':"A5.wav", 'A5#':"A5#.wav", 'B5':"B5.wav"}
notes4 = {'C4':"C4.wav" , 'C4#':"C4#.wav", 'D4':"D4.wav", 'D4#':"D4#.wav", 'E4':"E4.wav", 'F4':"F4.wav", 'F4#':"F4#.wav", 'G4':"G4.wav", 'G4#':"G4#.wav", 'A4':"A4.wav", 'A4#':"A4#.wav", 'B4':"B4.wav"}

notes2freq={**notes4, **notes5}
print(notes2freq)
tones = input("Enter the notes: \n")
data= ''
for i in range(len(tones)) :
    if (tones[i]!=' '):
        if(tones[i-1]==' '):
            mplay(notes2freq[data])
            data=''
        elif (i+1==len(tones)):
            data = data + tones[i]
            mplay(notes2freq[data])
            data=''
        data=data+tones[i]


