import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels
import statsmodels.api as sm

#sample data (replace with your own dataset)
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

#Fit a linear regression model using statsmodels
x = sm.add_constant(x)  #Add a constant term for the intercept
model = sm.OLS(y, x).fit()

#Residuals
residuals = model.resid

#Residual plot
plt.figure(figsize=(8,6))
plt.scatter(model.predict(), residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residual plot')
plt.xlabel('Predicate values')
plt.ylabel('Residuals')
plt.show()

#check fo normality of residuals using a Q-Q plot
sm.qqplot(residuals, line='s')
plt.title('Q-Q Plot')
plt.show()

#Histogram of residuals
plt.hist(residuals, bins=15, edgecolor='k', alpha = 0.7)
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

#check for hetroscedasticity (residuals vs. fitted values)
plt.scatter(model.predict(), residuals)
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Fitted values (check for Hetroscedasticity)')
plt.axhline(y=0, color='red', linestyle='--')
plt.show()

#Run a formal test for hetroscedasticity (eg., Breusch-Pagan Test)
_, p_value, _, _ = statsmodels.stats.diagnostic.het_breuschpagan(residuals, x)
print(f'p-value for Breusch-pagan test: {p_value}')
if p_value < 0.5:
    print('Hetroscedasticity Occurs')
else:
    print('Hetroscedasticity does not Occurs')

#Check if residuals are normally distributed using a Shapiro_wilk test
_, p_value = stats.shapiro(residuals)
print(f'p-value for shapiro-wilk test: {p_value}')
if p_value > 0.5:
    print('Normal Distribution')
else:
    print('Not a Normal Distribution')
