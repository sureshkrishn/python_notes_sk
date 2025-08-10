from statistics import mean
import numpy as np
from matplotlib import style, pyplot as plt

def calculate_slope_intercept(xvalues, yvalues):
    m = (((mean(xvalues) * mean(yvalues)) - mean(xvalues * yvalues)) /
         ((mean(xvalues) * mean(xvalues)) - mean(xvalues * xvalues)))
    b = mean(yvalues) - m * mean(xvalues)
    return m, b

def linear_regression(xvalues, yvalues, m, b):
    regression_line = [(m * x) + b for x in xvalues]
    style.use('ggplot')
    plt.title('Training data & Regression line')
    plt.scatter(xvalues, yvalues, color='#003F72', label='Training data')
    plt.plot(xvalues, regression_line, label='Regression line')
    plt.legend(loc='best')
    plt.show()

def test_data(xvalues, m, b):
    predict_xvalue = 7
    predict_yvalue = (m * predict_xvalue) + b
    print('test data for x :  ', predict_xvalue, '    ',
          'test data for y :  ', predict_yvalue)
    plt.title('train, reg line, test value')
    plt.scatter(xvalues, yvalues, color='#003F72', label='data')
    plt.scatter(predict_xvalue, predict_yvalue, color='#ff0000',
                label='predicted_value')
    plt.legend(loc='best')
    plt.show()

def validate_results(m, b):
    predict_xvalues = np.array([2.5, 3.5, 4.5, 5.5, 6.5], dtype=np.float64)
    predict_yvalues = [(m * x) + b for x in predict_xvalues]
    print('Validation dataset')
    print('X value', predict_xvalues)
    print('Y value', predict_yvalues)

xvalues = np.array([1, 2, 3, 4, 5], dtype=np.float_)
yvalues = np.array([2, 4, 6, 8, 10], dtype=np.float_)

m, b = calculate_slope_intercept(xvalues, yvalues)
print('slope :  ', m, 'Intercept :  ', b)

linear_regression(xvalues, yvalues, m, b)
test_data(xvalues, m, b)
validate_results(m, b)
