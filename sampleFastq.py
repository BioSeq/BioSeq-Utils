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
import random

def main():
    if len(argv) != 3:
        print "Wrong number of command-line parameters"
        usage()

    validateInput()

    makeSampleFastq(argv[1], getNewName(argv[1], argv[2]), float(argv[2]))

    exit(0)
    


# Prints usage and exits non-zero
def usage():
    print "USAGE:", argv[0], "input_fastq decimal_to_keep"
    exit(1)


# Makes sure the first command-line argument is a fastq file, and the second
# is a decimal between 0 and 1. Otherwise calls usage (thus exits non-zero)
def validateInput():
    # Validate FASTQ
    if not argv[1].endswith(".fastq"):
        print argv[1], "is not a valid FASTQ file."
        print "First command-line parameter must be a FASTQ file"
        usage()

    # Validate decimal
    try:
        dec = float(argv[2])
    except ValueError:
        print argv[2], "is not an appropriate decimal (illegal characters)"
        print "Second command-line parameter must be a decimal between 0 and 1"
        usage()
    if dec < 0 or dec > 1:
        print dec, "is not an appropriate decimal"
        print "Second command-line parameter must be a decimal between 0 and 1"
        usage()


# Generates the name of the new file
def getNewName(oldName, dec):
    nL = oldName.split(".")
    return nL[0] + "_" + dec.split(".")[1] + "." + nL[1]


# Writes dec percentage of oldFile FASTQ entries into newFile
def makeSampleFastq(oldFile, newFile, dec):
    n = 0
    keep = False

    filew = open(newFile, 'w')
    with open(oldFile, 'r') as filer:
        for line in filer:
            if n % 4 == 0:
                if random.random() < dec:  # hit!
                    keep = True
                else:
                    keep = False

            if keep:
                filew.write(line)

            n += 1
        
    filew.close()


if __name__ == '__main__':
    main()
