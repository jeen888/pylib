# 파일과 디렉토리를 비교할 때는 filecmp 모듈을 사용한다. dircmp 클래스는 두 디렉토리를 비교하여 공통된 파일과 서로 다른 파일을 구분해준다.
import filecmp

# fd = filecmp.dircmp('a', 'b')
fd = filecmp.dircmp('./', './archive')

for a in fd.left_only:
    print("a: %s" % a)

for b in fd.right_only:
    print("b: %s" % b)

for x in fd.diff_files:
    print("x: %s" % x)
