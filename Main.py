from Backend.CustomeWidget import *
import sys
import json
import random
import ctypes
from Backend import Tools
from Backend.Tools.ProcessText import ReadText
from Backend.Tools.ThemeChange import WidgetsThemeChange


def CheckIsSaved():
    def SavingCheck():

        if textEdit.toPlainText() != savedTexts:
            return False
        return True

    if not SavingCheck():
        isSaved = False
        savedLabel.show()
    else:
        savedLabel.hide()

def ThemeChange():
    pass

def iconActivated(reason):
    if reason == QSystemTrayIcon.DoubleClick:
        effectWindow.setWindowState(Qt.WindowActive)
        effectWindow.show()

def Close():
    sys.exit(app.exec_())

def Save():
    try:
        data = textEdit.toPlainText()
        global savedTexts
        savedTexts = data
        with open("./Cache/cache.txt", mode="w") as file:
            file.write(data)

        savedLabel.hide()
    except Exception as E:
        print(E)

def Hide():
    effectWindow.showMinimized()

def SaveLabelHide():
    savedLabel.hide()

def SaveLabelShow():
    savedLabel.show()

def TextBold():
    try:
        cursor = textEdit.textCursor()
        if cursor.hasSelection():
            charFormat = cursor.charFormat()
            charFormat.setFontWeight(QFont.Bold)
            cursor.setCharFormat(charFormat)
            textEdit.setTextCursor(cursor)

    except Exception as E:
        print(E)

def SetTextSize(size):
    try:
        cursor = textEdit.textCursor()
        if cursor.hasSelection():
            charFormat = cursor.charFormat()
            charFormat.setFontPointSize(size)
            cursor.setCharFormat(charFormat)
            textEdit.setTextCursor(cursor)

    except Exception as E:
        print(E)

def SetTheme(themeText):
    showIndex = random.randint(0, 1)

    colorFront = colors[themeText][showIndex]
    colorBack = colors[themeText][1-showIndex]

    Tools.WidgetsThemeChange(colorFront, colorBack, textEdit,
                             titleFrame, savedLabel, title,
                             menu)


def SetTextColor():
    colorWindow = MyColorWindow(effectWindow)
    colorWindow.setWindowFlags(Qt.FramelessWindowHint)
    col = colorWindow.getColor(parent=effectWindow).name()

    cursor = textEdit.textCursor()
    if cursor.hasSelection():
        charFormat = cursor.charFormat()
        charFormat.setForeground(QBrush(QColor(col)))
        cursor.setCharFormat(charFormat)
        textEdit.setTextCursor(cursor)

def Default():
    cursor = textEdit.textCursor()
    charFormat = cursor.charFormat()
    charFormat.setFontPointSize(13)
    try:
        charFormat.setForeground(QBrush(QColor(colorFront[0], colorFront[1], colorFront[2])))
    except Exception as E:
        print(E)
    charFormat.setFontWeight(QFont.Normal)
    cursor.setCharFormat(charFormat)
    textEdit.setTextCursor(cursor)


