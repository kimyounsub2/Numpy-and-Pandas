import numpy as np

# 4행만 출력하시오? (다양한 방법으로 출력할수 있다.)
ar25size = np.arange(1,26).reshape(5,5)
print(ar25size)

# 모두 4행만 출력할수 있다.
print(ar25size[4])
print(ar25size[4,])
print(ar25size[4,:])
print(ar25size[-1])
print(ar25size[-1,])
print(ar25size[-1,:])

# 역인덱스
print(ar25size[-1])
print(ar25size[-2])
print(ar25size[-3])