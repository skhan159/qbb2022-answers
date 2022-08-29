# QBB2022 - Day 1 - Homework Exercises Submission
#1.
#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v awkvar="$nuc" '/^#/{next} {if ($4 == awkvar) {print $5}}' $1 | sort | uniq -c
done

#nuc needs to be defined as a shell script variable outside of the single quotes using -v

Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G

transitions are more likely than transversions