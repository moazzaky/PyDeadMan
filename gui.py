from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


import pyAesCrypt, shutil, os, subprocess, time
from getpass import getpass
from utils import compress, shred, encrypt

PASSWORD = 'moaz'

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()


top_button = QPushButton('Select a directory')
bottom_button = QPushButton('Start')
label = QLabel('Hello')
label.setAlignment(Qt.AlignCenter)


layout.addWidget(label, alignment=Qt.AlignVCenter)
layout.addWidget(top_button, alignment=Qt.AlignVCenter)
layout.addWidget(bottom_button, alignment=Qt.AlignVCenter)



def top_click():
    global folder
    folder = str(QFileDialog.getExistingDirectory(window, "select Directory"))
    alert = QMessageBox()
    alert.setText('you selected {}'.format(folder))
    alert.exec_()
top_button.clicked.connect(top_click)

def start():
    compress(folder)
    shred(folder)
    encrypt(PASSWORD)
bottom_button.clicked.connect(start)





window.setLayout(layout)
window.show()

app.exec()