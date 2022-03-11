# Numpy_idnetical type(넘파이는 왜 빠르가?)
# 넘파일 요소는 모두 동일한 타입
# 그래서 파이썬 리스트보다 빠르다.

import numpy as np

arr3 = np.array([1,2,3,'a','b','c']) 
print(arr3[0])
print(type(arr3[0])) # 전체 문자열 형태로 변환되어 str 형태로 가진다.
print(type(arr3[3])) # 전체 문자열 형태로 변환되어 str 형태로 가진다.

lst = [1,2,3,'a','b','c']

print(lst[0])
print(type(lst[0])) # 첫번째 1이 출력되는데 숫자형태이니까 int가 출력된다.
print(type(lst[3])) # 네번재 a이 출력되는데 문자 형태이니까 str이 출력된다.