# QBB2022 - Day 1 - Homework Exercises Submission
1.
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

2. 
#not defined at all

#used as a separate shell script:

vcffile=~/data/vcf_files/random_snippet.vcf
promofile=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed

bedtools intersect -a $vcffile -b $promofile > intersect_out_e2.bed

#and then used the file result from the top shell script to feed a second script:

for nuc in C
do
  echo "Considering " $nuc
  awk -v awkvar="$nuc" '/^#/{next} {if ($4 == awkvar) {print $5}}' $1 | sort | uniq -c
done

awk by itself without sort and uniq -c returns a large list of nucleotides, but after sorting and uniq -c then we get:
470 A
 382 G
2094 T

indicating that for nucleotide C, transitions between C and T are favored (due to the fact they are both pyrimidines).

3. 
#first line removes headers from the vcf, prints only the first two columns (chromosome and start position). Bedtools closest requires BOTH lists to be sorted!
#also requires tab delineation

to do so:

#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} BEGIN{OFS="\t"} {print $1,$2-1, $2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed

then:

cut -f 4 genes.sorted.bed | sort | uniq -c | wc -l = 19991 unique genes, without sort and uniq (basically wc -l on genes.sorted.bed) 20017 variants, thus there is about 1 variant per gene.
