Really great work! Just one minor issue:

1. When you're making your boxplot, I think you have an off by one issue. You're starting your count at `1`, but I think you should start it at `0`. (It doesn't look like your `IC50` dataframe has a header line) As such, I think your boxplot is plotting the data for the SNP *next to* the most significant SNP. That's why the boxplot doesn't look like there's a strong relationship (-0.5 point)

You've done a great job here!

(9.5/10)
