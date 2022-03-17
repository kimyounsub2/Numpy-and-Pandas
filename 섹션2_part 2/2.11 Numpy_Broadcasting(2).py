# Numpy_Broadcasting
import numpy as np

# 브로드캐스팅 기본개념 이해1
a = np.ones((4,4))
print(a)
b = np.arange(4) # 0 1 2 3 
print(b)
print(a+b) # 각 열에 0 1 2 3 씩 더해서 출력된다.

# 브로드캐스팅 기본개념 이해2
c = np.arange(5).reshape(5,1) # 5행이 나오고
d = np.arange(5) # 5열이 나온다.
print(c)
print(d)
print(c+d) # 5행과 5열이 더해줘서 5x5 형태로 변형된다.
 # c를 열을 5개 해주고 d행 5개 같이 추가하여 서로 더해준것