# Numpy_자료형 실습(1) 
import numpy as np
# int 와 int_는 다르므로 사용시 주의!
# 약칭으로 보통 int32 or int64
# int 타입의 넘파이 배열
a = np.int_([1,2,3,4,5])
print(type(a))
print(a.dtype)

# _를 하지 않고 하면 타입에러가 발생한다.
#a = np.int([1,2,3,4,5])
print(type(a))
print(a.dtype)

#float_로 실수 지정.
x = np.float_(4)
print(x)
print(x.dtype)

# 타입지정 1
ar1 = np.arange(10, dtype = np.uint8)
print(ar1)
print(ar1.dtype)

# 타입지정 2
ar2 = np.arange(10, dtype="uint8")
print(ar2)
print(ar2.dtype)

# 타입지정 3
ar3 = np.arange(10, dtype = 'u8') # 자료형에 대한 문자 코드 uint64 = u8
print(ar3)
print(ar3.dtype)
# uint64 = u8 (8 x 8 =64) , uint32 = u4 (4 x 8 = 32), uint16 = u2 (2 x 8 = 16), uint8 = u1 (1 x 8 = 8)

# str 문자형식으로 바꿔라
a = np.dtype('uint32')
print(a.type)
print(a.str) # <u4 코드 문자형식으로 출력