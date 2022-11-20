#Part 1
You can see that instead of being unsure about assigning a label to an ambiguous image, it will tend to assign a label
in order to be definitive about its answer. In essence, it does not appear to have the ability to "not know" and leave it as
such. For example, in the bottom right of the model performance image, it assigns incorrectly "pullover" with 74% confidence 
to a coat image despite sizable ambiguity (26%). Is it possible to tune the model to be more stringent with its choices?
Say, can the network be programmed with a setting to say "too ambiguous, skipped?" Even us humans would struggle with some of
these!

#Part 2
python xpresso_predict.py ./pretrained_models/K562_trainepoch.11-0.4917.h5 ./input_fasta/human_promoters.fa.gz predicted_expression.txt

python plotting.py ./Xpresso-predict/predicted_expression.txt ../espresso-predictions-human/416685-1.txt 

The correlation is exactly the same. At the extreme ends (beyond 1 and below -1) there appears to be some discordance between
the two, but generally they match up extremely well. 

