################        DATED ON 06/08/2023      ###################

import matplotlib.pyplot as plt

#sample data
x = ['A', 'B', 'C', 'D', 'E']
y = [2, 4, 6, 8, 10]
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 40, 30, 70, 80]
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
''''
#create line plot
plt.plot(x, y, marker= 'o') 

#Add lables and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
'''
'''
#scatter chart
plt.scatter(x,y, marker = 'o', color = 'red')   #without line only dot, S = square
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter chart')
'''
'''
#Bar Chart
plt.bar(x,y, color = 'Purple')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot')

plt.scatter(categories, values)
plt.xlabel('cat')
plt.ylabel('val')
plt.title('Combine Chart')
'''
'''
#Histogram --- Its used for frequency
plt.hist(data, bins = 3, edgecolor = 'yellow')
plt.xlabel('cat')
plt.ylabel('val')
plt.title('Histogram Chart')
'''
'''
#Pie Chart
explodedata = (0, 0, 0, 0, 0.5)
col = ('blue', 'green', 'orange', 'pink', 'yellow')
plt.pie(values, labels = categories, shadow = True, explode = explodedata, autopct = '%1.0f%%', colors = col)
plt.title('Pie Plot')

'''
'''
import numpy as np
import matplotlib.pyplot as plt
# Sample data
x = np.linspace(0, 2 * np.pi, 50) #start, end, step value
y = np.sin(x)

print(x,y)

# Create a line plot
plt.plot(x, y, label='sin(x)', color='orange', linewidth=2, marker = 'o')

# Add labels and title
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')

# Add grid lines
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.show()

#show the plot
plt.show()

'''
#######################  DATED ON 20/08/2023       #####################
'''
#HISTOGRAM
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 100)
print(data)

# Create a histogram
plt.hist(data, bins=10, edgecolor='black', color='skyblue')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Custom Data')

# Show the plot
plt.show()

'''
'''

#LINE PLOT
import numpy as np
import matplotlib.pyplot as plt

# Sample data for the x-axis and two y-axis variables
# Replace these arrays with your own datasets
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a line plot with two data series
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Custom Data')

# Add legend to identify data series
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

'''
#LINE WITH MULTIPLE SERIES
import matplotlib.pyplot as plt

# Sample data for three data series
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [3, 6, 2, 5, 8]

# Create a line plot with multiple data series
plt.plot(x, y1, label='Series 1', marker='o')
plt.plot(x, y2, label='Series 2', marker='s')
plt.plot(x, y3, label='Series 3', marker='^')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Multiple Data Series')

# Add legend to identify data series
plt.legend()

# Show the plot
plt.show()