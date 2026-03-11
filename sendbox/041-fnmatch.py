import fnmatch
import os

for filename in os.listdir('.'): # ?, *, [seq], [!seq]
    # if fnmatch.fnmatch(filename, 'a???[0-9].py'):
    if fnmatch.fnmatch(filename, '0[3-4][0-9]*.py'):    # regex: 0[3-4][0-9].*\.py와 다름에 주의
        print(filename)
