# Numpy_eye - 단위행렬(identity matrix)
# 좌측 위에서 우측 아래로 대각선 방향으로 요소가 1
# 주대각선의 원소가 모두 1
# 다른 요소들은 0
# 정사각형 행렬

import numpy as np

# 1차 단위행렬
arr = np.eye(1)
print(arr)

# 2차 단위행렬
arr = np.eye(2)
print(arr)

# 3차 단위행렬
arr = np.eye(3)
print(arr)

# Numpy_ 단위행렬의 성질
# 표기 - E
# 어떤 행렬 A와 단위행렬 E를 곱하면(EA) 자기 자신(A) 나옴
# 차원이 같음