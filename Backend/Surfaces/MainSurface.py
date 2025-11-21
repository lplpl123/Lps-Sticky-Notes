import random
import sys
from Backend.Tools.ThemeChange import WidgetsThemeChange
from Backend.CustomeWidget import *


class MainSurface():

    def __int__(self, app, colorFront, colorBack):
        self.app = app
        self.colorFront = colorFront
        self.colorBack = colorBack

        self.__init_surface()

    def __init_surface(self):
        # region window

        self.effectWindow = MyWindow()

        self.effectWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.effectWindow.setGeometry(1580, 85, 300, 450)
        self.effectWindow.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.effectWindow.show()

        shadow = QGraphicsDropShadowEffect(self.effectWindow)
        shadow.setOffset(2, 2)
        shadow.setBlurRadius(10)
        shadow.setColor(Qt.gray)

        window = QWidget(self.effectWindow)
        window.setGeometry(0, 0, 250, 400)
        self.effectWindow.setWindowIcon(QIcon("./Resources/icon.jpg"))
        window.setGraphicsEffect(shadow)
        window.show()

        # endregion

        # region trayIcon

        trayIcon = QSystemTrayIcon(self.effectWindow)
        trayIcon.setIcon(QIcon("./Resources/icon.jpg"))
        trayIcon.setToolTip("lp的便利贴")
        trayIcon.activated.connect(self.iconActivated)
        trayIcon.show()

        # endregion

        # region windowL

        windowL = QVBoxLayout(window)

        titleFrame = QFrame(window)
        titleFrame.setMinimumHeight(40)

        self.textEdit = QTextEdit(window)
        self.textEdit.textChanged.connect(self.CheckIsSaved)
        self.textEdit.setPlainText(savedTexts)

        windowL.addWidget(titleFrame)
        windowL.addWidget(self.textEdit)

        windowL.setStretch(0, 2)
        windowL.setStretch(1, 28)

        windowL.setContentsMargins(0, 0, 0, 0)

        # endregion

        # region menu
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

        menu.addAction(ActionSave)
        menu.addAction(ActionHide)
        menu.addAction(ActionTextDefault)
        menu.addAction(ActionTextColor)
        menu.addAction(ActionTextBold)
        menu.addAction(ActionClose)

        ActionSave.triggered.connect(self.Save)
        ActionHide.triggered.connect(self.Hide)
        ActionTextDefault.triggered.connect(self.Default)
        ActionTextColor.triggered.connect(self.SetTextColor)
        ActionTextBold.triggered.connect(self.TextBold)

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

        FontSize01.triggered.connect(lambda: self.SetTextSize(12))
        FontSize02.triggered.connect(lambda: self.SetTextSize(24))
        FontSize03.triggered.connect(lambda: self.SetTextSize(36))
        FontSize04.triggered.connect(lambda: self.SetTextSize(48))
        FontSize05.triggered.connect(lambda: self.SetTextSize(60))
        FontSize06.triggered.connect(lambda: self.SetTextSize(72))
        FontSize07.triggered.connect(lambda: self.SetTextSize(10))
        FontSize08.triggered.connect(lambda: self.SetTextSize(8))

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

        Theme01.triggered.connect(lambda: self.SetTheme("琥珀黄-青雀头绿"))
        Theme02.triggered.connect(lambda: self.SetTheme("太师青-血牙"))
        Theme03.triggered.connect(lambda: self.SetTheme("浅云-东方既白"))
        Theme04.triggered.connect(lambda: self.SetTheme("珊瑚粉红-蓝莓"))
        Theme05.triggered.connect(lambda: self.SetTheme("勃艮第红-米白"))
        Theme06.triggered.connect(lambda: self.SetTheme("烈淡紫-灰白"))
        Theme07.triggered.connect(lambda: self.SetTheme("冷蓝-脏橘"))

        ActionClose.triggered.connect(self.Close)

        # endregion

        # region titleL

        titleL = QHBoxLayout(titleFrame)

        self.savedLabel = QLabel(titleFrame)
        self.savedLabel.setGeometry(15, 15, 10, 10)
        self.savedLabel.setText("*")
        self.savedLabel.hide()

        titleButton = QPushButton(titleFrame)
        titleButton.setText("lp的便利贴")
        # titleButton.setContextMenuPolicy(Qt.ActionsContextMenu)
        titleButton.setMenu(menu)

        titleL.addWidget(titleButton)
        titleL.setAlignment(Qt.AlignCenter)
        titleL.setContentsMargins(0, 0, 0, 0)

        # endregion

        WidgetsThemeChange(self.colorFront, self.colorBack, self.textEdit,
                           titleFrame, self.savedLabel, titleButton,
                           menu)


    def CheckIsSaved(self):
        def SavingCheck():

            if self.textEdit.toPlainText() != savedTexts:
                return False
            return True

        if not SavingCheck():
            isSaved = False
            self.savedLabel.show()
        else:
            self.savedLabel.hide()

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.effectWindow.setWindowState(Qt.WindowActive)
            self.effectWindow.show()

    def Close(self):
        sys.exit(self.app.exec_())

    def Save(self):
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
        colorBack = colors[themeText][1 - showIndex]

        WidgetsThemeChange(colorFront, colorBack, textEdit,
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