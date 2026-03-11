import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)  # 1~45 사이의 숫자중 임의의 숫자 생성
    result.append(num)

print(result)  # 무작위 생성된 6개의 숫자 출력
random.shuffle(result)  # result 리스트의 요소들을 무작위로 섞음
print(result)  # 섞인 result 리스트 출력
print(random.choice(result))  # result 리스트에서 무작위로 하나의 요소를 선택하여 출력