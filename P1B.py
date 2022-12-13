from tkinter import *
from playsound import playsound
from scipy.io.wavfile import write
import math
import random
import wave
import sys
from pyaudio import PyAudio

#                           Generating our own audio sounds
BITRATE = 16000 #number of frames per second/frameset.
#FREQUENCY = 2000 #Hz, Waves Per Second
FREQUENCY = 4600 #Hz, Waves Per Second
LENGTH = 1.2232 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

for x in range(NUMBEROFFRAMES):
   WAVEDATA += chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128)) 
   FREQUENCY += 1/16

#fill remainder of frameset with silence
for x in range(RESTFRAMES): 
    WAVEDATA += chr(128)

p = PyAudio()
stream = p.open(
    format=p.get_format_from_width(1),
    channels=1,
    rate=BITRATE,
    output=True,
    )

#                       playing their audiofile
def original_sound():
    playsound('/Users/christopherbarnes/cmsc20300/P1B/Pilot/alarm.wav')
    print('the original sound')

def generated_sound():
    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('playing the PyAudio generated sound')

def main():
    rand = random.randint(1,2)
    '''
    if rand == 1:
        play_sound()
        print("1")
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
        p.terminate()
    else:
        print("2")
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
        p.terminate()
        play_sound()
        '''
    
    
    #original_sound()
    generated_sound()



main()