# Numpy_인덱싱(1) 
import numpy as np

# 기본 인덱싱
ar = np.arange(10)
print(ar[4:7]) # 0 1 2 3 4 5 6 7 8 9중에 4, 5, 6이 출력된다.

# 범위를 지정한 요소들의 값을 한번에 변경.
ar[4:7] = 0
print(ar) # [0 1 2 3 0 0 0 7 8 9]

# [ : ] 
ar[:]
print(ar) # ar[:] = ar 과 같아서 [0 1 2 3 0 0 0 7 8 9] 동일하게 출력된다.


# Numpy_인덱싱(2)
# 2차원 배열 부터는 조금 헷갈린다.
# 1차원 배열과는 달리, 좌우로 행, 열로 분리.
ar25size = np.arange(1,26).reshape(5,5)
print(ar25size)

# 3행(인덱스)만 출력하시오?
print(ar25size[3,:]) # [16 17 18 19 20] 3행이 출력된다.
print(ar25size[3,]) # 아무것도 안써줘도 된다.

# 24를 출력하시오?
print(ar25size[4,3]) 

# 13을 출력하시오?
print(ar25size[2,2])

# 17, 18, 19를 출력하시오
print(ar25size[3,1:4])

# 22,23을 출력하시오
print(ar25size[4,1:3])