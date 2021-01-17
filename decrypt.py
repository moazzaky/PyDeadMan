#!/usr/bin/env python3

import os, pyAesCrypt
from getpass import getpass

bufferSize = 64 * 1024
password = getpass("Enter password: ")

# decrypt
try:
    pyAesCrypt.decryptFile("compressed.aes", "compressed.zip", password, bufferSize)
except ValueError:
    print('--> Wrong password')





    #     # My Code
    #     self.pushButton_browse_folder.clicked.connect(self.get_folder)
    #     self.pushButton_browse_file.clicked.connect(self.get_file)
    #
