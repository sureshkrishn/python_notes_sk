import numpy as np
from matplotlib import style, pyplot as plt

x = np.array ([1, 2, 3, 4, 5])
y = np.array ([2, 4, 6, 8, 10])

test_x = np.array([3, 6, 8, 10])
test_y = np.array([6, 12, 16, 20])

'''
mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x -mean_x) ** 2)
m = numerator / denominator
b = mean_y -m * mean_x
'''
m, b = np.polyfit(x, y, 1)

y_pred = m * test_x + b

residuals = test_y - y_pred
ss_residuals = np.sum(residuals ** 2)
ss_total = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (ss_residuals / ss_total)

print('slope:  ', m, 'Intercept: ', b)
print(f"Regression Equation: y = {m:.2f}x + {b:.2f}")
print("Pred: ", y_pred)
print(f"R-squared value : {r_squared:.2f}")

thershold = 0.7
if r_squared >= thershold:
    print("R-squared is above the acceptable thershold.")
else:
    print("R-squared is below the acceptable thershold.")

plt.title('Best Fit Line')
plt.scatter(x, y, color= '#003F72', label = 'Orginal values')
plt.scatter(x, y_pred, color= '#ff0000', label='Predicated values')
plt.plot(x, y, label='Reg Line')
plt.legend(loc='Best')
plt.show()