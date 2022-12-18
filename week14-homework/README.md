python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
python script.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197

ktImportText -q SRR492183_krona.txt -o SRR492183.txt
ktImportText -q SRR492186_krona.txt -o SRR492186.txt 
ktImportText -q SRR492188_krona.txt -o SRR492188.txt 
ktImportText -q SRR492189_krona.txt -o SRR492189.txt 
ktImportText -q SRR492190_krona.txt -o SRR492190.txt 
ktImportText -q SRR492193_krona.txt -o SRR492193.txt 
ktImportText -q SRR492194_krona.txt -o SRR492194.txt 
ktImportText -q SRR492197_krona.txt -o SRR492197.txt 


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





