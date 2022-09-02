This is a good start! 

A few notes: 

Ex.2

The definition of which chromatin states define a promoter is pretty ambiguous, but there are some marks that I think can associated pretty clearly. The TSS for example is usually considered as part of the core promoter. I would use these marks and an awk script subset the file `chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed` to promoter-like regions. From what I can tell, you are using the entire file without any subsetting as input for bedtools.

The general syntax of your bedtools intersect command looks good though! 

Your awk script at the end is also good! Because you are only looking for one nucleotide (C), there's no need to use the for loop and `awk -v`. This is a simpler awk command and would give the same result: `awk '{if ($4 == "C") {print $5}}'`. That said, your awk code definitely works.

What output do you get from awk? Please include that in your solution, along with any observations on the results. 

Ex. 3

Good start, and you have correctly identified the problems with this file. Could you include the sorting code you use to sort both codes, along with the code to convert to tab delineation and the correct bedtools closest command? 

- Andrew 
