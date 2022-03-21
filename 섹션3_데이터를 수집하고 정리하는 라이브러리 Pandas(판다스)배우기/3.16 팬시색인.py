# 넘파이 모듈을 포함한 종합실습 - 팬시 색인
import pandas as pd
import numpy as np


# 다차원 배열 색인
ar = np.arange(1,26).reshape(5,5)
print(ar)

# 팬시 색인 --> 배열(리스트)을 색인에 사용
print(ar[0]) # [1 2 3 4 5] 
print(ar[0].ndim) # 1차원으로 반환
print(ar[[0]]) # [[1 2 3 4 5]] 이게 팬시 색인이다. 2차원으로 반환
print(ar[[0]].ndim) # 2차원으로 반환
# 똑같은거 같은데 왜 이렇게 해줄까
# 정수 인덱스 색인은 하나의 스칼라 값만 반환 해준다.
# 반면, 팬시 검색(색인,배열)은 2차원 배열을 반환한다.
# 즉, 2차원 형상을 유지함
# 기존 배열의 형상을 유지하면서 색인함

# 하나의 스칼라 값 반환 과 배열 변환
print(ar[0,-1]) # 0행의 마지막값을 출력해서 5가 나온다
print(ar[[0,-1]]) # 0행과 마지막행을 출력해준다.
# ar 배열에서 13,14,18,19 색인하시오
print(ar[2:-1,2:-1])

# 팬시 색인시 메모리 공유
# 팬시 색인은 메모리 공유를 하지 않는다.
# 바로 사본을 만듬
# np.may_share_momory() --> False

ar1 = ar[0]
print(ar1)
print(np.may_share_memory(ar,ar1)) # True
# 정수 인덱스 색인의 경우 -->True
# 그럼 팬시 색인은?
ar2 = ar[[0]]
print(ar2)
print(np.may_share_memory(ar,ar2)) # False 팬시는 공유하지 않기 때문에 팬시 색인은 사본을 만들어 메모리 공유를 하지 않는다.


