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
    
    origRecords = readInFastq(argv[1])

    newRecords = pullNRandRecords(origRecords, int(round(len(origRecords) *\
                                                float(argv[2]))))

    writeOut(newRecords, getNewName(argv[1], argv[2]))

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


# Reads in a FASTQ file and returns a list of lists, where each inner list
# represents one entry in the FASTQ file.
def readInFastq(fileName):
    toReturn = []
    current = []
    counter = 0

    with open(fileName, 'r') as filer:
        for line in filer:
            # Time for new entry
            if counter % 4 == 0 and counter != 0:
                toReturn.append(current)
                current = []

            current.append(line)

            counter += 1

        # Get last entry
        toReturn.append(current)

    return toReturn


# Returns array with n random items from orig array. Assumes that n is
# less than or equal to len(orig)
def pullNRandRecords(orig, n):
    toReturn = []

    # Take care of all randomness
    random.shuffle(orig)

    for x in range(n):
        toReturn.append(orig[x])

    return toReturn


# Writes out the records to the file name provided
def writeOut(records, newName):
    with open(newName, 'w') as filew:
        for r in records:
            for x in r:
                filew.write(x)

    print "Done"
    print "New FASTQ written to", newName,


# Generates the name of the new file
def getNewName(oldName, dec):
    nL = oldName.split(".")
    return nL[0] + "_" + dec.split(".")[1] + "." + nL[1]


if __name__ == '__main__':
    main()
