import pandas as pd
import numpy as np

# Series 연산
ar = pd.Series([1,2,3,4,5])
print(ar)
print(ar*2)

# 추가 인덱스 지정시 값이 없으면 NaN(Not a Number)
a = {"외데고르" : 100, "사카" : 95 ,"스미스로우" : 90 }
arr = pd.Series(a)
print(arr)
# 인덱스 추가
ix_name = {"김윤섭", "외데고르", "사카", "스미스로우"}
ar1 = pd.Series(a, index = ix_name)
print(ar1)

# Series에서 2차원 배열을 생성하려고 하면 에러가 발생한다.
br = pd.Series(np.array([1,2,3])) #1차원이라서 오류가 안난다.
print(br)
br1 = pd.Series(np.arange(1,6,1)) #1차원이라서 오류가 안난다.
print(br1)
# br2 = pd.Series(np.arange(1,31).reshape(5,6)) 2차원이라서 오류가 난다.
