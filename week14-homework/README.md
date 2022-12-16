python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197 #rinse and repeat

ktImportText -q SRR492193_krona.txt -o SRR492190.txt #rinse and repeat

Question 1: the microbiome is dominated by E. faecalis.

Question 2: BLAST

bwa index metagenomics_data/step0_givendata/assembly.fasta

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.sam #rinse and repeat

samtools sort SRR492183.sam -o SRR492183s.bam #rinse and repeat

Question 3A: 6

Question 3B: 
grep ">" bin.1.fa | wc -l (55)
grep ">" bin.2.fa | wc -l (78)
grep ">" bin.3.fa | wc -l (8)
grep ">" bin.4.fa | wc -l (37)
grep ">" bin.5.fa | wc -l (13)
grep ">" bin.6.fa | wc -l (6)
							= 197 / 4103 = 4.8%
							
3C: wc -m bin.6.fa gives you an estimate in base pair count, reasonable around 2M base pairs for proks

3D: BLAST





