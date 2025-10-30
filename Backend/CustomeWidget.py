from PyQt5.Qt import *
from PyQt5.QtCore import Qt, pyqtSignal


class MyWindow(QWidget):
    clicked = pyqtSignal()


    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.drag:
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if self.drag and event.button() == Qt.LeftButton:
            self.drag = False


class MyQLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                            QWidget{
                            font-family: "微软雅黑";}
                            """)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()


class MyColorWindow(QColorDialog):
    def __init__(self, parent=None):
        super(MyColorWindow, self).__init__(parent)

    def closeEvent(self, a0):
        self.hide()




