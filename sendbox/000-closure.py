import time

# 함수의 실행 시간을 측정하는 코드 : without using decorator
# def myfunc():
#     start=time.time()
#     print("함수 실행")
#     end=time.time()
#     print("실행 시간 : %f 초" % (end-start))

# myfunc()

# 함수의 실행 시간을 측정하는 코드 : using decorator(클로저)
def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print("실행 시간 : %f 초" % (end-start))

        return result

    return wrapper  

# 어노테이션을 이용해 아래를 대체할 수 있다.
# decorated_func=timer(func)
# decorated_func()

@timer
def func(msg): # 매개변수 추가
    print("함수 실행: %s" % msg)

func("Hello, World!")
