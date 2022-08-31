#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0
#within list vcf, extract the selected headers into sets within list vcf and define the types using the type_map set
    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)
#file handling
    for h, line in enumerate(fs): #enumerate file
        if line.startswith("#"): #check if line is a header
            try:
                if line.startswith("##FORMAT"): #extract ##FORMAT header
                    fields = line.split("=<")[1].rstrip(">\r\n") + "," #split the header into a list and strip to clean it up
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=') #split out the equals sign from each member split in the list
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value #extraction of the values of the format header and giving them a description
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string #anything in quotes is thrown out
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"): #extract ##INFO header
                    fields = line.split("=<")[1].rstrip(">\r\n") + "," #split the header into a list and strip to clean it up
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=') #split out the equals sign from each member split in the list
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value #extraction of the values of the format header and giving them a description
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string #anything in quotes is thrown out
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t") #extract what is in header #CHROM
                    vcf.append(fields) #append fields to list vcf
            except:
                raise RuntimeError("Malformed header") #list error if header is not structured correctly
        else:
            try:
                fields = line.rstrip().split("\t") #extract literally everything else
                fields[1] = int(fields[1]) #1 is a integer
                if fields[5] != ".":
                    fields[5] = float(fields[5]) #if 5 has a decimal, make it a float
                info = {}
                for entry in fields[7].split(";"): #split the entries within 7 across the semicolon
                    temp = entry.split("=")
                    if len(temp) == 1:
                        info[temp[0]] = None #if the length of the split is 1, then set the display to None
                    else:
                        name, value = temp
                        Type = info_type[name]
                        info[name] = type_map[Type](value) #if the split length has values, assign them names and define them
                fields[7] = info
                if len(fields) > 8:
                    fields[8] = fields[8].split(":") #split 8 by the colon
                    if len(fields[8]) > 1:
                        for i in range(9, len(fields)):
                            fields[i] = fields[i].split(':') #if the length of 8 after the split is greater than 1, resplit
                    else:
                        fields[8] = fields[8][0]
                vcf.append(fields) #append these results to the vcf list
            except:
                malformed += 1
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description #assign the list members with descriptors
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf #end of the vcf list

if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname) #load the file we want to parse
    for i in range(10):
        print(vcf[i]) #print the vcf list we have made and parse the vcf file successfully (we hope)
