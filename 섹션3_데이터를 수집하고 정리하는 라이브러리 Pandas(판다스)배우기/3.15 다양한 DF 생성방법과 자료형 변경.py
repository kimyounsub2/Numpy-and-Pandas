# 넘파이 모듈을 포함한 종합실습 - 다양한 DF 생성방법과 자료형 변경
import pandas as pd
import numpy as np


# 데이터프레임 생성의 다양한 예

# DF생성시 보통 필요한것 --> data, index, column
_data = [[1,2,3],[4,5,6],[7,8,9]]
_index = list("abc")
_column = list("ABC")
df = pd.DataFrame(data=_data, index=_index, columns=_column)
print(df)

# 시리즈로 데이터프레임 생성
# 이때 시리즈의 자료형을 문자열로 전달
# 그럼 알아서 자료형을 추정해 값 세팅
dfseries = pd.DataFrame({"A":pd.Series([1,2,3,4],dtype="int"), "B":pd.Series([5,6,7,8],dtype="float")})
print(dfseries.ndim) # 2차원
print(dfseries.shape) #(4,2)
print(dfseries)
print(dfseries.dtypes) # A : int32 B : float64 dtype: object

# 리스트 개게로 데이터프레임 생성
# 값을 리스트로 전달
dflist = pd.DataFrame({"점수":[99,90,80,70], "학점":["A+","B","C+","D"]})
print(dflist)
print(dflist.dtypes)# 점수 : int64 ,학점 :object dtype: object

