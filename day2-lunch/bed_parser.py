#!/usr/bin/env python3

import sys
#import program
def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist") #file handling
    bed = []
    field_types = [str, int, int, str, int, str, int, int] #defines field types in the bed file
    for i, line in enumerate(fs):
        if line.startswith("#"): #ignore headers
            continue
        fields = line.rstrip().split() #strip and split lines into a list
        fieldN = len(fields) #measure the length of the list
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed", file=sys1.stderr) #bed files less than 3 columns or only has 10 or 11 columns are prohibited
            continue
        try:
            for j in range(fieldN):
                if j in range(0, 8):
                    fields[j] = field_types[j](fields[j]) #print the line and type for ranges 1-8
                elif j == 8:
                    fields[j] = fields[j].split(",")
                    fields[j] = [int(i) for i in fields[j]]
                    assert len(fields[8]) == 3 #remove the comma between each value and split the values between and check there are 3 total as a result in the list
                elif j == 9:
                    fields[j] = int(fields[j]) #record the 9th member if the list as an integer
                elif j == 10 or 11:
                    fields[j] = fields[j].rstrip(",").split(",")
                    fields[j] = [int(i) for i in fields[j]]
                    assert fields[9] == len(fields[j]) #split and remove the comma for members 10 and 11 in the list and make sure the length of the resulting unit is the same as the integer in fields 9
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr) #if these functions don't apply then print the line that failed
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    print(bed) #print the result
