import time

l=[1,2,3];

# for a in l:
#     print(a)

# iterator
# il=iter(l);
# for i in il: # next 자동으로 호출, but 재호출 불가
#     print(i)

# generator : iterator를 생성하는 함수, yield 키워드 사용, 연속된 값을 차례대로 반환
def mygen():
    yield 1
    yield 2
    yield 3

# for i in mygen():
#     print(i)

# g=mygen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration 예외 발생, generator는 더 이상 반환할 값이 없음을 알리는 예외

# with open('../README.md') as f:
#     for line in f:
#         print(line.strip())

def longtime_job():
    print("작업 시작")
    time.sleep(1)
    print("작업 완료")

    return "done"

# 전부 실행
# list_job=iter([longtime_job() for i in range(5)])
# print(next(list_job))

# lazy evaluation : generator expression, 필요할 때마다 값을 생성, 메모리 효율적
# list_job=(longtime_job() for i in range(5))
# print(next(list_job))
# print(next(list_job))
