# Pandas_DataFrame - 생성, 대소문자, 인덱스지정, 다양한 df생성법
import pandas as pd
import numpy as np


# 기본 데이터 프레임 생성
# 대소문자도 주의하자 -> dataframe라고 하면 에러가 발생한다.
dftest = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]])
print(dftest)

# 가장 기본적인 형태.
# 인자로 파이썬의 중ㅇ첩 리스트를 넣으면 자동으로 행과 열에 대한 레이블이 만들어진다.
# 물론 이러한 레이블은 생성시 지정도 가능하다.

# 데이타프레임 생성시 인덱스 지정 
dftest1 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]],list('ab')) # 행을 a ,b 로 표시(인덱스)해준다.
print(dftest1)

# 데이타프레임 생성시 행과 열 레이블 지정
dftest2 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=["a","b"], columns=["a","b","c","d","e"])
print(dftest2) # (2,5)의 형태이니까 행과열의 갯수를 주의하자

# 다양한 df 생성 방식 -> 행과 열의 모양을 변경하는 여러가지 방법
df = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=["a","b"], columns=["a","b","c","d","e"])
df1 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=list("ab"), columns=list("abcde"))
df2 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=["a","b"], columns=list("abcde"))
df3= pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=list("ab"), columns=["a","b","c","d","e"])
print(df3)

# 변수 생성하여 변경할수 있다.
r = list("ab")
c = list("abcde")
df4 = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]], index=r, columns=c)
print(df4)

