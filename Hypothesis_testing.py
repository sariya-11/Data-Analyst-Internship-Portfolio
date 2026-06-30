import pandas as pd
from scipy.stats import ttest_ind
#Load dataset
df = pd.read_csv("cleaned_dataset.csv")
# Select purchase amount column
group1 = df["Purchase_Amount"].dropna()
# Split into two samples
mid = len(group1) // 2
sample1 = group1.iloc[:mid]
sample2 = group1.iloc[mid:]
# Perform T-test
t_stat, p_value = ttest_ind(sample1, sample2)
# Print results
print("T Statistic:", t_stat)
print("P Value:", p_value)
# Decision
if p_value < 0.05:
    print("Reject H0")
else:
    print("Accept H0")