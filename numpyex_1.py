import numpy as np


arr = np.arange(2,20,2, dtype = np.int_)     #dtype--data type we want
print(arr)

s = slice(2,5)
print("slice_1", arr[s])

s = slice(0,7,2)
print("slice_1 using step ", arr[s])

ans = arr[0:7:2]
print("using old slicing method using colon:", ans)