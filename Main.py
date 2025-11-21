import sys
import ctypes
from Backend.CustomeWidget import *
from Backend.Tools.ProcessText import ReadText
from Backend.Surfaces.MainSurface import MainSurface
from Backend.Tools.Init import InitLocalFiles, InitColors



if __name__ == '__main__':
    myappid = "lps app"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    isSaved = True
    InitLocalFiles()
    colorFront, colorBack = InitColors()
    savedTexts = ReadText()

    app = QApplication(sys.argv)
    mainSurface = MainSurface(app, colorFront, colorBack)

    sys.exit(app.exec_())