import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Mean
mean_before = df.iloc[:,1].mean()
mean_after = df.iloc[:,2].mean()

# Absolute difference
abs_diff_before = np.abs(df.iloc[:,1] - mean_before)
abs_diff_after = np.abs(df.iloc[:,2] - mean_after)

# Calculate mean absolute deviation
mad_before = np.mean(abs_diff_before)
mad_after = np.mean(abs_diff_after)

# Print the mean absolute deviation
print("Mean Absolute Deviation Before:", mad_before)
print("Mean Absolute Deviation After:", mad_after)
