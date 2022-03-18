# Numpy_3D array 인덱싱 - 3차원 배열 생성
import numpy as np

# 3차원 배열이다.
a = np.arange(27).reshape(3,3,3)
print(a)
print(a[0]) # 3차원의 첫번째 행이 출력된다.[[0 1 2],[3 4 5],[6 7 8]]
print(a[0,2]) # [6 7 8]

# 8만 출력되게 해보자
print(a[0,2,2])

# 3차원 배열 슬라이싱
# 24,25 출력
print(a[2,2,:2])