#1
medaka_variant -i methylation.bam -f hg38.fa -r chr11:1900000-2800000 -p -t 4
medaka_variant -i methylation.bam -f hg38.fa -r chr14:100700000-100990000 -p -t 4 -o medaka_variant2
medaka_variant -i methylation.bam -f hg38.fa -r chr15:23600000-25900000 -p -t 4 -o medaka_variant3
medaka_variant -i methylation.bam -f hg38.fa -r chr20:58800000-58912000 -p -t 4 -o medaka_variant4

#2
whatshap haplotag -o tagged_reads4.bam --reference hg38.fa --output-haplotag-list tagged_reads4.tsv medaka_variant4/round_0_hap_mixed_phased.vcf.gz methylation.bam
repeat for each

#3
whatshap split --output-h1 split_readsh1_2.bam --output-h2 split_readsh2_2.bam tagged_reads2.bam tagged_reads2.tsv
repeat for each

#4
samtools index split_readsh2_4.bam
repeat for each split

#6
different parent due to differential methylation patterns (due to the variable transposable elements that need to be silenced via piRNAs)

