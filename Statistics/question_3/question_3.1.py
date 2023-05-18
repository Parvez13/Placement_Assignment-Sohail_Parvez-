import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

mean_before = df.iloc[:,1].mean()
mean_after = df.iloc[:,2].mean()

bp_range_before = df.iloc[:,1].max() - df.iloc[:,1].min()
bp_range_after = df.iloc[:,2].max()-df.iloc[:,2].min()

variance_before = df.iloc[:,1].var()
variance_after = df.iloc[:,2].var()

std_before = df.iloc[:,1].std()
std_after = df.iloc[:,2].std()

print("Measure of dispersion(variance & standard deviation)")
print('The mean is of Blood Pressure Before: ',mean_before)
print('The range before BP: ',bp_range_before)
print('Variance: ',variance_before)
print('Standard deviation: ',std_before)
print("*"*50)
print('The mean is of Blood Pressure after: ', mean_after)
print('The range after BP: ', bp_range_after)
print('Variance: ', variance_after)
print('Standard deviation: ', std_after)
