#step 1
bwa index sacCeer3.fa

#step 2, 3a, 3b
for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
	bwa mem -t 4 -R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" -o ${SAMPLE}.sam sacCer3.fa ${SAMPLE}.fastq
	samtools sort -@ 4 -O bam -o ${SAMPLE}.bam ${SAMPLE}.sam
	samtools index ${SAMPLE}.bam
done

#step 4
freebayes -f sacCer3.fa --genotype-qualities -p 4 *.bam > yeast.vcf

#step 5
vcffilter -f "QUAL > 20" yeast.vcf > filtered.vcf

#step 6
vcfallelicprimitives -kg filtered.vcf > filtered2.vcf

#step 7

