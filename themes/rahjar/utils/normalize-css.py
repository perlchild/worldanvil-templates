#!/usr/bin/env python3
import sys,os, argparse,rcssmin
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename' )          # positional argument
args = parser.parse_args()
with open(args.filename,"r") as fd:
    print(rcssmin.cssmin(fd.read()))