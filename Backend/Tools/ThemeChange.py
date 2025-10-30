


def WidgetsThemeChange(colorFront, colorBack, textEdit,
                       titleFrame, savedLabel, title,
                       menu):
    textEdit.setStyleSheet("""
        QWidget {
        font-family: "微软雅黑";
        font-size: 22px;
        color: rgb""" + str(colorFront) + """;
        background-color: rgb""" + str(colorBack) + """;
        }
        QScrollBar{ background: white; width:5px}
        QScrollBar::handle:vertical{ background-color: #86dbcb; min-height: 60px ;width:30px }
        """)

    titleFrame.setStyleSheet(f"""
        background-color: rgb{colorFront}
        """)

    savedLabel.setStyleSheet("""
        QLabel{
        font-family: "微软雅黑";
        color: rgb""" + str(colorBack) + """
        }
        """)

    title.setStyleSheet("""
        QWidget{
        font-family: "微软雅黑";
        font-size: 20px;
        font-weight: bold;
        border: None;
        color: rgb""" + str(colorBack) + """
        }
        """)

    menu.setStyleSheet("""
        QMenu{
        font-family: "微软雅黑";
        font-size: 20px;
        font-weight: bold;
        border: None;
        color: rgb""" + str(colorBack) + """;
        background-color: rgb""" + str(colorFront) + """
        }
        QMenu::item:selected{color: rgb""" + str(colorFront) + """;
        background-color: rgb""" + str(colorBack) + """}
        """)