# QBB2022 - Day 4 - Homework Exercises Submission

A. the line outputs a list of floats that decrease in sequential order by 0.05.
The numpy.arange followed by the two floats indicates we want to make a list increasing sequentially by 0.05 for each member in the list between the two floats we specify for in the range argument.
The numpy.around rounds off the floats of the list down to two decimal places, preventing in case of manipulation that the respective members of the list do not go beyond 2 decimal places in length.
[::-1] indicates we want to start counting in reverse direction.

C. as flip number increases we increase our power. However, if we use hypothesis testing correction then we require a greater number of flips to achieve the same respective power in comparison to a flip count with no correction.

D. Mendelian genetics requires adherence to the the law of segregation when it comes to the creation of gametes via meiosis. The law of segregation states that each allele from each parent has an equivalent chance of being inherited in offspring. However, in some species, research has showed exceptions to this law in where "selfish" alleles segregate disproportionately in gametes. This study has utilized the statistical power of a large repository of single-cell sequenced sperm to examine if this unequal distribution of alleles occurs in humans.

In the referenced paper, a clear similarity between our simulation and their simulation is the difference in power that occurs when multiple testing correction is applied to the power determination. The transmission rate is similar to the coin fairness as well. However, the number of cells required is much higher than the number of flips of a coin to reach the same power (1000 max for coin, 10000 max for sperm). We also ran the simulation once, while in the paper it is computed from 1000 iterations.

Specifically, prob_heads or the fairness of the coin is equivalent to the transmission rate. Number of sperm is equivalent to n_toss, or the number of coin flips. 

We use a binomial test because we have calculated a theoretical distribution of the data based on simulating the results to determine power and the respective P-value that needs to be achieved if the second, tested distribution is deviated to the point that the first distribution (the null) is rejected.

