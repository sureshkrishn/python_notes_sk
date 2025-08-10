import numpy as np
from numpy import mean
from scipy.stats import f

def calculate_slope_intercept(xvalues, yvalues):
    m = (((mean(xvalues) * mean(yvalues)) - mean(xvalues * yvalues)) /
         ((mean(xvalues) * mean(xvalues)) - mean(xvalues * xvalues)))
    b = mean(yvalues) - m * mean(xvalues)
    return m, b
def linear_regression():
    regression_line = [(m * x) + b for x in xvalues]
    return regression_line

def determination_coeff(ys_orig, ys_line):
    y_mean = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean)
    print('SER:', squared_error_regr)
    print('SEYM:', squared_error_y_mean)
    err_value = squared_error_regr / squared_error_y_mean
    print('EV:', err_value)
    rsq = 1 - (squared_error_regr / squared_error_y_mean)
    return rsq

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))

#driver

xvalues = np.array([1, 2, 3, 4, 5], dtype=np.float_)
yvalues = np.array([2, 4, 6, 8, 10], dtype=np.float_)

m, b = calculate_slope_intercept(xvalues, yvalues)
print('slope :  ', m, 'Intercept :  ', b)

regression_line = linear_regression()
print(regression_line)

Rsq = determination_coeff(yvalues, regression_line)
print('Rsq', Rsq)

thershold = 0.4
if (Rsq > thershold):
    print('Acceptable range')
else:
    print('Not acceptable range')

#perform an F-test to test the significance of R Squared
n = len(yvalues)
k = 1 # Number of independent variable(including the intercept)
dof_reg = k
dof_resid = n-k-1  #drgrees of freedom for the residuals

#calculate the explained variance (numerator)
explained_variance = squared_error(yvalues, regression_line)

#calculate the residual variance(denominator)
residual_variance = squared_error(yvalues, mean(yvalues))

#calculate the F-statistic
F= (explained_variance / dof_reg) / (residual_variance / dof_resid)

#calculate the p-value associated with F-statistic
p_value = 1 - f.cdf(F, dof_reg, dof_resid)

print("F-statistic:", F)
print("p-value:", p_value)

#set the significance level
alpha = 0.05

#perform the hypothesis test
if p_value < alpha :
    print("R-squared is statistically significant."
          "Reject the null hypothesis.")
else:
    print("R-squared is not statistically significant."
          "Fail to reject the null hypothesis.")

