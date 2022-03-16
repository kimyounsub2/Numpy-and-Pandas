# Numpy_View(1) - [][] 방법으로 색인
import numpy as np

ar30size = np.arange(1,31).reshape(5,6)
print(ar30size)

print(ar30size[0])

print(ar30size[4][4]) # 5행의 5열 출력되어서 29가 찍힌다. 
# 하지만 이러한 방법은 Nuumpy의 방식이 아니고 파이썬의 방식이다

#[][] 파이썬의 방법으로 8,9,10,11,12를 출력하시오
print(ar30size[1][1:])

#[][] 파이썬의 방법으로 27,28,29를 출력하시오
print(ar30size[4][2:5])

# a 변수에 담아서 값을 변경해보시오?
a = ar30size[4][2:5]
print(a) # 27, 28, 29가 출력된다.

a[-1] = 0 # 27, 28, 29중에 29를 0으로 변경
print(a)
print(ar30size) # 전체 출력하면 29만 0으로 출력된다.