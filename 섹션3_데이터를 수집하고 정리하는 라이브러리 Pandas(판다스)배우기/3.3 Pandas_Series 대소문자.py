import pandas as pd
import numpy as np

# 대소문자 주의
# ar = pd.series([1,2,3,-4,5]) -> seris의 앞 s를 대문자로 써줘야 오류가 안단다. 
ar = pd.Series([1,2,3,-4,5]) # 파이썬 리스트
print(ar)

# 다양한 인자 입력
ar2 = pd.Series(np.array([1,2,3,-4,5]))

# 둘다 판다스의 시리얼 타입으로 출력된다.
print(type(ar)) # <class 'pandas.core.series.Series'>
print(type(ar2))

# index, value 정보 확인
print(ar2.index) # RangeIndex(start=0, stop=5, step=1) 행의 시작이 0이고 끝이 5이고 1씩 증가
print(ar2.values) #value s를 꼭붙여서 써야한다.

# Type Check
print(ar2.dtype) # int32
