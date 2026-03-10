from collections import namedtuple

data=[
    ('홍길동', 20, '01012345678'),
    ('김철수', 30, '01098765432'),
    ('박영희', 25, '01055555555')
]
Employee=namedtuple('Employee', ['name', 'age', 'phone'])
employees=[Employee(*d) for d in data]
for emp in employees:
    print(emp.name, emp.age, emp.phone)