# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(1396, 782)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        StackedWidget.addWidget(self.page_2)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(841, 0))
        self.label.setStyleSheet(u"font: 75 30pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(33, 35, 45)\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")
        self.Cadastro = QWidget()
        self.Cadastro.setObjectName(u"Cadastro")
        self.verticalLayout_3 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(300, 30, 350, 20)
        self.frame_5 = QFrame(self.Cadastro)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(900, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(100, -1, 100, -1)
        self.le_cpf_label = QLabel(self.frame_5)
        self.le_cpf_label.setObjectName(u"le_cpf_label")
        self.le_cpf_label.setMinimumSize(QSize(90, 31))
        self.le_cpf_label.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.le_cpf_label.setFont(font)
        self.le_cpf_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_cpf_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.le_cpf_label)

        self.le_cpf = QLineEdit(self.frame_5)
        self.le_cpf.setObjectName(u"le_cpf")
        self.le_cpf.setMinimumSize(QSize(231, 31))
        self.le_cpf.setMaximumSize(QSize(400, 16777215))
        self.le_cpf.setAutoFillBackground(False)
        self.le_cpf.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_cpf.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_5.addWidget(self.le_cpf)


        self.gridLayout_2.addWidget(self.frame_5, 3, 0, 1, 1)

        self.frame_11 = QFrame(self.Cadastro)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(684, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(128, -1, 0, -1)
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(470, 0))
        self.frame_14.setMaximumSize(QSize(470, 51))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, -1, -1, -1)
        self.le_id_label_3 = QLabel(self.frame_14)
        self.le_id_label_3.setObjectName(u"le_id_label_3")
        self.le_id_label_3.setMinimumSize(QSize(30, 31))
        self.le_id_label_3.setMaximumSize(QSize(50, 16777215))
        self.le_id_label_3.setFont(font)
        self.le_id_label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_id_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.le_id_label_3)

        self.le_rua = QLineEdit(self.frame_14)
        self.le_rua.setObjectName(u"le_rua")
        self.le_rua.setMinimumSize(QSize(231, 31))
        self.le_rua.setMaximumSize(QSize(400, 16777215))
        self.le_rua.setAutoFillBackground(False)
        self.le_rua.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_rua.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_13.addWidget(self.le_rua)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(72, 51))
        self.frame_15.setMaximumSize(QSize(100, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.le_id_label_4 = QLabel(self.frame_15)
        self.le_id_label_4.setObjectName(u"le_id_label_4")
        self.le_id_label_4.setMinimumSize(QSize(30, 31))
        self.le_id_label_4.setMaximumSize(QSize(30, 30))
        self.le_id_label_4.setFont(font)
        self.le_id_label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_id_label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.le_id_label_4)

        self.le_num = QLineEdit(self.frame_15)
        self.le_num.setObjectName(u"le_num")
        self.le_num.setMinimumSize(QSize(40, 31))
        self.le_num.setMaximumSize(QSize(50, 16777215))
        self.le_num.setAutoFillBackground(False)
        self.le_num.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_num.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_14.addWidget(self.le_num)


        self.horizontalLayout_10.addWidget(self.frame_15)


        self.gridLayout_2.addWidget(self.frame_11, 5, 0, 1, 1)

        self.frame_10 = QFrame(self.Cadastro)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(900, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(100, -1, 100, -1)
        self.le_id_label_2 = QLabel(self.frame_10)
        self.le_id_label_2.setObjectName(u"le_id_label_2")
        self.le_id_label_2.setMinimumSize(QSize(90, 31))
        self.le_id_label_2.setMaximumSize(QSize(100, 16777215))
        self.le_id_label_2.setFont(font)
        self.le_id_label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_id_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.le_id_label_2)

        self.le_cep = QLineEdit(self.frame_10)
        self.le_cep.setObjectName(u"le_cep")
        self.le_cep.setMinimumSize(QSize(231, 31))
        self.le_cep.setMaximumSize(QSize(400, 16777215))
        self.le_cep.setAutoFillBackground(False)
        self.le_cep.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_cep.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_9.addWidget(self.le_cep)


        self.gridLayout_2.addWidget(self.frame_10, 4, 0, 1, 1)

        self.frame_12 = QFrame(self.Cadastro)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(900, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(100, -1, 100, -1)
        self.le_id_label_5 = QLabel(self.frame_12)
        self.le_id_label_5.setObjectName(u"le_id_label_5")
        self.le_id_label_5.setMinimumSize(QSize(90, 31))
        self.le_id_label_5.setMaximumSize(QSize(100, 16777215))
        self.le_id_label_5.setFont(font)
        self.le_id_label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_id_label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.le_id_label_5)

        self.le_bairro = QLineEdit(self.frame_12)
        self.le_bairro.setObjectName(u"le_bairro")
        self.le_bairro.setMinimumSize(QSize(231, 31))
        self.le_bairro.setMaximumSize(QSize(400, 16777215))
        self.le_bairro.setAutoFillBackground(False)
        self.le_bairro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_bairro.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_11.addWidget(self.le_bairro)


        self.gridLayout_2.addWidget(self.frame_12, 6, 0, 1, 1)

        self.frame_4 = QFrame(self.Cadastro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(900, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(100, -1, 100, -1)
        self.le_email_label = QLabel(self.frame_4)
        self.le_email_label.setObjectName(u"le_email_label")
        self.le_email_label.setMinimumSize(QSize(90, 31))
        self.le_email_label.setMaximumSize(QSize(100, 16777215))
        self.le_email_label.setFont(font)
        self.le_email_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_email_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.le_email_label)

        self.le_email = QLineEdit(self.frame_4)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(231, 31))
        self.le_email.setMaximumSize(QSize(400, 16777215))
        self.le_email.setAutoFillBackground(False)
        self.le_email.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_email.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_4.addWidget(self.le_email)


        self.gridLayout_2.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.Cadastro)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(900, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, -1, 100, -1)
        self.le_celular_label = QLabel(self.frame_2)
        self.le_celular_label.setObjectName(u"le_celular_label")
        self.le_celular_label.setMinimumSize(QSize(90, 31))
        self.le_celular_label.setMaximumSize(QSize(100, 16777215))
        self.le_celular_label.setFont(font)
        self.le_celular_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_celular_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.le_celular_label)

        self.le_celular = QLineEdit(self.frame_2)
        self.le_celular.setObjectName(u"le_celular")
        self.le_celular.setMinimumSize(QSize(231, 31))
        self.le_celular.setMaximumSize(QSize(400, 16777215))
        self.le_celular.setAutoFillBackground(False)
        self.le_celular.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_celular.setInputMethodHints(Qt.ImhDigitsOnly)
        self.le_celular.setMaxLength(14)

        self.horizontalLayout.addWidget(self.le_celular)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.Cadastro)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 60))
        self.frame_6.setMaximumSize(QSize(700, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(63, -1, 0, -1)
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(470, 0))
        self.frame_16.setMaximumSize(QSize(470, 51))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.le_cpf_label_2 = QLabel(self.frame_16)
        self.le_cpf_label_2.setObjectName(u"le_cpf_label_2")
        self.le_cpf_label_2.setMinimumSize(QSize(90, 31))
        self.le_cpf_label_2.setMaximumSize(QSize(100, 16777215))
        self.le_cpf_label_2.setFont(font)
        self.le_cpf_label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_cpf_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.le_cpf_label_2)

        self.le_cidade = QLineEdit(self.frame_16)
        self.le_cidade.setObjectName(u"le_cidade")
        self.le_cidade.setMinimumSize(QSize(256, 31))
        self.le_cidade.setMaximumSize(QSize(275, 16777215))
        self.le_cidade.setAutoFillBackground(False)
        self.le_cidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_cidade.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_15.addWidget(self.le_cidade)


        self.horizontalLayout_6.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(160, 300))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.le_id_label = QLabel(self.frame_13)
        self.le_id_label.setObjectName(u"le_id_label")
        self.le_id_label.setMinimumSize(QSize(90, 0))
        self.le_id_label.setMaximumSize(QSize(16777215, 16777215))
        self.le_id_label.setFont(font)
        self.le_id_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_id_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.le_id_label)

        self.le_estado = QComboBox(self.frame_13)
        self.le_estado.setObjectName(u"le_estado")
        self.le_estado.setMaximumSize(QSize(50, 16777215))
        self.le_estado.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.le_estado)


        self.horizontalLayout_6.addWidget(self.frame_13)


        self.gridLayout_2.addWidget(self.frame_6, 7, 0, 1, 1)

        self.frame_3 = QFrame(self.Cadastro)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(900, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(100, -1, 100, -1)
        self.le_nome_label = QLabel(self.frame_3)
        self.le_nome_label.setObjectName(u"le_nome_label")
        self.le_nome_label.setMinimumSize(QSize(90, 31))
        self.le_nome_label.setMaximumSize(QSize(100, 16777215))
        self.le_nome_label.setFont(font)
        self.le_nome_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_nome_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.le_nome_label)

        self.le_nome = QLineEdit(self.frame_3)
        self.le_nome.setObjectName(u"le_nome")
        self.le_nome.setMinimumSize(QSize(231, 31))
        self.le_nome.setMaximumSize(QSize(400, 16777215))
        self.le_nome.setAutoFillBackground(False)
        self.le_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_nome.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_3.addWidget(self.le_nome)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(300, -1, 300, 100)
        self.frame_7 = QFrame(self.Cadastro)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(396, 0))
        self.frame_7.setMaximumSize(QSize(800, 200))
        self.frame_7.setLayoutDirection(Qt.LeftToRight)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(100, 0, 100, -1)
        self.add_btn = QPushButton(self.frame_7)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(128, 41))
        self.add_btn.setStyleSheet(u"font: 11pt \"Century Gothic\";\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.add_btn)

        self.update_btn = QPushButton(self.frame_7)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMinimumSize(QSize(128, 41))
        self.update_btn.setStyleSheet(u"font: 11pt \"Century Gothic\";\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.update_btn)

        self.delete_btn = QPushButton(self.frame_7)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(128, 41))
        self.delete_btn.setStyleSheet(u"font: 11pt \"Century Gothic\";\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.delete_btn)


        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.Cadastro, "")
        self.Tabela = QWidget()
        self.Tabela.setObjectName(u"Tabela")
        self.verticalLayout_5 = QVBoxLayout(self.Tabela)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_8 = QFrame(self.Tabela)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 100, -1)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(345, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 16pt \"Century Gothic\";\n"
"color:rgb(255, 255, 255)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.name_filter_txt = QLineEdit(self.frame_8)
        self.name_filter_txt.setObjectName(u"name_filter_txt")
        self.name_filter_txt.setMinimumSize(QSize(0, 31))
        self.name_filter_txt.setMaximumSize(QSize(500, 16777215))
        self.name_filter_txt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.name_filter_txt)

        self.search_btn = QPushButton(self.frame_8)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(131, 41))
        self.search_btn.setMaximumSize(QSize(170, 50))
        self.search_btn.setStyleSheet(u"background-color: rgb(98, 114, 164);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")

        self.horizontalLayout_2.addWidget(self.search_btn)


        self.gridLayout_3.addWidget(self.frame_8, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)

        self.table = QTableWidget(self.Tabela)
        if (self.table.columnCount() < 10):
            self.table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"font: 11pt \"Century Gothic\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.table)

        self.frame_9 = QFrame(self.Tabela)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.refresh_btn = QPushButton(self.frame_9)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setMinimumSize(QSize(151, 51))
        self.refresh_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.refresh_btn)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.tabWidget.addTab(self.Tabela, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        StackedWidget.addWidget(self.page_1)

        self.retranslateUi(StackedWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None))
        self.le_cpf_label.setText(QCoreApplication.translate("StackedWidget", u"CPF", None))
        self.le_id_label_3.setText(QCoreApplication.translate("StackedWidget", u"Rua", None))
        self.le_id_label_4.setText(QCoreApplication.translate("StackedWidget", u"N\u00b0", None))
        self.le_id_label_2.setText(QCoreApplication.translate("StackedWidget", u"CEP", None))
        self.le_id_label_5.setText(QCoreApplication.translate("StackedWidget", u"Bairro", None))
        self.le_email_label.setText(QCoreApplication.translate("StackedWidget", u"EMAIL", None))
        self.le_celular_label.setText(QCoreApplication.translate("StackedWidget", u"CELULAR", None))
        self.le_celular.setInputMask(QCoreApplication.translate("StackedWidget", u"(00)00000-0000", None))
        self.le_celular.setPlaceholderText("")
        self.le_cpf_label_2.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None))
        self.le_id_label.setText(QCoreApplication.translate("StackedWidget", u"Estado", None))
        self.le_nome_label.setText(QCoreApplication.translate("StackedWidget", u"NOME", None))
        self.add_btn.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.update_btn.setText(QCoreApplication.translate("StackedWidget", u"Alterar", None))
        self.delete_btn.setText(QCoreApplication.translate("StackedWidget", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cadastro), QCoreApplication.translate("StackedWidget", u"Cadastro", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Digite um nome para procurar:", None))
        self.search_btn.setText(QCoreApplication.translate("StackedWidget", u"Procurar", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StackedWidget", u"Celular", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StackedWidget", u"Nome", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StackedWidget", u"Email", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StackedWidget", u"CEP", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StackedWidget", u"Rua", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StackedWidget", u"N\u00b0", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("StackedWidget", u"Bairro", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("StackedWidget", u"Estado", None));
        self.refresh_btn.setText(QCoreApplication.translate("StackedWidget", u"Atualizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tabela), QCoreApplication.translate("StackedWidget", u"Tabela", None))
    # retranslateUi

