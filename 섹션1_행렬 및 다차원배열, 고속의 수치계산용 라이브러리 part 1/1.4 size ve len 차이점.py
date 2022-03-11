#1. Numpy_size vs len - size 와 len의 차이점
import numpy as np

# 1차원 배열에서는 size 와 len 함수의 차이가 없어 보이나
arr = np.array(['a','b','c','d','e'])

print(arr.size) # 5가 나온다
print(len(arr)) # 5가 나온다

ndarr = np.array([[1,2,3,5],
                [4,5,6,3],
                [7,8,9,5]])
print(ndarr)
print(ndarr.size) # 총 개수인 9가 나온다, 몇개의 요소가 들어있는지를 반환
print(len(ndarr)) # 중괄호의 숫자인 3이 출력된다. 중첩된 리스트의 경우 바깥리스트를 기준으로 몇개의 요소가 들어 있는지를 체크
print(len(ndarr[0])) # 첫 리스트의 1,2,3의 개수가 출력된다.
