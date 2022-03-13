# Numpy_마이너스(-1), shape 행 기준 - shapte(n[정수],-1)

import numpy as np

ar = np.arange(12)
ar1 = ar.reshape(1,-1) # 행 기준으로 가로로 출력된다.
print(ar1)

ar2 = ar.reshape(2, -1)
print(ar2)

# reshape(-1) 하나만 입력했을때
ar3 = np.arange(12).reshape(3,4)
ar4 = ar3.reshape(-1) # (1.-1)과 같은 값이 나온다.
print(ar4) 

# reshape(-1,-1)일때
#ar_test = ar.reshape(-1, -1)
# 어느 한쪽의 기준이 없기 때문에 에러가난다. 반드시 행과 열 하나의 기준점이 있어야 한다.

# reshape(6, -2) -1보다 더 크게 입력했을때 
ar_1 = ar.reshape(6, -20) # 출력은 되지만 어떠한 값을 입력해도 -1로 출력된다.
print(ar_1) 

###### 이상을 살펴본봐와 같이
# ar.reshape(-1,n) 또는 ar.reshape(n,-1) 메소드는 주어진 배열의 요소 사이즈와 연관성이 높다.
# 배열에 있는 요소가 재배열 되려는 배열의 모양구조(차원에) 빠짐없이 배분이 되어질수 있는냐 없느냐가 중요한 핵심이다.
# 당연히 제대로 분배가 안되어지는 경우의 모양은 에러가 난다. 
# 예를 들어 12개 배열요소에서 ar.reshape(-1,5) 혹은 ar.reshape(7, -10)로 재멸열 하려면 옐간 난다.
# Reshape(-1)의 경우 (1.-1)과 같은 값이 나온다