import pandas as pd 
from scipy.stats import pearsonr 

df = pd.read_csv('data.csv')


before = df.iloc[:,1]
after = df.iloc[:,2]

# Correlation coefficients 
correlation_coefficient, p_value = pearsonr(before, after)

alpha = 0.01 # Significance of 1%
if p_value < alpha:
    significance = "Significant"
else:
    significance = "Not significant"

print("Correlation Coefficient:", correlation_coefficient)
print("Significance:", significance)
