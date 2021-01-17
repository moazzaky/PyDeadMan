from PyQt5 import QtTest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from qtwidgets import PasswordEdit
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

        self.pushButton_encrypt.clicked.connect(self.start_encrypting)
        self.pushButton_hide.clicked.connect(self.hide)


    def get_folder(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "Choose a Directory to Encrypt"))
        if self.directory:
            self.lineEdit_folder.setText('{}'.format(self.directory))

    def get_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Choose a File to Decrypt", "AES files (*.aes)")
        if self.file:
            self.lineEdit_file.setText('{}'.format(self.file[0]))


    def start_encrypting(self):
        """Check if there are directory and password selected, then clear the password field,
        then compress,shred and encrypt the compressed file"""
        if (self.lineEdit_folder) and (self.lineEdit_pass_encrypt.text()):
            self.captured_encrypt_pass = self.lineEdit_pass_encrypt.text()
            self.lineEdit_pass_encrypt.clear()
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





def main():
    app = QApplication(sys.argv)
    form = PyDeadMan()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()