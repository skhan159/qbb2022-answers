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

Question 2: BLASTn alignments.

bwa index metagenomics_data/step0_givendata/assembly.fasta

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492183_1.fastq metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > SRR492183.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492186_1.fastq metagenomics_data/step0_givendata/READS/SRR492186_2.fastq > SRR492186.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492188_1.fastq metagenomics_data/step0_givendata/READS/SRR492188_2.fastq > SRR492188.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492189_1.fastq metagenomics_data/step0_givendata/READS/SRR492189_2.fastq > SRR492189.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492190_1.fastq metagenomics_data/step0_givendata/READS/SRR492190_2.fastq > SRR492190.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492193_1.fastq metagenomics_data/step0_givendata/READS/SRR492193_2.fastq > SRR492193.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492194_1.fastq metagenomics_data/step0_givendata/READS/SRR492194_2.fastq > SRR492194.sam 
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.sam 

samtools sort SRR492183.sam -o SRR492183s.bam
samtools sort SRR492186.sam -o SRR492186s.bam
samtools sort SRR492188.sam -o SRR492188s.bam
samtools sort SRR492189.sam -o SRR492189s.bam
samtools sort SRR492190.sam -o SRR492190s.bam
samtools sort SRR492193.sam -o SRR492193s.bam
samtools sort SRR492194.sam -o SRR492194s.bam
samtools sort SRR492197.sam -o SRR492197s.bam

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

4A: head bin.1.fa 
>NODE_12_length_269228_cov_106.168966
grep NODE_12_length_269228_cov_106.168966 ../metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
NODE_12_length_269228_cov_106.168966	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

head bin.2.fa 
>NODE_20_length_181746_cov_381.691663
grep NODE_20_length_181746_cov_381.691663 ../metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
NODE_20_length_181746_cov_381.691663	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A

head bin.3.fa 
>NODE_3_length_498518_cov_181.760000
grep NODE_3_length_498518_cov_181.760000 ../metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
NODE_3_length_498518_cov_181.760000	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548

head bin.4.fa 
>NODE_14_length_235766_cov_39.967778
grep NODE_14_length_235766_cov_39.967778 ../metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
NODE_14_length_235766_cov_39.967778	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435

head bin.5.fa 
>NODE_4_length_455101_cov_112.371015
grep NODE_4_length_455101_cov_112.371015 ../metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
NODE_4_length_455101_cov_112.371015	root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067

head bin.6.fa 
>NODE_1_length_1447137_cov_2268.097092
grep NODE_1_length_1447137_cov_2268.097092 ../metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
NODE_1_length_1447137_cov_2268.097092	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF

4B: Once again, BLAST can be used here.




