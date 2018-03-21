#!/usr/bin/env python3
from pydub import AudioSegment
import random 
import numpy as np
import easysettings as ez
import sys

samplerate = 1000
start_shuffle = 10 
end_shuffle = 120
shuffle_seq = 500

try:
    filename = sys.argv[1]
except:
    print("Verwendung: jumble.py <Audiodatei> [<start_shuffle>, <end_shuffle>, <shuffle_seq>]")
    sys.exit(-1)

try:
    start_shuffle = int(sys.argv[2])
    end_shuffle = int(sys.argv[3])
    shuffle_seq = int(sys.argv[4])
except:
    pass

config = ez.EasySettings("unjumble.conf")
config.set("start_shuffle",start_shuffle)
config.set("end_shuffle",end_shuffle)
config.set("shuffle_seq",shuffle_seq)

file = AudioSegment.from_mp3(filename)

start = file[:start_shuffle*samplerate]
end = file[end_shuffle*samplerate:]

middle = []
for i in range(int((end_shuffle-start_shuffle)*samplerate/shuffle_seq)):
    middle.append((i,file[start_shuffle*samplerate+shuffle_seq*i:start_shuffle*samplerate+shuffle_seq*(i+1)]))
random.shuffle(middle)

shuffled = start
for (_,s) in middle:
    shuffled = shuffled.append(s,crossfade=0)
shuffled = shuffled.append(end,crossfade=0)

indices = [i for (i,_) in middle]
config.set("indices",indices)
shuffled.export("shuffled.flac",format="flac")
config.save()
