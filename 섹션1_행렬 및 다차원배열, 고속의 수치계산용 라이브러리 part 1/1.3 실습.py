import numpy as np

ar1 = np.array([1,2,3,4,5])
print(ar1) # 넘파이에서는 1 2 3 4 5 이렇게 출력된다.

lst = [1,2,3,4,5]
print(lst) # 파이썬 리스트로 출력했을때 1,2,3,4,5로 출력된다.

# 배열의 모양(형태)를 알수있다.
ar1.shape
print(type(ar1))
print(ar1.shape)

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.ndim)