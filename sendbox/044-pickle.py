import pickle
# pickle 모듈은 객체를 파일로 저장하거나, 파일에서 객체를 읽어올 때 사용합니다.

def get_all_data():
    try:
        with open("data.p", 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def add_data(no, subject, content):
    data = get_all_data()
    assert no not in data   # 이 문장이 없으면, 기존 데이터가 덮어쓰기 됩니다.
    data[no] = {'no': no, 'subject': subject, 'content': content}
    with open('data.p', 'wb') as f:
        pickle.dump(data, f)


def get_data(no):
    data = get_all_data()
    return data[no]


# 데이터저장
add_data(1, '안녕 피클', '피클은 매우 간단합니다.')

# 데이터조회
data = get_data(1)
print(data['no'])
print(data['subject'])
print(data['content'])
