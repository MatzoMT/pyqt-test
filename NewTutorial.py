from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(200, 200, 300, 300)
    window.setWindowTitle("Tech With Tim Tutorial!")

    label = QtWidgets.QLabel(window)
    label.setText("Hello world!")
    label.move(50, 50)

    window.show()
    sys.exit(app.exec_())

window()