# Numpy_고유인덱싱 방식
import numpy as np

ar30size = np.arange(1,31).reshape(5,6)
print(ar30size)
a = ar30size[4][2:5]
a[-1] = 0 # 27, 28, 29중에 29를 0으로 변경
print(ar30size)

# 예를들어 아래와 같은 방식이 고유 인덱싱 방식이다. 앞에 해왔던것이
print(ar30size[1,1:])

# [1,1:]
# 이러한 접근 방식이 고유 인덱싱 방식이다.
# 그런데 이게 왜? 넘파이 고유 방식일까???
# 파이썬 중첩 리스트에서는 이 방식이 안되기 때문이다.
# 다음장에서 그러한 예를 살펴보자

# 파이썬 중첨 리스트가 아닌 넘파이 배열이면
ar2d_np = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(ar2d_np)
print(ar2d_np[1,1:]) # [ 7  8  9 10]이 출력된다.

# 물론 파이선 방식으로도 가능하다.
print(ar2d_np[1][1:]) # [ 7  8  9 10]이 출력된다.

# 이상으로 파이썬과 넘파이가 지정된 요소에 접근하는 방식이 다르다는 것을 알수 있다.
# 하지만 넘파이 고유 인덱싱 방시이 더 빠르기 때문에 왠만해서는 넘파이 고유 방식을 사용하자