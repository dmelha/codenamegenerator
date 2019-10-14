#!/usr/env/bin python

import argparse
import random
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputfiles", dest="inputfiles", help="list of input files to select a random word from", required=False, nargs='+', default=[])

args = ap.parse_args()
cn=[]
for f in args.inputfiles:
    with open(f, 'r') as fd:
        #filter commented lines
        cn.append( random.choice(list(filter(lambda x: not x.startswith("#") and not x.strip()=="",fd.readlines()))).strip() )
print(' '.join(cn))
        