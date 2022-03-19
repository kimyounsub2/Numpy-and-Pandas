import numpy as np

ar25size = np.arange(1,26).reshape(5,5)
print(ar25size)

# 2행만 출력하시오
print(ar25size[2,]) # [11 12 13 14 15] 1차원인 2행의 숫자만 출력되지만
print(ar25size[2:3]) # [[11 12 13 14 15]] 2차원인 2행 전체문구가 출력된다.
print(ar25size[2,].ndim) # 1차원
print(ar25size[2:3].ndim) # 2차원
# 2,3행 두행을 출력하시오?
print(ar25size[2:4])

# 2,3,4행을 출력하시오?
print(ar25size[2:5])
print(ar25size[2:])