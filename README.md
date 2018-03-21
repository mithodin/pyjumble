# pyjumble
Jumble an audiofile reversibly

    Usage: jumble.py <audiofile> [<start_shuffle>, <end_shuffle>, <shuffle_seq>]
             creates a shuffled file in flac format from the given audio file.
             Optional parameters:
                 start_shuffle: Begin shuffling after <start_shuffle> seconds (default: 0)
                 end_shuffle: End shuffling at <end_shuffle> seconds (default: 120)
                 shuffle_seq: Shuffle packets of <shuffle_seq> frames (default: 500). 1 frame equals 1 ms.
             The output file will be named shuffled.flac. Also, a file named unjumble.conf will be created.
             That file is needed to reverse the shuffle.
       
           unjumble.py <audiofile> <secret>
             recovers a shuffled audio file. Pass the files created by jumble.py to reverse the shuffling.
