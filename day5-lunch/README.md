# QBB2022 - Day 5 - Lunch Exercises Submission

1. awk 'BEGIN={FS=","; OFS="\t"} /father/ {$1=$1; print $5, $6}' aau1043_dnm.csv | sort | uniq -c > fathers.txt
awk 'BEGIN={FS=","; OFS="\t"} /mother/ {$1=$1; print $5, $6}' aau1043_dnm.csv | sort | uniq -c > mothers.txt

cut -f 1 mothers.txt > mothers_cut.txt
cut -f 1 fathers.txt > fathers_cut.txt

join -1 2 -2 2 mothers_cut.txt fathers_cut.txt > final.txt #I see what I screwed up here. I joined using mothers as the first file, but then assigned the third number to be fathers instead in the python code. The rest of this file has been edited with the correct results.

awk 'BEGIN{FS=","; OFS=" "} {$1=$1; print}' aau1043_parental_age.csv | sort > ages.txt

join ages.txt final.txt > the_final_final.txt

2.
maternal age vs maternal mutations                     
OLS Regression Results                            
==============================================================================
Dep. Variable:     maternal_mutations   R-squared:                       0.228
Model:                            OLS   Adj. R-squared:                  0.226
Method:                 Least Squares   F-statistic:                     116.0
Date:                Wed, 07 Sep 2022   Prob (F-statistic):           6.88e-24 #not as significant as fathers
Time:                        20:22:19   Log-Likelihood:                -1158.1
No. Observations:                 396   AIC:                             2320.
Df Residuals:                     394   BIC:                             2328.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        2.5040      0.981      2.553      0.011       0.576       4.432
maternal_age     0.3776      0.035     10.772      0.000       0.309       0.446
==============================================================================
Omnibus:                       51.143   Durbin-Watson:                   2.141
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               75.501
Skew:                           0.845   Prob(JB):                     4.03e-17
Kurtosis:                       4.310   Cond. No.                         121.
==============================================================================


paternal age vs paternal mutations
  OLS Regression Results                            
==============================================================================
Dep. Variable:     paternal_mutations   R-squared:                       0.619
Model:                            OLS   Adj. R-squared:                  0.618
Method:                 Least Squares   F-statistic:                     639.6
Date:                Wed, 07 Sep 2022   Prob (F-statistic):           1.55e-84 #quite significant
Time:                        20:19:12   Log-Likelihood:                -1406.6
No. Observations:                 396   AIC:                             2817.
Df Residuals:                     394   BIC:                             2825.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       10.3263      1.702      6.066      0.000       6.979      13.673
paternal_age     1.3538      0.054     25.291      0.000       1.249       1.459
==============================================================================
Omnibus:                        7.687   Durbin-Watson:                   1.907
Prob(Omnibus):                  0.021   Jarque-Bera (JB):                8.185
Skew:                           0.256   Prob(JB):                       0.0167
Kurtosis:                       3.483   Cond. No.                         127.
==============================================================================

6. Run a t-test, p-value is 2.1986031793078793e-264 #very, very, very, very significant

7. using the OLS equation computed above: y = 1.3538(x) + 10.3263 we get 78.6932
