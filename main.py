import sys
from random import randint, choice
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.run)
        self.flag = False
        self.color = ['yellow', 'black', 'green', 'red']

    def paintEvent(self, e):
        if not self.flag:
            return
        qp = QPainter(self)
        qp.begin(self)
        for _ in range(randint(1, 10)):
            x = randint(0, 300)
            y = randint(0, 300)
            r = randint(10, 100)
            col = choice(self.color)
            qp.setPen(QColor(col))
            qp.setBrush(QColor(col))
            qp.drawEllipse(x, y, r, r)
        qp.end()

    def run(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())