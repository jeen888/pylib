import shelve
# shelve 모듈은 객체를 파일로 저장하거나, 파일에서 객체를 읽어올 때 사용합니다. 딕셔너리를 파일로 저장.

def save(key, value):
    with shelve.open('shelve.dat') as d:
        d[key] = value


def get(key):
    with shelve.open('shelve.dat') as d:
        return d[key]


save('number', [1, 2, 3, 4, 5])
print(get('number'))  # [1, 2, 3, ,4, 5] 출력
