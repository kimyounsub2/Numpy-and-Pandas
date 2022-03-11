import numpy as np

ar1 = np.array(['a','b','c','d','e'])
ar2 = np.array([['a','b','c','d','e'],['f','g','h','i','f']])
ar3 = np.array([['a','b','c','d','e'],['f','g','h','i','f'],['1','2','3','4','5']])
print(ar1.shape) # 왜 1 차원에서는 (1,5)가 나오지 않고 (5,)로 출력될까 -> 1차원이기때문에 2차원과 구분하기 위해서
print(ar2.shape) # 2차원 (2,5)
print(ar3.shape) # 2차원 (3,5)

