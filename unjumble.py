#!/usr/bin/env python3
from pydub import AudioSegment
import random 
import easysettings as ez
import sys

samplerate = 1000
try:
    filename = sys.argv[1]
    secret = sys.argv[2]
except:
    print("Verwendung: unjumble.py <Audiodatei> <Geheimnis>")
    sys.exit(-1)

try:
    config = ez.EasySettings(secret)
    start_shuffle = config["start_shuffle"]
    end_shuffle = config["end_shuffle"]
    shuffle_seq = config["shuffle_seq"]
    indices = config["indices"]
except:
    print("Geheimdatei nicht lesbar.")
    sys.exit(-2)

try:
    source = AudioSegment.from_file(filename)
except:
    print("Audiodatei nicht lesbar.")
    sys.exit(-3)

start = source[:start_shuffle*samplerate]
end = source[end_shuffle*samplerate:]

unshuffled = [()]*len(indices)
for i in range(int((end_shuffle-start_shuffle)*samplerate/shuffle_seq)):
    unshuffled[indices[i]]=source[start_shuffle*samplerate+shuffle_seq*i:start_shuffle*samplerate+shuffle_seq*(i+1)]

shuffled = start
for s in unshuffled:
    shuffled = shuffled.append(s,crossfade=0)
shuffled = shuffled.append(end,crossfade=0)

shuffled.export("unshuffled.flac",format="flac")
