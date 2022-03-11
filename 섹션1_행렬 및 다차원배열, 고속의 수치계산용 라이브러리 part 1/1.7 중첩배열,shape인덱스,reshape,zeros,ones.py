# Numpy_arr[1,2] - 배열의 배열
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a[1,0]) # 4
print(a[0,2]) # 3
print(a[1,2]) # 6

# Numpy_np.shape(arr) - 넘파이 객체로부터 직접 호출
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape)
print(np.shape(arr)) # 넘파이 객체로부터 바로 호출할수 있다.
# Numpy_arr.shape[0] - shape로 행, 열만 구하기
print(arr.shape[0]) # (2,3)의 영번째여서 2이 출력된다.
print(arr.shape[1]) # (2,3)의 1번째여서 3이 출력된다.

# Numpy_reshape - 구조변경
arr1 = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]]) # (2,3)구조이다.
print(arr1)

arr2 = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]]).reshape(3,4) # (2,3)에서 (3,4)로 구조 변환
print(arr2)
print(arr2.shape)

# Numpy_zeros - 모든 요소를 0으로
arr = np.zeros((2,2))
print(arr) 
# 행렬간의 연산(+,-,*)결과 값을 저장할때 
# 처음에 0으로 만들어야 할때

# Numpy_ones - 모든 요소를 1로
arr = np.ones((2,2))
print(arr)