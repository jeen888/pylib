import lzma
# 압축률 좋으나 속도가 느린 lzma 모듈은 7z 압축 형식에서 사용되는 알고리즘을 구현한 모듈로, 
# 높은 압축률을 제공하지만 압축 및 해제 속도가 느릴 수 있다. 
# 대용량 데이터를 압축할 때 유용하지만, 실시간 처리에는 적합하지 않을 수 있다. 

data = "Life is too short, You need python." * 10000
compress_data = lzma.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 220 출력

org_data = lzma.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

assert data == org_data
