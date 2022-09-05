# QBB2022 - Day 5 - Lunch Exercises Submission

1. awk 'BEGIN={FS=","; OFS="\t"} /father/ {$1=$1; print $5, $6}' aau1043_dnm.csv | sort | uniq -c > fathers.txt
awk 'BEGIN={FS=","; OFS="\t"} /mother/ {$1=$1; print $5, $6}' aau1043_dnm.csv | sort | uniq -c > mothers.txt

cut -f 1 mothers.txt > mothers_cut.txt
cut -f 1 fathers.txt > fathers_cut.txt

join -1 2 -2 2 mothers_cut.txt fathers_cut.txt > final.txt

awk 'BEGIN{FS=","; OFS=" "} {$1=$1; print}' aau1043_parental_age.csv | sort > ages.txt

join ages.txt final.txt > the_final_final.txt

2.
maternal age vs maternal mutations
OLS Regression Results                            
==============================================================================
Dep. Variable:     maternal_mutations   R-squared:                       0.482
Model:                            OLS   Adj. R-squared:                  0.481
Method:                 Least Squares   F-statistic:                     366.7
Date:                Fri, 02 Sep 2022   Prob (F-statistic):           2.96e-58 #very significant lol
Time:                        15:59:02   Log-Likelihood:                -1467.3
No. Observations:                 396   AIC:                             2939.
Df Residuals:                     394   BIC:                             2947.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       12.1348      2.141      5.669      0.000       7.926      16.343
maternal_age     1.4653      0.077     19.150      0.000       1.315       1.616
==============================================================================
Omnibus:                       19.496   Durbin-Watson:                   1.891
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               27.179
Skew:                           0.396   Prob(JB):                     1.25e-06
Kurtosis:                       4.010   Cond. No.                         121.
==============================================================================

paternal age vs paternal mutations
 OLS Regression Results                            
==============================================================================
Dep. Variable:     paternal_mutations   R-squared:                       0.130
Model:                            OLS   Adj. R-squared:                  0.128
Method:                 Least Squares   F-statistic:                     58.82
Date:                Fri, 02 Sep 2022   Prob (F-statistic):           1.37e-13 #not that significant
Time:                        15:59:52   Log-Likelihood:                -1181.7
No. Observations:                 396   AIC:                             2367.
Df Residuals:                     394   BIC:                             2375.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        5.6160      0.965      5.821      0.000       3.719       7.513
paternal_age     0.2327      0.030      7.669      0.000       0.173       0.292
==============================================================================
Omnibus:                       55.661   Durbin-Watson:                   2.158
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               84.236
Skew:                           0.897   Prob(JB):                     5.11e-19
Kurtosis:                       4.375   Cond. No.                         127.
==============================================================================

6. Run a t-test, p-value is 2.1986031793078793e-264 #very, very, very, very significant

7. using the OLS equation computed above: y = 0.2327(x) + 5.6160 we get 17.215
