import gzip
# gzip 모듈은 파일을 gzip 형식으로 압축하거나 압축된 파일을 읽을 때 사용한다. 내부적으로 zlib 모듈을 사용하여 데이터를 압축한다.

data = "Life is too short, you need python." * 10000

with gzip.open('data.txt.gz', 'wb') as f:
    f.write(data.encode('utf-8'))

# 저장된 파일을 확인해 보았더니 파일사이즈가 1097 바이트로 표시된다.

with gzip.open('data.txt.gz', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data

print(len(data))  # 350000 출력