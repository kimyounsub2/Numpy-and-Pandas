# Numpy_np,arange(1) - arabge로 원하는 숫자 범위, 간격을 지정.
import numpy as np

arr = np.arange(10) # 0 ~ 9까지 출력된다.
print(arr)

arr1 = np.arange(0, 10, 3)
print(arr1) # 0 ~ 9까지 3을 더한값이 출력된다. 0 3 6 9

qrr2 = np.arange(0, 20, 2)
print(qrr2) # [ 0  2  4  6  8 10 12 14 16 18]

# Numpy_np,arange(2) - 짝수 출력, 0.5 간격

arr3 =np.arange(0, 21, 2)
print(arr3) # [ 0  2  4  6  8 10 12 14 16 18 20]

arr4 = np.arange(1, 10, 0.5)
print(arr4) # [1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5 9.  9.5]

# Numpy_np,arange(3) - arange + reshape , 3 x 3 행렬을 수동으로 만들면
arr5 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr5.shape)

arr6 = np.arange(9) # 0 ~ 9 까지 arange를 해주고 3 x 3의 행렬로 수도으로 만들어준다.
arr3x3 = arr6.reshape(3,3)
print(arr3x3)

# Numpy_np,arange(4) - 6 x 6 행렬 만들기
arr7 = np.arange(1, 37)
arr_6x6 = arr7.reshape(6,6)
print(arr_6x6)

arr8 = np.arange(1,10).reshape(3,3) # 한번에 작업할수 있다.
print(arr8)

arr9 = np.arange(100).reshape(10,10)
print(arr9)
print(arr9.shape)
print(arr9.size)
print(arr9.ndim)
print(arr9[0,9])
print(arr9[4,7])

