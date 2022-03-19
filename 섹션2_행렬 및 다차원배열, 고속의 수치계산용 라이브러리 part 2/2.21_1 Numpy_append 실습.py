# Numpy_Append() axis=0,1
import numpy as np

# 파이썬 방식 배열 append
a = [] # 빈 배열에서
a.append([1])
print(a) # [[1]] -> ([])를 쳐서 출력하면 리스트(list)형식이다. 
a.append(2)
print(a) # [[1], 2] 괄호와 중괄호의 차이를 알아야 한다. -> ()괄호만 입력하면 인트(int)형식이다.

b = []
b.append([1,2,3,4,5])
b.append([6,7,8,9,10])
print(b) # 2차원 배열이 될수있다.
print(b[0])


# 넘파이 방식 배열 append
c = np.array([])
c = np.append(c,[1,2])
print(c)
c = np.append(c,np.array([3,4])) # 이렇게 append 함수를 사용할수도 있다.
print(c)

# empty 함수 -> 값을 초기화 하지 않고 출력되기 때문에 자주 사용된다.
u = np.empty((5,5))
print(u)
print(u.shape)
print(u.dtype)

z = np.empty((4,4), dtype=int)
print(z)

z1 = np.empty_like(z, dtype=int) # 위 z와 동일한 형식으로 출력할수 있다
print(z1)

ar = np.ones((5,5), int)
print(ar)

ar = np.append(ar,[[3,4,5,6,7]], axis=0) #  axis=0는 행추가 할때
print(ar)
print(ar.shape)

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # (2,5)
addcol = np.zeros((2,1), dtype=int) #(2,1) 형태의 제로
print(np.append(arr1, addcol, axis = 1)) #  axis=1는 열추가 할때



