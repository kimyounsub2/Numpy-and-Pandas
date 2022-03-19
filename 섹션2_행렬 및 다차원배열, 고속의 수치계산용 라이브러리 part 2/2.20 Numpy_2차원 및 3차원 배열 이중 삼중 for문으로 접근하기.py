# Numpy_2차원 및 3차원 배열 이중 삼중 for문으로 접근하기
import numpy as np

# 문제) 2차원 배열과 3차원 배열을 각각 arange()로 생성한 후 각 요소들의 값을 for문으로 출력하시오?
# - 이때 2차원 배열의 요소 수는 25개로 하고 3차원 배열의 요소 수는 60개로 한다.

# 2차원
a = np.arange(1,26).reshape(5,5)
print(a)
print(a.ndim)
# 2차원 for문
for x_ in range(0,5):
    for y_ in range(0,5):
        print(a[x_][y_],end = '\t')
    print()
    
    
# 3차원
b = np.arange(1,61).reshape(3,4,5) 
print(b)
print(b.ndim)
# 3차원 for문
for x_ in range(0,3):
    for y_ in range(0,4):
        for z_ in range(0,5):
            print(b[x_][y_][z_], end = '\t')
        print()
    print()