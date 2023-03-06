import numpy as np

# 4x4 boyutunda sifirlardan olusan numpy array
array1 = np.zeros((4, 4))

# 4x4 boyutunda False degerlerden olusan numpy array
array2 = np.zeros((4, 4), dtype=bool)

print(array1)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]

print(array2)
#[[False False False False]
# [False False False False]
# [False False False False]
# [False False False False]]