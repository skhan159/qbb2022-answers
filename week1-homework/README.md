1.1 - 50,000 and 150,000 #1,000,000x5/100 or 1,000,000x15/100
1.3 - 7227 no coverage in genome, 6737 poisson predicted #both calculations are completed in the python script
1.4 - 11 no coverage in genome, 0.3 poisson predicted #both calculations are completed in the python script
2.1 - 4 contigs #spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31
#note that for spades to run the files need to be within the location of the spades.py directory, but the output is to a separate asm folder denoted by the -o flag
2.2 - 234,497 #since a scaffold is all overlapping contigs, I did samtools faidx scaffolds.fasta then less on scaffolds.fasta.fai
2.3 - 105,830 #this required samtools faidx contigs.fasta and then less contigs.fasta.fai
2.4 - 47,860 #If 1/2 of the total scaffold size is ~117,248, then regardless of which direction you go in (node 1 to 4 or 4 to 1) the 2nd contig is the N50.
3.1 - 99.98% #dnadiff ref.fa contigs.fasta
#nucmer ref.fa scaffolds.fasta 
#show-coords out.mdelta 
3.2 - 207,007 #also show-coords out.mdelta
3.3 - 15 #less out.report
4.1 - 