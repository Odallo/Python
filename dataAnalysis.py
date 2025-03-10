# import numpy as np

# array_id = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(array_id)
# print(type(array_id))

# array_3d = np.array([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]])
# print("Size:", array_3d.size) 
# print("Shape: ", array_3d.shape)
# print("Data Type: ", array_3d.dtype)

import numpy as np
# spaceship = np.array([2000, 3000, 5000, 7000])

# print("Spaceship: ", spaceship)
# print("Size: ", spaceship.size)
# print("Shape: ", spaceship.shape)
# print("Data Type: ", spaceship.dtype)
# print ("Item size: ", spaceship.itemsize)

# A boolean index for even numbers
# array_1d = np.array([8, 4, 7, 3, 4, 11])
# even_index = array_1d % 2 == 0
# even_numbers = array_1d[even_index]
# print(even_numbers)  # Output: [8 4 4]

# Select elements at odd indices 1, 3, 5, ...
array_1d = np.array([1, 2, 3, 4, 5, 6])
every_second = array_1d[1:4:2]
print(every_second)  # Output: [2 4 6]