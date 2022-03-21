# Pandas_DataFrame - 조건식을 이용한 True,False 입력
import pandas as pd
import numpy as np


######### 예제1
raw_data = {
    "food" : ["apple","pear","peach","banana","orange","watermelon"],
    "month" : [1,2,3,4,5,6],
    "quantity" : [55,32,59,87,24,49]
            }

df1 = pd.DataFrame(raw_data, columns=["quantity","month","rank","food"])
print(df1) 
########


# 조건을 이용한 True, False 입력
df1["rank"] = df1.food == "apple"
print(df1)
df1["addcol"] = df1.food == "peach"
print(df1)

# 추가한 컬럼 삭제 -> del
# 물론 원하는 열(컬럼)을 삭제할 때도 가능
del df1["addcol"]
print(df1)

########## 예제 2
data = {
    "Seoul" : {2018:1, 2019:2, 2020:1},
    "Busan" : {2018:3, 2019:1, 2020:4}
}

df2 = pd.DataFrame(data=data)
print(df2)
###########



# 행과 열 바꾸기 -> T(Transpose) 대소문자 주의하자
print(df2.T) # 행과 열을 바꿔서 출력해준다.

# 특정 범위만 df로 생성(1)
df3 = pd.DataFrame(data, index = [2019,2020])
print(df3) 
df4 = pd.DataFrame(data=data, index=[2019,2020,2021])
print(df4)
# 특정 범위만 df로 생성(2)
x = {
    "Seoul" : df2["Seoul"][:2]
}
print(pd.DataFrame(x))
# 특정 범위만 df로 생성(3)
y = {
    "Busan":df2["Busan"][1:-1],
    "Seoul":df2["Seoul"][:-1]
}
print(pd.DataFrame(y)) # 열에 NaN이 들어가있을 경우 1.0으로 표시된다.

