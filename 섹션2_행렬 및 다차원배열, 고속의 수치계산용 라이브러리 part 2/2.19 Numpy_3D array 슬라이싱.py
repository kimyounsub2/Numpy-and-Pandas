# Numpy_3D array slicing(슬라이싱) - 3차원 배열 슬라이싱

import numpy as np

a = np.arange(1,51).reshape(2,5,5)
print(a)

# [37,38,39],[42,42,44],[47,48,49]를 출력해라
print(a[1,2:,1:4])
 