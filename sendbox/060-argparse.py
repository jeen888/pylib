import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자') # *, +, ?, {n}, {n,}, {n,m} 중 하나를 사용할 수 있다. nargs='*'는 0개 이상의 인자를 받는다. nargs='+'는 1개 이상의 인자를 받는다. nargs='?'는 0개 또는 1개의 인자를 받는다. nargs='{n}'는 n개의 인자를 받는다. nargs='{n,}'는 n개 이상의 인자를 받는다. nargs='{n,m}'는 n개 이상 m개 이하의 인자를 받는다.
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("합은 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("곱은 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))

# $ python 060-argparse.py -a 1 2 3 -m 4 5