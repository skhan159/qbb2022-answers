#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, int, str, int, int]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        try:
            for j in range(fieldN):
                if j in range(0, 8):
                    fields[j] = field_types[j](fields[j])
                elif j == 8:
                    fields[j] = fields[j].split(",")
                    fields[j] = [int(i) for i in fields[j]]
                    assert len(fields[8]) == 3
                elif j == 9:
                    fields[j] = int(fields[j])
                elif j == 10 or 11:
                    fields[j] = fields[j].rstrip(",").split(",")
                    fields[j] = [int(i) for i in fields[j]]
                    assert fields[9] == len(fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
