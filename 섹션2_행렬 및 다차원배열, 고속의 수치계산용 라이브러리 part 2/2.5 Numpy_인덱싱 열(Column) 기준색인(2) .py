import numpy as np

# 열(Column) 기준으로 인덱싱
ar25size = np.arange(1,26).reshape(5,5)
print(ar25size)

# 2,3,4,7,8,9 값을 0으로 채우시오?
# 1) 먼저 해당부분만 출력.
print(ar25size[:2,1:-1])
# 2) 그리고 0으로 출력
ar25size[:2,1:-1] = 0
print(ar25size)
