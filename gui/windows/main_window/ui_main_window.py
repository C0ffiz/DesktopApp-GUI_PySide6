from qt_core import *

from gui.pages.ui_pages import Ui_application_pages

from gui.widgets.py_push_button import PyPushButton

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        self.central_frame = QFrame()

        #Tela Inicial
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        #Menu da Esquerda
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        #Stack Menu Esquerda
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        #Frame Botões Top
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: white; }")

        #Stack Top Menu
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        #Botões Top Menu
        self.toggle_button = PyPushButton(
            text="Toggle"


        )
        self.btn1 = PyPushButton(
            text="Página Inícial",
            is_active=True
        )
        self.btn2 = PyPushButton(
            text="Página 2"

        )

        #Adicionar Botões
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn1)
        self.left_menu_top_layout.addWidget(self.btn2)

        #Spacer Menu
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #Frame Botões Bottom
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: white; }")

        #Stack Bottom Menu
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        #Botões Bottom Menu
        self.settings_btn = PyPushButton(
            text="Configurações"
        )

        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        #Label Bottom
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        #Adicionar Frames, Spacer, Version
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        #Frame Telas
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        #Stack Telas
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        #Top Frame Description
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        #Label Esquerda Top Frame
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")

        #Spacer Top Frame
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Label Direita Top Frame
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #Adicionar Label Esquerda e Direita, Spacer
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        #Cria Widget Pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;")

        #Instancia Classe da Tela e Chama função da Tela
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_2)

        #Bottom Frame Description
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        #Stack Bottom Frame
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        #Label Esquerda Bottom Frame
        self.bottom_bar_left = QLabel("Exemplo")

        #Spacer Bottom Frame
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Label Direita Bottom Frame
        self.bottom_bar_right = QLabel("| Rodapé")
        self.bottom_bar_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #Adicionar
        self.bottom_bar_layout.addWidget(self.bottom_bar_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_bar_right)

        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)
