'''
from scipy.special import factorial

n =5
result = factorial(n, exact=True)   # exact=True is given for avoiding the float number in decimal anfd for getting whole number
print("factorial of", n, "is", result)
'''

'''
from scipy.stats import norm

mean = 0
std_dev = 1
x = 1.5

pdf_value = norm.pdf(x, mean, std_dev)
cdf_value = norm.cdf(x, mean, std_dev)

print("probability density function at x:", pdf_value)
print("cumulative distribution function at x:", cdf_value)
'''
'''
from scipy.optimize import minimize

def func(x):
    return x**2 + 5*x + 10
result = minimize(func, x0 = 0)
print("minimize value :", result.fun)
print("minimizer:", result.x)
'''
'''
from scipy.optimize import minimize

def func(x):
    y = x**2 + 5*x + 10
    print('x = ', x, 'y = ', y)
    return y
result = minimize(func, x0 = 0)
print("minimize value :", result.fun)
print("minimizer:", result.x)
'''

'''
import numpy as np
from scipy.interpolate import interp1d   # interpolate 1 dimension array

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

interp_func = interp1d(x, y, kind = 'cubic')

new_x = 2.5
interp_value = interp_func(new_x)
print("Interpolated value at x =", new_x, "is", interp_value)
'''

'''
# Define function to be intergrated :-
import numpy as np
from scipy import integrate

def func(x):
    return np.sin(x)
# Perform numerical intergration using scipy intergrate.quad
result, error = integrate.quad(func, 0, np.pi)

# Print the result
print("Numerical Intergration Result:")
print("Intergral value:", result)
print("Estimated error:", error)
'''

import numpy as np
from scipy import stats, optimize, interpolate

# generating sample data

x = np.linspace(0, 10, 20)
y = np.sin(x) + np.random.normal(0, 0.1, 20)

print(x)
print(y)


def func(x, a, b):
    return a* np.sin(b * x)
params, parmas_covariance = optimize.curve_fit(func, x, y)
print("curve fitting parameter:")
print("Amplitude (a):", params[0])
print("Frequency (b):", params[1])

data= np.random.rand(100)
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

print("\nStatistical Operations:")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)



