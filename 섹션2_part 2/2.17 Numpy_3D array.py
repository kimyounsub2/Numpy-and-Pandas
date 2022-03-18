# Numpy_3D array - 3차원 배열 생성
import numpy as np

# 3차원 배열이다.
a = np.arange(1,25).reshape(2,3,4)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
# 2,3,4
b = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(b)
print(b.shape)
print(b.ndim)
print(b.size)
# 2,4,3
c = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[13,14,15],[16,17,18],[19,20,21],[22,23,24]]])
print(c)
print(c.shape)
print(c.ndim)
print(c.size)