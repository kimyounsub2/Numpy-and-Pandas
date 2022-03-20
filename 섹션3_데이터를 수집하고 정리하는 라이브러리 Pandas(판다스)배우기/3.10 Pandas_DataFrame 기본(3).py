# Pandas_DataFrame - 색인, 열기준처리, 넘파이로 df생성, 예외처리
import pandas as pd
import numpy as np

# 해당 숫자를 출력할때 데이타프레임음 좀다르다.

# 넘파이 기준 29를 출력
ar = np.arange(1,31).reshape(5,6)
print(ar)
print(ar[4,4])

# 데이타프레임 29출력
df = pd.DataFrame(np.arange(1,31).reshape(5,6))
print(df)
# print(df[4,4])로 출력하면 에러가 나온다.
print(df.loc[4,4]) # 행을 조회하려면 별도의 인덱서를 사용한다. -> loc

# 열 기준 색인 -> 넘파이랑 헷갈리지 말자 첫번째가 열기준
print(df[0]) # 이렇게 출력하면 0번째 행이 아니라 0번째 열로 출력된다.
print(df[0][0]) # 1
print(df[0][4]) # 25
# print(df[4][5]) # 에러(KeyError : 5) 5행이 없기 때문에
print(df[5][4]) # 30
print(df[3][2]) # 16

# 예외 처리 , 예외 처리를 하면 에러줄이 길게 안나온다.
try:
    print(df[4][5])
except Exception as e:
    print(e)
    
print(df[4][5])

