#!/usr/bin/env python3

import sys

from PyQt5 import QtTest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from qtwidgets import PasswordEdit
from utils import compress, shred, encrypt

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
        self.setFixedSize(600, 270)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.encrypt_UI_components()
        self.decrypt_UI_components()

        # self.layout = QVBoxLayout()

        # label = QLabel('Choose a directory to be encrypted then shredded')
        # label.setAlignment(Qt.AlignCenter)
        # top_button = QPushButton('Select a directory')
        # top_button.clicked.connect(self.get_dir)
        # password = PasswordEdit()
        # bottom_button = QPushButton('Start encrypting')
        # bottom_button.clicked.connect(self.start)

        # self.layout.addWidget(label, alignment=Qt.AlignVCenter)
        # self.layout.addWidget(top_button, alignment=Qt.AlignVCenter)
        # self.layout.addWidget(password)
        # self.layout.addWidget(bottom_button, alignment=Qt.AlignVCenter)
        #
        # self.centralWidget.setLayout(self.layout)



    def encrypt_UI_components(self):


        label_1 = QLabel('Choose a directory to be encrypted then shredded: ')
        label_1.setFont(QFont('Arial', 15))
        #label_1.setAlignment(Qt.AlignCenter)
        self.directory_button = QPushButton('Choose a directory')
        self.directory_button.clicked.connect(self.get_dir)
        label_2 = QLabel('Enter a strong password: ')
        self.password = PasswordEdit()
        start_button = QPushButton('Start encrypting')
        start_button.clicked.connect(self.start)

        self.layout.addWidget(label_1, alignment=Qt.AlignVCenter)
        self.layout.addWidget(self.directory_button, alignment=Qt.AlignVCenter)
        self.layout.addWidget(label_2, alignment=Qt.AlignVCenter)
        self.layout.addWidget(self.password)
        self.layout.addWidget(start_button, alignment=Qt.AlignVCenter)

        self.centralWidget.setLayout(self.layout)

    def decrypt_UI_components(self):
        decrypt_label = QLabel('Or Choose a file to decrypt: ')
        decrypt_label.setFont(QFont('Arial',15))
        self.layout.addWidget(decrypt_label)

        self.file_button = QPushButton('Choose a file')
        self.file_button.clicked.connect(self.get_file)
        self.layout.addWidget(self.file_button)


    def get_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Choose a File to Decrypt", "AES files (*.aes)")
        if self.file:
            self.file_button.setText('{}'.format(self.file[0]))

    def get_dir(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "Choose a Directory to Encrypt"))
        if self.directory:
            self.directory_button.setText('{}'.format(self.directory))


    def start(self):
        if (self.directory) and (self.password.text()):
            self.password.clear()
            QtTest.QTest.qWait(5*1000)
            compress(self.directory)
            shred(self.directory)
            encrypt(self.password.text())

            alert = QMessageBox()
            alert.setText('Done')
            alert.exec_()
        else:
            alert = QMessageBox()
            alert.setText('Choose a directory and password first')
            alert.exec_()







# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pydead = QApplication(sys.argv)
    # Show the GUI
    view = PyDead()
    view.show()
    # Execute the program's main loop
    sys.exit(pydead.exec_())

if __name__ == '__main__':
    main()
