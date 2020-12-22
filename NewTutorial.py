from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim Tutorial!")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello world!")
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Aqui!")
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())

window()