# Numpy_Broadcasting
import numpy as np

# 브로드캐스팅 기본개념 이해3
# 아래의 결과는 에러가 날까?
a = np.arange(5).reshape(5,1) # 5행이 나오고
b = np.arange(3) # 5열이 나온다.
print(a)
print(b)
print(a+b)
