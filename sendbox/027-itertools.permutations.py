# 반복 가능 객체 중 r개를 선택한 순열 반환
import itertools
sun=list(itertools.permutations(['1','2','3'], 2))
print(sun) # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')], 1, 2, 3에서 2개를 선택한 순열 반환
for a, b in itertools.permutations(['1','2','3'], 2):
    print(a, b) # 1 2, 1 3, 2 1, 2 3, 3 1, 3 2

print('-' * 50)

# combinations(조합)는 순열과 달리 순서가 중요하지 않다.
sun=list(itertools.combinations(['1','2','3'], 2))
print(sun) # [('1', '2'), ('1', '3'), ('2', '3')], 1, 2, 3에서 2개를 선택한 조합 반환
for a, b in itertools.combinations(['1','2','3'], 2):
    print(a, b) # 1 2, 1 3, 2 3

