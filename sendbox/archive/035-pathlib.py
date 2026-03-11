# 전통적 방식
# import glob
# import os
import shutil
# 
# for file_path in glob.glob('%s/*.py' % os.getcwd()):
#     parent = os.path.dirname(file_path)
#     filename = os.path.basename(file_path)
#     new_path = os.path.join(parent, 'archive', filename)
#     # shutil.move(file_path, new_path)
#     shutil.copy(file_path, new_path)
# 
import pathlib

for p in pathlib.Path.cwd().glob('*.py'):
    new_p = p.parent.joinpath('archive', p.name)
    # p.replace(new_p)
    shutil.copy(p, new_p)
