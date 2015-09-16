#!/usr/bin/env python

#
# NAME: sampleFastq.py
# AUTHOR: Philip Braunstein
# ORGANIZATION: BioSeq
# DATE CREATED: September 16, 2015
# LAST MODIFIED: September 16, 2015
#
# Makes a new FASTQ file with the percent of entries provided on the command
# line for the FASTQ file provided on the command line. This is a random
# sampling - it pays no attention to read quality.
#

from sys import argv
from sys import exit

def main():
    if len(argv) != 3:
        usage()

# Prints usage and exits non-zero
def usage():
    print "USAGE:", argv[0], "input_fastq percent_to_keep"
    exit(1)

if __name__ == '__main__':
    main()
