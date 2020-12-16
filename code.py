import numpy as np

# data
x = np.array([[6, 148, 72, 35, 0, 33.6, 0.627, 50]])
y = np.array([[1, 85, 66, 29, 0, 26.6, 0.351, 31]])

# def d(x,y):
#   arr = np.concatenate((x, y))
#   np.reshape(arr, ()))
#   for att in arr:

arr = np.concatenate((x,y))
np.reshape(np.ravel(arr), (2, 10))
print(arr)