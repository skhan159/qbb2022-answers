What a wild implementation! Needlman-Wunsch is almost entirely correct (a few very small issues), and then I have a few other comments:

First, the way you're filling in your traceback matrix, the first row should be full of `2`, not `4`, as this first row represents leading gaps in sequence 1. This matters for the DNA alignment, as there are some leading gaps. So your DNA alignment and alignment stats are actually slightly off. (-0.25)

My biggest issue is that you have this giant `if/else` statement checking the scoring matrix file name. There's no need for this, as the code inside this loop is essentially identical between the the DNA and AA alignments, it looks like the only thing that changes is the output file name you used. And we actually asked you to make the name of the output file a user input (so this giant conditional wouldn't be necessary) (-0.5)

I really like your choice to use `pandas` for the scoring matrix, I think that's a great choice that makes things a little more intuitive.

Really really great work overall though!

9.25/10
