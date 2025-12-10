import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.resize(600, 400)
        MainWindow.setWindowTitle("Random Circles")
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton = QPushButton('Add Circle', self.centralwidget)
        self.pushButton.setGeometry(250, 20, 100, 30)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        d = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        self.circles.append((x, y, d, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, d, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(QPointF(x, y), d / 2, d / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
