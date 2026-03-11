import itertools    # 순서에 따른 로테이션

emp_pool=itertools.cycle(['김은경', '이명자', '이성진'])
print(next(emp_pool)) # '김은경'
print(next(emp_pool)) # '이명자'
print(next(emp_pool)) # '이성진'
print(next(emp_pool)) # '김은경', cycle은 순환하는 반복자이므로 다시 처음으로 돌아감