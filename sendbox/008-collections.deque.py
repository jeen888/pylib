from collections import deque

a=[1,2,3,4,5]
q=deque(a)
q.rotate(2) # 양수면 오른쪽으로, 음수면 왼쪽으로 회전
result=list(q)
print(result)   #[4, 5, 1, 2, 3]