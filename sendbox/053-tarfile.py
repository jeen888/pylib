import tarfile

# 여러파일 합치기
# with tarfile.open('mytext.tar', 'w') as mytar: # 단순 압축으로 용량이 줄어들지 않음
with tarfile.open('mytext.tar.bz2', 'w:bz2') as mytar: # bzip2 압축으로 용량이 줄어듬, :gz=*.tar.gz, :xz=*.tar.xz
    mytar.add('a.txt')
    mytar.add('b.txt')
    mytar.add('c.txt')
    mytar.add('saying.txt')

# 여러파일 해제하기
# with tarfile.open('mytext.tar.bz2') as mytar:
#     mytar.extractall()
