import random
import sys
import json
from Backend.Tools.ThemeChange import WidgetsThemeChange
from Backend.CustomeWidget import *
from Backend.Config.Colors import COLORS


class MainSurface:

    def __init__(self, app, colorFront, colorBack, savedTexts):
        self.app = app
        self.colorFront = colorFront
        self.colorBack = colorBack
        self.colors = COLORS
        self.savedTexts = savedTexts

        self.__init_surface()

    def __init_surface(self):
        # region window

        self.effectWindow = QWidget()
        self.effectWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.effectWindow.setGeometry(1580, 85, 260, 410)
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

        self.titleFrame = MyFrame(window)
        self.titleFrame.setMinimumHeight(40)

        self.textEdit = QTextEdit(window)
        from Backend.Tools.ToolsColor2RGB import hex_to_rgb
        for key, value in self.savedTexts.items():
            text = value[0]
            fontSize = value[1]
            fontColor = value[2]
            rgbColor = hex_to_rgb(fontColor)
            self.textEdit.setFontPointSize(fontSize)
            if fontColor != "#000000":
                self.textEdit.setTextColor(QColor(rgbColor[0], rgbColor[1], rgbColor[2]))
            self.textEdit.append(text)
            self.textEdit.setTextColor(QColor(self.colorFront[0], self.colorFront[1], self.colorFront[2]))
        self.textEdit.setFontPointSize(16)

        windowL.addWidget(self.titleFrame)
        windowL.addWidget(self.textEdit)

        windowL.setStretch(0, 2)
        windowL.setStretch(1, 28)

        windowL.setContentsMargins(0, 0, 0, 0)

        # endregion

        # region titleL

        titleL = QHBoxLayout(self.titleFrame)

        self.savedLabel = QLabel(self.titleFrame)
        self.savedLabel.setGeometry(15, 15, 10, 10)
        self.savedLabel.setText("*")
        self.savedLabel.hide()

        self.titleButton = QPushButton(self.titleFrame)
        self.titleButton.setText("lp的便利贴")
        # self.titleButton.setContextMenuPolicy(Qt.ActionsContextMenu)

        titleL.addWidget(self.titleButton)
        titleL.setAlignment(Qt.AlignCenter)
        titleL.setContentsMargins(0, 0, 0, 0)

        # endregion


        # region menu
        self.menu = QMenu()

        self.ActionSave = QAction("save")
        self.ActionSave.setShortcut('Ctrl+S')

        self.ActionHide = QAction("hide")
        self.ActionHide.setShortcut('Ctrl+H')

        self.ActionTextDefault = QAction("default")
        self.ActionTextDefault.setShortcut('Ctrl+D')

        self.ActionTextColor = QAction("Color")
        self.ActionTextBold = QAction("Bold")
        self.ActionClose = QAction("close")
        self.ActionClose.setShortcut('Ctrl+G')
        self.ActionTextEnlarge = QAction("Text Enlarge")
        self.ActionTextEnlarge.setShortcut('Ctrl++')
        self.ActionTextShrink = QAction("Text Shrink")
        self.ActionTextShrink.setShortcut('Ctrl+-')

        self.MenuThemeChange = self.menu.addMenu("theme change")

        self.menu.addAction(self.ActionSave)
        self.menu.addAction(self.ActionHide)
        self.menu.addAction(self.ActionTextDefault)
        self.menu.addAction(self.ActionTextEnlarge)
        self.menu.addAction(self.ActionTextShrink)
        self.menu.addAction(self.ActionTextColor)
        self.menu.addAction(self.ActionTextBold)
        self.menu.addAction(self.ActionClose)

        self.ActionSave.triggered.connect(self.Save)
        self.ActionHide.triggered.connect(self.Hide)
        self.ActionTextDefault.triggered.connect(self.Default)
        self.ActionTextColor.triggered.connect(self.SetTextColor)
        self.ActionTextBold.triggered.connect(self.TextBold)
        self.ActionTextEnlarge.triggered.connect(self.EnlargeTextSize)
        self.ActionTextShrink.triggered.connect(self.ShrinkTextSize)

        self.Theme01 = QAction("琥珀黄-青雀头绿")
        self.Theme02 = QAction("太师青-血牙")
        self.Theme03 = QAction("浅云-东方既白")
        self.Theme04 = QAction("珊瑚粉红-蓝莓")
        self.Theme05 = QAction("勃艮第红-米白")
        self.Theme06 = QAction("烈淡紫-灰白")
        self.Theme07 = QAction("冷蓝-脏橘")
        self.MenuThemeChange.addAction(self.Theme01)
        self.MenuThemeChange.addAction(self.Theme02)
        self.MenuThemeChange.addAction(self.Theme03)
        self.MenuThemeChange.addAction(self.Theme04)
        self.MenuThemeChange.addAction(self.Theme05)
        self.MenuThemeChange.addAction(self.Theme06)
        self.MenuThemeChange.addAction(self.Theme07)

        self.Theme01.triggered.connect(lambda: self.SetTheme("琥珀黄-青雀头绿"))
        self.Theme02.triggered.connect(lambda: self.SetTheme("太师青-血牙"))
        self.Theme03.triggered.connect(lambda: self.SetTheme("浅云-东方既白"))
        self.Theme04.triggered.connect(lambda: self.SetTheme("珊瑚粉红-蓝莓"))
        self.Theme05.triggered.connect(lambda: self.SetTheme("勃艮第红-米白"))
        self.Theme06.triggered.connect(lambda: self.SetTheme("烈淡紫-灰白"))
        self.Theme07.triggered.connect(lambda: self.SetTheme("冷蓝-脏橘"))

        self.ActionClose.triggered.connect(self.Close)

        # endregion

        WidgetsThemeChange(self.colorFront, self.colorBack, self.textEdit,
                           self.titleFrame, self.savedLabel, self.titleButton,
                           self.menu)

        # function bunding
        self.textEdit.textChanged.connect(self.CheckIsSaved)
        self.titleButton.setMenu(self.menu)
        window.show()


    def CheckIsSaved(self):
        def SavingCheck():

            if self.textEdit.toPlainText() != self.savedTexts:
                return False
            return True

        if not SavingCheck():
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
            # texts save
            data = self.textEdit.toPlainText()
            self.savedTexts = data

            # qss save
            toWrite = {}
            toTheme = {}
            allTexts = self.textEdit.document()
            lines = allTexts.blockCount()
            for i in range(lines):
                textLine = allTexts.findBlockByLineNumber(i)
                cursor = self.textEdit.textCursor()
                cursor.setPosition(textLine.position())
                fontSize = cursor.charFormat().font().pointSize()

                fontColor = cursor.charFormat().foreground().color().name()
                textLine = textLine.text()
                toWrite[i] = [textLine, fontSize, fontColor]
            # acquire the theme
            toTheme["frontColor"] = (tuple(self.colorFront))
            toTheme["backColor"] = (tuple(self.colorBack))


            with open("./Backend/Config/SavedData.json", 'w') as f:
                json.dump(toWrite, f)

            with open("./Backend/Config/Theme.json", 'w') as f:
                json.dump(toTheme, f)

            self.savedLabel.hide()
        except Exception as E:
            print(E)

    def Hide(self):
        self.effectWindow.showMinimized()

    def SaveLabelHide(self):
        self.savedLabel.hide()

    def SaveLabelShow(self):
        self.savedLabel.show()

    def TextBold(self):
        try:
            cursor = self.textEdit.textCursor()
            if cursor.hasSelection():
                charFormat = cursor.charFormat()
                charFormat.setFontWeight(QFont.Bold)
                cursor.setCharFormat(charFormat)
                self.textEdit.setTextCursor(cursor)

        except Exception as E:
            print(E)

    def EnlargeTextSize(self):
        try:
            cursor = self.textEdit.textCursor()
            if cursor.hasSelection():
                charFormat = cursor.charFormat()
                size = charFormat.font().pointSize()

                charFormat.setFontPointSize(size + 2)
                cursor.setCharFormat(charFormat)
                self.textEdit.setTextCursor(cursor)

        except Exception as E:
            print(E)

    def ShrinkTextSize(self):
        try:
            cursor = self.textEdit.textCursor()
            if cursor.hasSelection():
                charFormat = cursor.charFormat()
                size = charFormat.font().pointSize()

                charFormat.setFontPointSize(size - 2)
                cursor.setCharFormat(charFormat)
                self.textEdit.setTextCursor(cursor)

        except Exception as E:
            print(E)

    def SetTheme(self, themeText):
        showIndex = random.randint(0, 1)

        self.colorFront = self.colors[themeText][showIndex]
        self.colorBack = self.colors[themeText][1 - showIndex]

        WidgetsThemeChange(self.colorFront, self.colorBack, self.textEdit,
                           self.titleFrame, self.savedLabel, self.titleButton,
                           self.menu)

        self.textEdit.setTextColor(QColor(self.colorFront[0], self.colorFront[1], self.colorFront[2]))

    def SetTextColor(self):
        colorWindow = MyColorWindow(self.effectWindow)
        colorWindow.setWindowFlags(Qt.FramelessWindowHint)
        col = colorWindow.getColor(parent=self.effectWindow).name()

        cursor = self.textEdit.textCursor()
        if cursor.hasSelection():
            charFormat = cursor.charFormat()
            charFormat.setForeground(QBrush(QColor(col)))
            cursor.setCharFormat(charFormat)
            self.textEdit.setTextCursor(cursor)

    def Default(self):
        cursor = self.textEdit.textCursor()
        charFormat = cursor.charFormat()
        charFormat.setFontPointSize(16)
        try:
            charFormat.setForeground(QBrush(QColor(self.colorFront[0], self.colorFront[1], self.colorFront[2])))
        except Exception as E:
            print(E)
        charFormat.setFontWeight(QFont.Normal)
        cursor.setCharFormat(charFormat)
        self.textEdit.setTextCursor(cursor)