# Pandas_DataFrame - iloc, fillna NaN값 채우기 
import pandas as pd
import numpy as np

raw_data = {
    "food" : ["apple","pear","peach","banana","orange","watermelon"],
    "month" : [1,2,3,4,5,6],
    "quantity" : [55,32,59,87,24,49]
            }

df1 = pd.DataFrame(raw_data, columns=["quantity","month","rank","food"])
print(df1) 

# iloc 이용한 열 출력
print(df1.iloc[:,[1]]) # 1열만 출력해라
print(df1.iloc[:,[0,3]]) # 0, 3열만 출력해라
print(df1.iloc[:,[0,3,1]]) # 열의 입력한 순서대로 출력된다.

# NaN 값 숫자로 초기화 시키기 - >fillna(0)
print(df1.fillna(0)) # 값이 없던 rank값이 다 0으로 해서 출력된다.