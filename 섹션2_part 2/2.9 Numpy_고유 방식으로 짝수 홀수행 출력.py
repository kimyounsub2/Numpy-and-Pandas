#Numpy_고유방식으로 짝수 홀수 출력하기
import numpy as np

# for문을 쓰지 않고 넘파이 고유 방식으로
ar30size = np.arange(1,31).reshape(5,6)
print(ar30size)

# 짝수행 
print(ar30size[::2]) # 0번째 행부터 2칸씩 띄어서 출력하시오 0, 2, 4 행이 출력된다.

print(ar30size[::3]) # 0번째 행에서 3칸 0, 3 행이 출력된다.

print(ar30size[:3:3])

# 홀수행만 출력
print(ar30size[1::2])

