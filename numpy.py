import numpy as np

# Create a NumPy array of size 3x21 with integer values from 1 to 63
arr = np.arange(1, 64).reshape(3, 21)
print(arr)

# Reshape it into two arrays of size 7x9 and 9x7 respectively
arr_7x9 = arr.reshape(7, 9)
arr_9x7 = arr.reshape(9, 7)

# Find the integer values at the center of the arrays
center_3x21 = arr[1, 10]
center_7x9 = arr_7x9[3, 4]
center_9x7 = arr_9x7[4, 3]

# Calculate mean of each row of the arrays
mean_row_3x21 = np.mean(arr, axis=1)
mean_row_7x9 = np.mean(arr_7x9, axis=1)
mean_row_9x7 = np.mean(arr_9x7, axis=1)

# Print the results
print("Integer value at the center of the 3x21 array:", center_3x21)
print("Integer value at the center of the 7x9 array:", center_7x9)
print("Integer value at the center of the 9x7 array:", center_9x7)
print("\nMean of each row of the 3x21 array:\n", mean_row_3x21)
print("\nMean of each row of the 7x9 array:\n", mean_row_7x9)
print("\nMean of each row of the 9x7 array:\n", mean_row_9x7)
