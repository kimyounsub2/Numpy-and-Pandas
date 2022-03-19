import numpy as np

# 열(Column) 기준으로 인덱싱
ar25size = np.arange(1,26).reshape(5,5)
print(ar25size)

# 각 행의 2열 값만 출력하시오? 3, 8, 13, 18, 23
print(ar25size[:,2])
# print(ar25size[,2]) 행처럼 열을 이렇게 입력하면 에러가 난다. 

# 각 행의 4열 값만 출력하시오? [ 5 10 15 20 25]
print(ar25size[:,4]) 

# 열(Column) 기준 역인덱싱
print(ar25size[:,-1])
print(ar25size[:,-2])
print(ar25size[:,-3])

# 3미만인 열(인덱스)의 값을 출력?
# 먼저 배열에서 어떤 부분을 출력하는지 파악해라 열 0 1 2까지만 출력 3미만이니가
print(ar25size[:, :3])

# 3이상인 열(인덱스)의 값을 출력?
print(ar25size[:, 3:])

# 첫번재열과 마지막열을 제외한 가운데 열들만 출력?
print(ar25size[:, 1:4])
print(ar25size[:, 1:-1])
# 먼저 배열에서 어떤 부분을 출력하는지 파악해라
