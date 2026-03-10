from decimal import Decimal
import math 

# 이진수 기반의 파이썬 float연산은 때에 따라 미세한 오차가 발생한다.
print(0.1*3==0.3) # False, 0.1*3은 0.30000000000000004로 표현됨
print(0.1*3) # 0.30000000000000004
print(0.1*3-0.3) # 5.551115123125783e-17, 0.1*3과 0.3의 차이
print(0.1*3-0.3==0) # False, 0.1*3과 0.3의 차이는 0이 아님
print(0.1*3-0.3<1e-10) # True, 0.1*3과 0.3의 차이는 1e-10보다 작음
print(math.isclose(0.1*3, 0.3)) # True, math.isclose()는 0.1*3과 0.3이 가까운지 판단
print('-'*50)

# decimal 모듈을 사용하면 10진수 기반의 float연산이 가능하다.
a=Decimal('0.1')*3 # Decimal('0.1')은 0.1을 10진수로 표현한 객체
b=Decimal('0.3') # Decimal('0.3')은 0.3을 10진수로 표현한 객체
print(a) # Decimal('0.3')
print(b) # Decimal('0.3')
print(a==b) # True, Decimal('0.1')*3과 Decimal('0.3')은 같은 값을 가짐
print(Decimal('1.2')-Decimal('0.1')) # Decimal('0E-28'), Decimal('0.1')*3과 Decimal('0.3')의 차이는 0
print(float(Decimal('1.2')-Decimal('0.1'))) 
print('-'*50)

# decimal은 정수연산은 가능하나, 실수 연산은 불가하다.
try:
    print(Decimal('0.1')*Decimal('0.2')) # Decimal('0.02'), Decimal('0.1')과 Decimal('0.2')의 곱
    print(Decimal('1.1') * 3.0) # TypeError: unsupported operand type(s) for *: 'Decimal' and 'float', Decimal('1.1')과 3.0의 곱
except Exception as e:    print(e) # Decimal('0.1')과 Decimal('0.2')의 곱은 Decimal('0.02')로 표현됨