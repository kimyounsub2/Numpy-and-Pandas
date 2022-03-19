import pandas as pd
import numpy as np

# 조건을 이용한 접근
# 조건은 값으로 비교

ar = pd.Series(["a","b","c","d","e"])
print(ar)
print(ar[3]) # d가 출력된다.

# a 이상만 출력하고 싶다면
print(ar[ar > "a"])

# 시리즈의 숫자 이상만 출력된다
br = pd.Series([1,2,3,4,5])
print(br)
print(br[br>3]) # 1 2 3 4 5에서 3이상이니까 4,5가 출력된다.
print(br[br>=3]) # 1 2 3 4 5에서 3이상이니까 3,4,5가 출력된다.
print(br[br!=3]) # 1 2 3 4 5에서 3빼고 1,2,4,5가 출력된다.