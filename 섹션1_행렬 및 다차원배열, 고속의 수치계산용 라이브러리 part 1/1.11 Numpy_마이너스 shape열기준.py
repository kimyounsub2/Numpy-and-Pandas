# Numpy_마이너스(-1), shape 열 기준 - shapte(-1, n[정수])

import numpy as np
ar = np.arange(12).reshape(3,4)
print(ar)

ar1 = ar.reshape(-1,1) # 열 기준으로 세로로 내려간다.
print(ar1) # (-1,1) = (12,1) 앞에 -1(행)은 아무런 권한 없이 오직 열의 숫자로 모양이 바뀐다.
ar2 = ar.reshape(-1,2)
print(ar2)