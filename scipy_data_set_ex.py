import numpy as np
from scipy import stats
#sample data
data = np.array([10, 15, 12, 18, 20, 25, 14, 22, 16, 19])
#calculate mean and std deviation
mean_value = np.mean(data)
std_deviation = np.std(data)

print("mean:", mean_value)
print("std deviation:", std_deviation)

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 8, 6])
#working on in-build functions of scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
print("Finding line regress functions using scipy:-----")
print("slope:", slope)
print("intercept:", intercept)
print("r_value:", r_value)
print("p_value:", p_value)
print("std_error:", std_err)

#creating Two independent gropups
group1 = np.array([23, 25, 18, 27, 21])
group2 = np.array([30, 29, 31, 28, 27])

t_statistic, p_value = stats.ttest_ind(group1, group2)
print("creating Two independent gropups :-----")
print("t_statistic:", t_statistic)
print("p_value:", p_value)
