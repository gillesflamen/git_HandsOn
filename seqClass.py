#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper().strip().replace(" ","")                 # Note we just added this line

#here we are seaking for RNA DNA specific nucleotides
if not re.search('^[ACGTU]+$', args.seq):
    print ('The sequence is not DNA nor RNA')
elif 'U' in args.seq and 'T' in args.seq:
    print('The sequence is neither DNA nor RNA')
elif re.search('U', args.seq):
    print ('The sequence is RNA')
elif re.search('T', args.seq):
    print ('The sequence is DNA')
else:
    print ('The sequence can be DNA or RNA')

#here we are looking for the motifs added in the input
if args.motif:
    args.motif = args.motif.upper()
    print('Motif search enabled, output:')
    if re.search(args.motif, args.seq):
        print("FOUND found found")
    else:
        print("motif NOT FOUND")
