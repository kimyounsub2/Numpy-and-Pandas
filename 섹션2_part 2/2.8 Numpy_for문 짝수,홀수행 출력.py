# Numpy_짝수, 홀수행 출력
import numpy as np

# 아래의 배열에서 짝수행만 출력하시오?

ar30size = np.arange(1,31).reshape(5,6)
print(ar30size)

# 먼저 해당 부분만 출력
print(ar30size[ :2,1:4])
# 보통 처음에는 for문을 생각할수 있다
# for문도 가능은 하나 큰 배열은 시간이 많이 걸린다.
# 물론 작은 배열에서는 상관없지만 빅데이터라면 엄청난 시간이 걸릴지도 모른다.

# 먼저 for문을 이용해서 짝수행 출력해보자
for i in range(5): 
    if i % 2 == 0:
            print(ar30size[i])
            
# for i in range(5): 에서 5는 5행으로 수동으로 입력해줬지만 아래처럼 가능하다.
# ar30size.shape[0] 5,6 의 0번째인 5가 출력되고 shape[1] 이면 5,6 의 첫번째인 6이 출력된다.
for i in range(ar30size.shape[0]): 
    if i % 2 == 0:
            print(ar30size[i])
            
# 먼저 for문을 이용해서 짝수열 출력해보자
for i in range(ar30size.shape[0]):
    for j in range(ar30size.shape[1]):
        if j % 2 ==0:
            print(ar30size[i][j],end ='') # 가로로 출력이 되지만 일렬로 출력되게 하기 위해
    print()
 