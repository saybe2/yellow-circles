import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, d in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(QPointF(x, y), d/2, d/2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
