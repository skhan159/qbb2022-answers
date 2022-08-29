# QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn Python.
 2b. wc genes.chr21.bed gives 219 lines and wc exons.chr21.bed gives 13653 lines thus there are an average of 62 exons per gene using python to divide: 13653//219.
 2c. Figure out the amount of exons per gene by calculating where each gene starts and ends and the number of exons within the gene locuses, probably would require a python script.
 3b. cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c
 305 1
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
 3c. 7 is the largest fraction using the result of above.
 4b. grep AFR integrated_call_samples.panel | cut -f 2 | sort | uniq -c
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
4c. replace AFR with the other populations
5
 