# Numpy_행렬 곱셈

import numpy as np

ar1 = np.eye(2)
print(ar1)

ar2 = np.array([[3,4],[5,6]])
print(ar2)

# 곱셈을 해주는 함수가 따로 존재 한다.
ar1xar2 = np.dot(ar1, ar2)
print(ar1xar2)

# 만약 곱하기로 했다면 각 행 과 열을 곱해줘서 다른 숫자가 나온다.
test = ar1 * ar2
print(test)

a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[7,8]])
a3 = np.dot(a1,a2)
print(a3)
print(np.dot(a1,a2))