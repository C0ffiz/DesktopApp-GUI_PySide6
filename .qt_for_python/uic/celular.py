# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'celular.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(851, 615)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_celular_label = QLabel(self.frame_4)
        self.le_celular_label.setObjectName(u"le_celular_label")
        self.le_celular_label.setMinimumSize(QSize(90, 31))
        self.le_celular_label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.le_celular_label.setFont(font1)
        self.le_celular_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_celular_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.le_celular_label, 0, Qt.AlignRight)

        self.le_celular = QLineEdit(self.frame_4)
        self.le_celular.setObjectName(u"le_celular")
        self.le_celular.setMinimumSize(QSize(400, 31))
        self.le_celular.setMaximumSize(QSize(16777215, 16777215))
        self.le_celular.setAutoFillBackground(False)
        self.le_celular.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Century Gothic\";")
        self.le_celular.setInputMethodHints(Qt.ImhDigitsOnly)
        self.le_celular.setMaxLength(14)

        self.horizontalLayout.addWidget(self.le_celular, 0, Qt.AlignHCenter)

        self.delete_btn_2 = QPushButton(self.frame_4)
        self.delete_btn_2.setObjectName(u"delete_btn_2")
        self.delete_btn_2.setMinimumSize(QSize(128, 41))
        self.delete_btn_2.setMaximumSize(QSize(200, 16777215))
        self.delete_btn_2.setStyleSheet(u"font: 11pt \"Century Gothic\";\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.delete_btn_2, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_2)

        StackedWidget.addWidget(self.page)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Insira um n\u00famero de celular", None))
        self.le_celular_label.setText(QCoreApplication.translate("StackedWidget", u"CELULAR", None))
        self.le_celular.setInputMask(QCoreApplication.translate("StackedWidget", u"(00)00000-0000", None))
        self.le_celular.setPlaceholderText("")
        self.delete_btn_2.setText(QCoreApplication.translate("StackedWidget", u"Buscar", None))
    # retranslateUi

