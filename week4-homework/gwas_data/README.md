#2
plink --vcf genotypes.vcf --pca 10
#3
plink --vcf genotypes.vcf --freq 
#4
plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --hide-covar --out GS451_phenotype_gwas_results.txt
plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --hide-covar --out CB1908_phenotype_gwas_results.txt
#5
#6
#7
the highest SNP for GS451 is in a empty region of chromosome 19, but it is possible that the SNP disrupts an enhancer or intron in the region.
the highest SNP for CB1908 is upstream of the ORF of tubulin alpha 1a, thus I would conclude that the SNP may disrupt the expression or transcription of the gene.