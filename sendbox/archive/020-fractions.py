# 유리수 계산

print(1/5 + 2/5) # 0.6000000000000001, 1/5과 2/5의 합

from fractions import Fraction
a=Fraction(1, 5) # Fraction(1, 5)은 1/5을 표현한 객체
b=Fraction('2/5') # 이런 방식도 가능
print(a) # 1/5
print(b) # 2/5
print(a+b) # 3/5, Fraction(1, 5)과 Fraction(2, 5)의 합은 Fraction(3, 5)로 표현됨
print(float(a+b)) # 0.6, Fraction(3, 5)을 float으로 표현하면 0.6이 됨

# 분자
print(a.numerator) # 1, Fraction(1, 5)의 분자는 1
# 분모 
print(a.denominator) # 5, Fraction(1, 5)의 분모는 5

print(type(a.numerator))
print(type(a.denominator))
print(type(a))