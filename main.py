from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle('Yellow Circles')
        self.place = 0, 0, 0, 0
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(*self.place)
        qp.end()

    def draw(self):
        rad = random.randint(50, 500)
        self.place = random.randint(50, 500), random.randint(50, 500), rad, rad
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())