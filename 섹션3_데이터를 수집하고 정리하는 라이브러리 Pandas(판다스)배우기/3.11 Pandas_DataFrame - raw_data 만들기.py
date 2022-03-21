# Pandas_DataFrame - raw_data 만들기(순서 및 값 변경, 열 추가, 행열 정보 확인 )
import pandas as pd
import numpy as np

# raw_data 만들기
raw_data = {
    "food" : ["apple","pear","peach","banana","orange","watermelon"],
    "month" : [1,2,3,4,5,6],
    "quantity" : [55,32,59,87,24,49]
            }

df = pd.DataFrame(raw_data)
print(df)

# 컬럼(Column) 인덱스의 순서를 변경
df1 = pd.DataFrame(raw_data, columns=["month","food","quantity"])
print(df1)

# 행(Raw) 인덱스 값 변경
df1 = pd.DataFrame(raw_data, index=list("abcdef"))
print(df1)

# 컬럼 순서를 변경하면서 컬럼 하나를 추가
df1 = pd.DataFrame(raw_data, columns=["quantity","month","rank","food"])
print(df1) # rank는 값이 없기 때문에 NaN으로 표시된다.

# index(행), column(열) 정보 확인
print(df1.index) # RangeIndex(start=0, stop=6, step=1)
print(df1.columns) # Index(['quantity', 'month', 'rank', 'food'], dtype='object')