#!/usr/env/bin python

import argparse
import random
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputfiles", dest="inputfiles", help="list of input files to select a random word from", required=False, nargs='+', default=[])

args = ap.parse_args()
cn=[]
for f in args.inputfiles:
    with open(f, 'r') as fd:
        cn.append( random.choice(fd.readlines()).strip() )
print(' '.join(cn))
        