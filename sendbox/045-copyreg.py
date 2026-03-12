import pickle
import copyreg

# 객체 읽기, 변경에 따른 오류 방지 copyreg 모듈 사용

# step1. 객체를 파일로 저장하기 위한 함수를 정의한다.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def pickle_student(student):
#     kwargs = student.__dict__
#     return unpickle_student, (kwargs, )

# def unpickle_student(kwargs):
#     return Student(**kwargs)

# copyreg.pickle(Student, pickle_student)   # 객체 생성에 필요한 함수와 인자를 등록한다.

# a=Student('임철희', 27)

# with open('student.p', 'wb') as f:
#     pickle.dump(a, f)

# step2. 객체의 속성을 변경한다. (예시에서는 dummy 속성을 추가한다.)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dummy = 'dummy'  # dummy 속성을 신규로 추가한다!!

def pickle_student(student):
    kwargs = student.__dict__
    return unpickle_student, (kwargs, )

def unpickle_student(kwargs):
    return Student(**kwargs)

copyreg.pickle(Student, pickle_student)

with open('student.p', 'rb') as f:
    student = pickle.load(f)  # unpickle_student 함수가 호출된다.

print(student.dummy)  # 오류가 발생하지 않고 'dummy' 가 출력된다.
