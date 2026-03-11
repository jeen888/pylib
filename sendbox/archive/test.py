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
    def wrapper():
        start=time.time()
        result=func()
        end=time.time()
        print("실행 시간 : %f 초" % (end-start))

        return result

    return wrapper  

def func():
    print("함수 실행")

decorated_func=timer(func)
decorated_func()
