import numpy as np


mx = np.arange(1, 10).reshape(3, 3)
print(mx)
original_rows, original_cols = mx.shape
print(original_rows, original_cols)
border_size = 1

# Calculate the new dimensions
new_rows = original_rows + 2 * border_size
new_cols = original_cols + 2 * border_size
print(new_rows, new_cols)
new_array = np.zeros((new_rows, new_cols), dtype=mx.dtype)
print(new_array)
new_array[0, 1] = 22
new_array[border_size:border_size + original_rows, border_size:border_size + original_cols] = mx
print()
# Print the new array
print(new_array)
