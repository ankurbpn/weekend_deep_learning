import sys
import os


def main():
    # my code here
    if len(sys.argv) != 4:
        print "Usage: python extract.py infilename speakername outfilename"
    speaker = sys.argv[2]
    for line in open(sys.argv[1], 'r'):
        if line

     
if __name__ == "__main__":
    main()
