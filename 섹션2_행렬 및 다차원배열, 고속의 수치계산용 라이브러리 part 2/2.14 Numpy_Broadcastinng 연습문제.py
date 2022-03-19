# Numpy_Broadcasting 연습문제
import numpy as np

#(문제) 아래의 배열 a,b,c에 대해서 각각의 형상을 말해보시오? 그리고 a+b, a+c의 연산이 가능한지와(브로드캐스팅)
#그 결과 배열의 형상은 어떻게 나올지에 대해서도 말해보시오?

a = np.array([[1],[2],[3],[4],[5],[6]])
b = np.array([1,2,3])
c = np.array([[1,2,3]])

# 001) 각각의 형상(shape)은? a= (6,1) 2차원  b = (3,)1차원 c = (1,3)2차원
# 002) a + b 연산의 결과 배열의 형상(shape)은? 6x3
# 003) a + c 연산의 결과 배열의 형상(shape)은? 6x3
print((a+b).shape)