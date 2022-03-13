# Numpy_Datatype - 넘파이 데이타 타입

import numpy as np

ar1 = np.array([1,2, 3.5,4,5])
print(type(ar1))
print(ar1.dtype) # 요소중 3.5(실수)가 석여 있어 float64가 출력된다.

ar2 = np.array([1,2,3,4,5])
print(type(ar2))
print(ar2.dtype) # 모든 수가 정수이기 때문에

# 넘파이 배열 생성시 데이터타입 지정.
ar3 = np.array([1,2,3,4,5], dtype=np.int64)
print(type(ar3))
print(ar3.dtype) # int32 -> int64형태로 데이타타입을 변형시켜준것 

# 타입 뒤의 숫자는 몇 bit로 배열의 요소를 표시할지를 보여주는 타입

ar4 = np.array([1,2,3,4, 255], dtype=np.uint8) # 0 ~255
print(ar4) # [  1   2   3   4 255]

ar5 = np.array([1,2,3,4,0, 255], dtype=np.uint8) 
print(ar5) # [  1   2   3   4   0 255]

ar6 = np.array([1,2,3,0, 256], dtype=np.uint8) 
print(ar6) # [1 2 3 0 0]

ar7 = np.array([1,2,3,4, -1], dtype=np.uint8) 
print(ar7) # [  1   2   3   4 255]

ar8 = np.array([0,1,2,3,65535], dtype=np.uint16) # 0 ~ 65535 
print(ar8) # [ 0   1   2  3 65535]

ar9 = np.array([0,1,2,3,-1], dtype=np.uint32) # 0 ~ 42억 정도
print(ar9) # [ 0  1  2 3 4294967295]

# 기존 array --> 새로운 타입으로 변환
arr1 = np.array([1,2,3,4,5])
print(arr1.dtype)

arr2 = ar1.astype(np.float64) # 정수에서 실수로 변환 [1.  2.  3.5 4.  5. ]
print(arr2)
print(arr2.dtype)

# bool 참 거짓 타임으로도 출력가능하다

arar1 = np.array([True, False])
print(arar1.dtype)