# Pandas_DataFrame - loc 
import pandas as pd
import numpy as np

raw_data = {
    "food" : ["apple","pear","peach","banana","orange","watermelon"],
    "month" : [1,2,3,4,5,6],
    "quantity" : [55,32,59,87,24,49]
            }

df1 = pd.DataFrame(raw_data, columns=["quantity","month","rank","food"])
print(df1) 

# 특정한 행과 열의 값을 출력

# 먼저 행 --> loc
print(df1.loc[3]) # loc를 사용하면 행이 출력된다.

# 열(컬럼) 출력
print(df1.month)

# loc를 이용해서 원하는 행만 출력
# 1,5 행만 출력하시오?
print(df1.loc[1]) # 세로만 출력이 되지만
print(df1.loc[[1,5],["quantity","month","rank","food"]])

# 행만 표시하는 것도 가능하다
# 다양한 방식이 있고 에러 유형도 알자
# print(df1.loc[1,5]) # 이렇게 하면 에러가 난다 중괄호 추가하자
print(df1.loc[[1,5]]) # 첫번째 방법
print(df1.loc[[1,5],]) # 두번째 방법 ,를 찍어 열을 표시해주고 입력을 안해줘도 인식이 가능하다.
print(df1.loc[[1,5],:]) # 세번째 방법

