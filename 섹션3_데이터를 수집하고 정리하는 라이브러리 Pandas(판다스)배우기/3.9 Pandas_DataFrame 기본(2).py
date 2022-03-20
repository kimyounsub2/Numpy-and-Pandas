# Pandas_DataFrame - values, index type, ndim, size, shape
import pandas as pd
import numpy as np

# values 속성
df = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=["a","b"], columns=["a","b","c","d","e"])
print(df.values)

# 2차원 배열로 출력
print(type(df)) # df로 타입을 보면 <class 'pandas.core.frame.DataFrame'> 데이타 프레임인걸 알수있다.

# 타입체크를 해보면 넘파이 배열
print(type(df.values)) # <class 'numpy.ndarray'>

# 그냥 df를 체크하면 DataFrame로 나옴
# df.values를 타입체크하면 넘파이 다차원 배열로 나옴

# 행과 열의 속성 타입체크 모두 index의 객체임을 알 수 있다.
print(df.index) # Index(['a', 'b'], dtype='object') 행의 타입이 객체로 출력
print(df.columns) # Index(['a', 'b', 'c', 'd', 'e'], dtype='object') 열의 타입이 객체로 출력

# 차원, 사이즈, 형태도 넘파이처럼 출력 가능하다.
print(df.ndim) # 2(2차원)
print(df.size) # 10(개수)
print(df.shape) # (2,5)모양

# 넘파이 함수를 이용해서 df생성 , 이때 reshape로 배열의 모양(형상)을 지정
dfa = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(dfa)
dfb = pd.DataFrame(np.arange(1,10).reshape(3,3))
print(dfb)
