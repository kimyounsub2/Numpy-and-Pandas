# Numpy_자료형 실습 - 자료형 확인 - np.issubdtype
import numpy as np

ar = np.arange(10, dtype=np.uint32)

ar1 = ar.astype(np.float64)
print(ar1)
print(ar1.dtype)

print(np.issubdtype(ar.dtype,np.integer)) # ar이 정수형인데 정수형이 맞는지 물어본다. True로 출력된다.

# print(np.issubdtype(ar.dtype,np.float)) # ar이 정수형인데 실수인지 물어본다. 하지만 float -> floating로 써줘야 에러가 안난다.
print(np.issubdtype(ar.dtype,np.floating)) # ar은 정수이니가 실수가 아니라서 False로 출력


# 다양한 np.issubdtype 사용법
print(np.issubdtype(ar.dtype,np.float64)) # False ar은 정수이기 때문에 
print(np.issubdtype(ar1.dtype,np.float64)) # True

