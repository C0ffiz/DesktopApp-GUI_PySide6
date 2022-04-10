import sys
import os

from qt_core import *

from gui.windows.main_window.ui_main_window import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python e PySide6")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
