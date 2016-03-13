import os
import sys
import glob

import re



SPEAKER = "TRUMP:"

def main():
    files = glob.glob("data/debates/[rR]*")
    print len(files)
    output = open("data/"+ SPEAKER[:-1] + ".txt","w")
    speaker_regex = re.compile("[A-Z]+:")
    for f in files:
        with open(f, "r") as fp:
            isSpeaker = False
            for line in fp:
                matches = speaker_regex.match(line)
                if matches is not None:
                    if matches.group() == SPEAKER:
                        isSpeaker = True
                    else:
                        isSpeaker = False
                if isSpeaker:
                    output.write(line)
    output.close()

if __name__=="__main__":
    main()
