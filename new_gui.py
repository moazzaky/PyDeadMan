from PyQt5 import QtTest
from PyQt5.QtWidgets import *
from qtwidgets import PasswordEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from utils import compress, shred, encrypt, decrypt


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication
import sys
from ui import Ui_MainWindow

class PyDeadMan(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(PyDeadMan, self).__init__(parent)
        self.setupUi(self)
        self.my_UI()

    def my_UI(self):
        self.pushButton_browse_folder.clicked.connect(self.get_folder)
        self.pushButton_browse_file.clicked.connect(self.get_file)

        self.pushButton_encrypt.clicked.connect(self.encrypt)
        self.pushButton_decrypt.clicked.connect(self.decrypt)

        self.pushButton_hide.clicked.connect(self.hide)




    def get_folder(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "Choose a Directory to Encrypt"))
        if self.directory:
            self.lineEdit_folder.setText('{}'.format(self.directory))

    def get_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Choose a File to Decrypt", "AES files (*.aes)")
        if self.file:
            self.lineEdit_file.setText('{}'.format(self.file[0]))


    def encrypt(self):
        """Check if there are folder and password selected, clear the password field,
        then compress,shred and encrypt the compressed file"""
        if (self.lineEdit_folder) and (self.lineEdit_pass_encrypt.text()):
            self.captured_encrypt_pass = self.lineEdit_pass_encrypt.text()
            self.lineEdit_pass_encrypt.clear()

            delay = int(float(self.delay.text()))
            QtTest.QTest.qWait(delay * 1000) # Wait until the delay is over before start encrypting
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
        if self.file and self.lineEdit_pass_decrypt.text():
            self.captured_decrypt_pass = self.lineEdit_pass_decrypt.text()
            self.lineEdit_pass_decrypt.clear()
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




def main():
    app = QApplication(sys.argv)
    form = PyDeadMan()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()