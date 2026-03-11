import fileinput
import glob

# 여러 개의 파일을 한꺼번에 읽어서 처리할 때는 fileinput 모듈이 편리하다. glob 모듈로 읽어들일 파일을 지정할 수 있다.
with fileinput.input(glob.glob("*.txt")) as f:
    for line in f:
        print(line)
