#!/usr/bin/env python3
import pyAesCrypt, shutil, os, subprocess, time
from getpass import getpass

#path = '/home/zaky/Videos'
#password = getpass("Enter password: ")

#time.sleep(30*60)

# compress to compressed.zip file
def compress(path):
    shutil.make_archive('compressed','zip', path)
    print('compressing is done.')

# Shred all the files
def shred(path):
    for root, folders, files in os.walk(path):
        for file in files:
            subprocess.call(['shred', '-uz', os.path.join(path, root, file)])
    # # then use 'rmtree' to delete the directory tree
    shutil.rmtree(path)

# encryption/decryption buffer size - 64K
def encrypt(password):
    bufferSize = 64 * 1024
    # encrypt
    pyAesCrypt.encryptFile(os.path.join('/home/zaky/PycharmProjects/PyDeadMan/', 'compressed.zip'), "compressed.aes", password, bufferSize)
    print('File encrypted')

    subprocess.run(['shred', '-uz', 'compressed.zip'])

if __name__ == "__main__":
    pass


