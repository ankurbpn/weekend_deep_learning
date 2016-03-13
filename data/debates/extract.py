import sys
import os


def main():
    # my code here
    if len(sys.argv) != 4:
        print "Usage: python extract.py infilename speakername outfilename"
    speaker = sys.argv[2]
    with open(sys.argv[3], 'w'):
        for line in open(sys.argv[1], 'r'):
            if line has speaker+'':

     
if __name__ == "__main__":
    main()
