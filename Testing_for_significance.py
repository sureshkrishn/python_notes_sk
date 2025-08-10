
import numpy as np
import statsmodels.api as sm

#sample data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Add a constant term for intercept
X = sm.add_constant(x)

#Fit a linear regression model
model = sm.OLS(y, X).fit()

#Get the summary of the regression model
summary = model.summary()
print(summary)