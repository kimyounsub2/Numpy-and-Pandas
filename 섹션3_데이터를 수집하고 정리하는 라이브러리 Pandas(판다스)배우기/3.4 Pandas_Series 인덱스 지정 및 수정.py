import pandas as pd
import numpy as np


# 인덱스 속성을 이용하여 index 지정
ar = pd.Series([1,2,3,-4,5], index =["a","b","c","d","e"])
print(ar)

# 파이썬 딕셔너리로 인덱스 지정
pydic = {"서울":100, "부산":200, "광주":300, "세종":400}

arr = pd.Series(pydic)
print(arr)

# 시리즈 이름 지정 할수 있다.
arr.name = "대한민국 광역시" 
print(arr) # 인덱스 딕셔너리 아래에 Name: 대한민국 광역시, dtype: int64 출력된다.

# 인덱스를 이용한 접근
print(arr["서울"])
print(arr[0])
print(arr[1:3])

