#!/usr/bin/env python3

import sys

from PyQt5 import QtTest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from qtwidgets import PasswordEdit
from utils import compress, shred, encrypt, decrypt

__version__ = '0.1'
__author__ = 'Moaz Zaky'


# Create a subclass of QMainWindow to setup the GUI
class PyDead(QMainWindow):
    def __init__(self):
        super().__init__()
        self.directory = ''
        self.layout = QVBoxLayout()
        # Set some main window's properties
        self.setWindowTitle('PyDead')
        self.setFixedSize(600, 350)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.encrypt_UI_components()
        self.decrypt_UI_components()

    def encrypt_UI_components(self):
        """Create and add the encryption UI components to the layout"""
        label_1 = QLabel('Choose a directory to be encrypted then shredded: ')
        label_1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        label_1.setAlignment(Qt.AlignCenter)
        self.directory_button = QPushButton('Choose a directory')
        self.directory_button.clicked.connect(self.get_dir)
        label_2 = QLabel('Enter a strong password: ')
        label_2.setFont(QFont('Arial', 12))
        self.password = PasswordEdit()
        start_button = QPushButton('Start encrypting')
        start_button.clicked.connect(self.start_encrypting)

        self.layout.addWidget(label_1, alignment=Qt.AlignVCenter)
        self.layout.addWidget(self.directory_button, alignment=Qt.AlignVCenter)
        self.layout.addWidget(label_2, alignment=Qt.AlignVCenter)
        self.layout.addWidget(self.password)
        self.layout.addWidget(start_button, alignment=Qt.AlignVCenter)

        self.centralWidget.setLayout(self.layout)

    def decrypt_UI_components(self):
        """Create and add the decryption UI components to the layout"""
        line = QLabel('='*250)
        line.setFont(QFont('Arial', 14, weight=QFont.Bold))
        line.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(line)

        decrypt_label = QLabel('Or Choose a file to decrypt: ')
        decrypt_label.setFont(QFont('Arial', 14, weight=QFont.Bold))
        decrypt_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(decrypt_label)




        self.file_button = QPushButton('Choose a file')
        self.file_button.clicked.connect(self.get_file)
        self.layout.addWidget(self.file_button)

        self.decryption_password = PasswordEdit()
        self.layout.addWidget(self.decryption_password)

        self.decrypt_button = QPushButton('decrypt')
        self.decrypt_button.clicked.connect(self.decrypt)
        self.layout.addWidget(self.decrypt_button)

        # The hide button
        self.hide_button = QPushButton('hide')
        self.hide_button.clicked.connect(self.hide)
        self.layout.addWidget(self.hide_button)

    def get_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Choose a File to Decrypt", "AES files (*.aes)")
        if self.file:
            self.file_button.setText('{}'.format(self.file[0]))

    def get_dir(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "Choose a Directory to Encrypt"))
        if self.directory:
            self.directory_button.setText('{}'.format(self.directory))

    def start_encrypting(self):
        """Check if there are directory and password selected, then clear the password field,
        then compress,shred and encrypt the compressed file"""
        if (self.directory) and (self.password.text()):
            self.captured_encrypt_pass = self.password.text()
            self.password.clear()
            QtTest.QTest.qWait(5 * 1000)
            compress(self.directory)
            shred(self.directory)
            encrypt(self.captured_encrypt_pass)

            alert = QMessageBox()
            alert.setText('Done')
            alert.exec_()
        else:
            alert = QMessageBox()
            alert.setText('Choose a directory and password first')
            alert.exec_()


    def decrypt(self):
        if self.file and self.decryption_password.text():
            print(self.decryption_password.text())
            self.captured_decrypt_pass = self.decryption_password.text()
            self.decryption_password.clear()
            try:
                decrypt(self.captured_decrypt_pass)
            except ValueError:
                print('--> Wrong password')

            alert = QMessageBox()
            alert.setText('Decrypted :)')
            alert.exec_()
        else:
            alert = QMessageBox()
            alert.setText('Choose an AES file and password first please')
            alert.exec_()






# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pydead = QApplication(sys.argv)
    # Instantiate and show the GUI
    view = PyDead()
    view.show()
    # Execute the program's main loop
    sys.exit(pydead.exec_())


if __name__ == '__main__':
    main()
