# 조합

import itertools

# it=itertools.combinations(range(1,46), 6) # 로또, 중복불가, 순서무관
it=itertools.combinations_with_replacement(range(1,46), 6) # 중복허용, 순서무관
l=list(it)
print(len(l))