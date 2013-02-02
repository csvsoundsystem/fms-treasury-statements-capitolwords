#!/usr/bin/env python2

import os
import json
import dumptruck

dt = dumptruck.DumpTruck(dbname = '/tmp/capitolwords.db')

def insert(phrase):
    for page in os.listdir(phrase):
        f = open(os.path.join(phrase, page))
        d = json.load(f)
        f.close()

        dt.insert(d['results'], 'result')

def main():
    import sys
    usage = "USAGE: %s [phrase]" % sys.argv[0]
    if len(sys.argv) != 1:
        print(usage)
        exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print(usage)
        exit(1)

    phrase = sys.argv[1]
    insert(phrase)
