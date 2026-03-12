import bz2
# zlib와 사용법이 같으나 bz2는 bzip2 알고리즘을 사용하여 데이터를 압축한다. zlib보다 더 높은 압축률을 제공하지만, 압축과 해제 속도가 느리다. 쓰레드 환경에서 안전.

data = "Life is too short, You need python." * 10000
# compress_data = bz2.compress(data.encode(encoding='utf-8'))
# print(len(compress_data))  # 163 출력

# org_data = bz2.decompress(compress_data).decode('utf-8')
# print(len(org_data))  # 350000 출력

# assert data == org_data

# 파일 압축
with bz2.open('data.txt.bz2', 'wb') as f:
    f.write(data.encode('utf-8'))

# 파일 압축 해제
with bz2.open('data.txt.bz2', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data
