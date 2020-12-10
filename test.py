#!/usr/bin/env python3
import shutil, os, subprocess
from secure_delete import secure_delete

path = '/home/zaky/Videos'
shutil.make_archive('compressed','zip', path)
print('compressed')

# delete the files but not the dir tree
# for root, folders, files in os.walk(path):
#     for file in files:
#         subprocess.call(['shred', '-uz', os.path.join(path, root, file)])

# or use 'rmtree' to delete the files and dirs
shutil.rmtree(path)
