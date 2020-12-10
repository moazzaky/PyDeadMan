#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from qtwidgets import PasswordEdit
from utils import compress, shred, encrypt

__version__ = '0.1'
__author__ = 'Moaz Zaky'



# Create a subclass of QMainWindow to setup the GUI
class PyDead(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyDead')
        self.setFixedSize(470, 150)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.UiComponents()

        # self.layout = QVBoxLayout()

        # label = QLabel('Choose a directory to be encrypted then shredded')
        # label.setAlignment(Qt.AlignCenter)
        # top_button = QPushButton('Select a directory')
        # top_button.clicked.connect(self.choose_dir)
        # password = PasswordEdit()
        # bottom_button = QPushButton('Start encrypting')
        # bottom_button.clicked.connect(self.start)

        # self.layout.addWidget(label, alignment=Qt.AlignVCenter)
        # self.layout.addWidget(top_button, alignment=Qt.AlignVCenter)
        # self.layout.addWidget(password)
        # self.layout.addWidget(bottom_button, alignment=Qt.AlignVCenter)
        #
        # self.centralWidget.setLayout(self.layout)

        self.directory = ''

    def UiComponents(self):
        self.layout = QVBoxLayout()

        label_1 = QLabel('Choose a directory to be encrypted then shredded: ')
        #label_1.setAlignment(Qt.AlignCenter)
        self.top_button = QPushButton('Select a directory')
        self.top_button.clicked.connect(self.choose_dir)
        label_2 = QLabel('Enter a strong password: ')
        self.password = PasswordEdit()
        start_button = QPushButton('Start encrypting')
        start_button.clicked.connect(self.start)

        self.layout.addWidget(label_1, alignment=Qt.AlignVCenter)
        self.layout.addWidget(self.top_button, alignment=Qt.AlignVCenter)
        self.layout.addWidget(label_2, alignment=Qt.AlignVCenter)
        self.layout.addWidget(self.password)

        self.layout.addWidget(start_button, alignment=Qt.AlignVCenter)

        self.centralWidget.setLayout(self.layout)

    def choose_dir(self):

        self.directory = str(QFileDialog.getExistingDirectory(self, "select Directory"))
        if self.directory:
            # alert = QMessageBox()
            # alert.setText('you selected {}'.format(self.directory))
            # alert.exec_()
            self.top_button.setText('{}'.format(self.directory))


    def start(self):
        compress(self.directory)
        shred(self.directory)
        encrypt(self.password.text())

        alert = QMessageBox()
        alert.setText('Done')
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