if __name__ == '__main__':
    # pre config
    myappid = "my app"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    colors = {"琥珀黄-青雀头绿": [(249, 180, 0), (21, 60, 70)],
              "太师青-血牙": [(85, 118, 123), (233, 209, 181)],
              "浅云-东方既白": [(234, 236, 241), (139, 163, 199)],
              "珊瑚粉红-蓝莓": [(197, 149, 171), (61, 63, 76)],
              "勃艮第红-米白": [(128, 16, 32), (221, 209, 195)],
              "烈淡紫-灰白": [(81, 56, 88), (226, 218, 216)],
              "冷蓝-脏橘": [(59, 96, 105), (211, 152, 134)]}


    data = ReadText()

    app = QApplication(sys.argv)

    # 获取当前项目路径
    # 路径不对，是因为项目的termernial路径不对

    global isSaved
    global savedTexts
    isSaved = True
    savedTexts = data

    effectWindow = MyWindow()

    effectWindow.setAttribute(Qt.WA_TranslucentBackground)
    effectWindow.setGeometry(1580, 85, 300, 450)
    effectWindow.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    shadow = QGraphicsDropShadowEffect(effectWindow)
    shadow.setOffset(2, 2)
    shadow.setBlurRadius(10)
    shadow.setColor(Qt.gray)

    window = QWidget(effectWindow)
    window.setGeometry(0, 0, 250, 400)
    effectWindow.setWindowIcon(QIcon("./Resources/icon.jpg"))
    window.setGraphicsEffect(shadow)

    trayIcon = QSystemTrayIcon(effectWindow)
    trayIcon.setIcon(QIcon("./Resources/icon.jpg"))
    trayIcon.setToolTip("lp的便利贴")
    trayIcon.activated.connect(iconActivated)
    trayIcon.show()
    # window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


    """
    
    """
    keysList = list(colors.keys())
    maxIndex = len(keysList)
    countIndex = random.randint(0, maxIndex - 1)

    showIndex = random.randint(0, 1)

    colorFront = colors[keysList[countIndex]][showIndex]
    colorBack = colors[keysList[countIndex]][1-showIndex]

    layout = QVBoxLayout(window)

    titleFrame = QFrame(window)
    titleFrame.setMinimumHeight(40)


    savedLabel = QLabel(titleFrame)

    textEdit = QTextEdit(window)
    textEdit.textChanged.connect(CheckIsSaved)
    textEdit.setPlainText(data)


    layout.addWidget(titleFrame)
    layout.addWidget(textEdit)

    layout.setStretch(0, 2)
    layout.setStretch(1, 28)

    layout.setContentsMargins(0, 0, 0, 0)

    titleLayout = QHBoxLayout(titleFrame)


    savedLabel.setGeometry(15, 15, 10, 10)
    savedLabel.setText("*")

    savedLabel.hide()

    title = QPushButton(titleFrame)
    title.setText("lp的便利贴")


    menu = QMenu()

    ActionSave = QAction("save")
    ActionSave.setShortcut('Ctrl+S')

    ActionHide = QAction("hide")
    ActionHide.setShortcut('Ctrl+H')

    ActionTextDefault = QAction("default")
    ActionTextDefault.setShortcut('Ctrl+D')

    ActionTextColor = QAction("Color")
    ActionTextBold = QAction("Bold")
    ActionClose = QAction("close")
    ActionClose.setShortcut('Ctrl+G')

    MenuTextEnlarge = menu.addMenu("font size")
    MenuThemeChange = menu.addMenu("theme change")

    ActionSave.triggered.connect(Save)
    ActionHide.triggered.connect(Hide)
    ActionTextDefault.triggered.connect(Default)
    ActionTextColor.triggered.connect(SetTextColor)
    ActionTextBold.triggered.connect(TextBold)

    FontSize01 = QAction("12px")
    FontSize02 = QAction("24px")
    FontSize03 = QAction("36px")
    FontSize04 = QAction("48px")
    FontSize05 = QAction("60px")
    FontSize06 = QAction("72px")
    FontSize07 = QAction("10px")
    FontSize08 = QAction("8px")
    MenuTextEnlarge.addAction(FontSize08)
    MenuTextEnlarge.addAction(FontSize07)
    MenuTextEnlarge.addAction(FontSize01)
    MenuTextEnlarge.addAction(FontSize02)
    MenuTextEnlarge.addAction(FontSize03)
    MenuTextEnlarge.addAction(FontSize04)
    MenuTextEnlarge.addAction(FontSize05)
    MenuTextEnlarge.addAction(FontSize06)

    FontSize01.triggered.connect(lambda: SetTextSize(12))
    FontSize02.triggered.connect(lambda: SetTextSize(24))
    FontSize03.triggered.connect(lambda: SetTextSize(36))
    FontSize04.triggered.connect(lambda: SetTextSize(48))
    FontSize05.triggered.connect(lambda: SetTextSize(60))
    FontSize06.triggered.connect(lambda: SetTextSize(72))
    FontSize07.triggered.connect(lambda: SetTextSize(10))
    FontSize08.triggered.connect(lambda: SetTextSize(8))

    Theme01 = QAction("琥珀黄-青雀头绿")
    Theme02 = QAction("太师青-血牙")
    Theme03 = QAction("浅云-东方既白")
    Theme04 = QAction("珊瑚粉红-蓝莓")
    Theme05 = QAction("勃艮第红-米白")
    Theme06 = QAction("烈淡紫-灰白")
    Theme07 = QAction("冷蓝-脏橘")
    MenuThemeChange.addAction(Theme01)
    MenuThemeChange.addAction(Theme02)
    MenuThemeChange.addAction(Theme03)
    MenuThemeChange.addAction(Theme04)
    MenuThemeChange.addAction(Theme05)
    MenuThemeChange.addAction(Theme06)
    MenuThemeChange.addAction(Theme07)

    Theme01.triggered.connect(lambda: SetTheme("琥珀黄-青雀头绿"))
    Theme02.triggered.connect(lambda: SetTheme("太师青-血牙"))
    Theme03.triggered.connect(lambda: SetTheme("浅云-东方既白"))
    Theme04.triggered.connect(lambda: SetTheme("珊瑚粉红-蓝莓"))
    Theme05.triggered.connect(lambda: SetTheme("勃艮第红-米白"))
    Theme06.triggered.connect(lambda: SetTheme("烈淡紫-灰白"))
    Theme07.triggered.connect(lambda: SetTheme("冷蓝-脏橘"))

    ActionClose.triggered.connect(Close)

    # title.setContextMenuPolicy(Qt.ActionsContextMenu)
    title.setMenu(menu)

    menu.addAction(ActionSave)
    menu.addAction(ActionHide)
    menu.addAction(ActionTextDefault)
    menu.addAction(ActionTextColor)
    menu.addAction(ActionTextBold)
    menu.addAction(ActionClose)


    titleLayout.addWidget(title)
    titleLayout.setAlignment(Qt.AlignCenter)
    titleLayout.setContentsMargins(0, 0, 0, 0)

    WidgetsThemeChange(colorFront, colorBack, textEdit,
                             titleFrame, savedLabel, title,
                             menu)

    effectWindow.show()
    window.show()

    sys.exit(app.exec_())