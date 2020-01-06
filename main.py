import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI


class Main(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        self.flag = False
        self.colours = [QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255),
                        QColor(0, 255, 255), QColor(255, 0, 255)]
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.begin(self)
            self.curc(painter)
            painter.end()
            self.flag = False

    def curc(self, painter):
        for i in range(random.randint(1, 15)):
            self.col = random.choice(self.colours)
            painter.setBrush(self.col)
            painter.setPen(self.col)
            x = random.randint(10, 400)
            y = random.randint(10, 400)
            a = random.randint(10, 100)
            painter.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())