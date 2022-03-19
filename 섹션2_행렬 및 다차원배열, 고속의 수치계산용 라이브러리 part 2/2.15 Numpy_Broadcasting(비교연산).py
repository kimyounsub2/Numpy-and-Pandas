# Numpy_Broadcasting 비교연산 ==,!=
import numpy as np

#(문제) 아래의 벼열들에 대해서 각각의 요소 값을 비교해보시오?

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[1,5,2]]) 
c = np.array([7,8,9])  
d = np.array([7,8]) # a == d는 브로드 캐스팅 자체가안된다.
e = np.array([1,2,3,4]) # a == e는 브로드 캐스팅 자체가 안된다.

# 여기에서는 ==비교했을 때의 결과 값과 != 비교했을 때의 결과 값을 잘 기억하는게 종요하다
print(a==b) # a == b -> [F,F,F],[F,T,F]
print(a==c) # a == c -> [F,F,F],[F,F,F] 

# ==과는 반대로 결과가 나온다.
print(a!=b) # [T,T,T],[T,F,T]
print(a!=c) # [T,T,T],[T,T,T]

# >,< 크냐 작냐도 브로드 캐스팅이 가능하면 결과가 나온다.
print(a>b) # [F,F,F],[T,F,T]
print(a<c) # [T,T,T],[T,T,T]