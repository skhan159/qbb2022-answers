# day 4 homework feedback

Good plots!

While you've submitted both heatmaps, I only see code for creating the uncorrected heatmap.

Regarding comments in your README file, great overall, just two small points:

* "We also ran the simulation once, while in the paper it is computed from 1000 iterations." -- your `n_iters` variable sets the number of iterations your simulation is run. We ran it 100 iterations rather than 1000.
* The binomial specifically is used because in the coin toss example you either have heads or tails, and in the biology example, you either inherit allele 1 or allele 2 -- so we have binary choices where the probability of one affects the probability of the other and each coin toss or sperm meiosis is independent from another toss or meiosis

One other small comment on your code: The assignment does ask you to incorporate the nested for loop and storing the power within the `run_experiment()` function rather than calling that function repeatedly. What you've done works and leads to the same conclusions, but consider how you might edit the function to incorporate the new code. While your results will be the same every time your script is run, will your results be the same compared to someone who only calls the `run_experiment()` function once therefore only sets the random seed once?
