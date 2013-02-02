#!/usr/bin/env python2

import os
import json
import dumptruck

dt = dumptruck.DumpTruck(dbname = '/tmp/capitolwords.db')

def insert(phrase):
    for page in os.listdir(phrase):
        if page[-5:] != '.json':
            continue

        try:
            f = open(os.path.join(phrase, page))
            d = json.load(f)
            f.close()

            for row in d['results']:
                row['phrase'] = phrase
                for k,v in row.items():
                    if v == None:
                        row[k] = ''

            dt.insert(d['results'], 'result')
        except:
            print page
            raise

def main():
    import sys
    usage = "USAGE: %s [phrase]" % sys.argv[0]
    if len(sys.argv) != 2:
        print(usage)
        exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print(usage)
        exit(1)

    phrase = sys.argv[1]
    insert(phrase)

if __name__ == '__main__':
    main()
