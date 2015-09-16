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

    validateInput()

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



if __name__ == '__main__':
    main()
