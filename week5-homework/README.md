Pt1
#1
samtools view -q 10 -b -o D2_Sox2_R2_input_filtered.bam D2_Sox2_R2_input.bam #repeat with different names for all 4 files
#2
macs2 callpeak -t D2_Sox2_R2_filtered.bam -c D2_Sox2_R2_input_filtered.bam -g 9.5e7 -n replicate2 -B
#3
bedtools intersect -a replicate1_peaks.narrowPeak -b replicate2_peaks.narrowPeak > intersected_reps.bam
#4
wc -l intersected_reps.bam #593 intersected
wc -l D2_Klf4_peaks.bed #60 intersected
bedtools intersect -a intersected_reps.bam -b D2_Klf4_peaks.bed > sox_klf_intersects.bam
wc -l sox_klf_intersects.bam #40 intersected
#5
python scale_bdg.py replicate1_treat_pileup.bdg scaled1.bdg #4x
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled2_treat.bdg > scaledcropped2_treat.bdg #4x

Pt2
#1,2,3
sort -k 5,5rn replicate1_peaks.narrowPeak | head -300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > manipulated_peaks.bed
#4
samtools faidx mm10.fa -r manipulated_peaks.bed -o sliced_peaks.bed
#5
meme-chip -maxw 7 sliced_peaks.bed 

Pt3
#1,2
tomtom combined.meme HOCOMOCOv11_full_MOUSE_mono_meme_format.meme 
#3,4
grep "KLF4\|SOX2" tomtom.tsv > matches.txt


