from msilib.schema import Error
from multiprocessing import connection
from socket import create_connection
import sys
import os
from unittest import result

from qt_core import *

import mysql.connector
from mysql.connector import errorcode

from gui.windows.main_window.ui_main_window import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python e PySide6")
   
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.Refresh_Table()
        

        self.ui.toggle_button.clicked.connect(self.toggle_button)
        self.ui.btn1.clicked.connect(self.show_page_1)   
        self.ui.btn2.clicked.connect(self.show_page_2)     
        #self.ui.btn3.clicked.connect(self.show_page_3)
        self.ui.ui_pages.add_btn.clicked.connect(self.Add_Table)

        self.show()

    def show_page_1(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
    
    def show_page_2(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
    
    # def show_page_3(self):
    #     self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)

    def toggle_button(self):
        #Pegar Largura Menu Esquerdo
        menu_width = self.ui.left_menu.width()

        width = 50
        if menu_width == 50:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def Refresh_Table(self):
        self.ui.ui_pages.refresh_btn.clicked.connect(self.GET_DATA)

    def Add_Table(self):    
        self.ui.ui_pages.add_btn.clicked.connect(self.ADD_DATA)
        print("vaaaaaaaaaai")

    def GET_DATA(self):
        try:    
                con = mysql.connector.connect(
                host= "localhost",
                user= "root",
                password= "tartaruga",
                database= "pythonmysql") 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        cursor=con.cursor()

        cursor.execute("SELECT * FROM clientes")

        result = cursor.fetchall()

        print(result)

        self.ui.ui_pages.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.ui.ui_pages.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.ui_pages.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def ADD_DATA(self):
        try:    
                        con = mysql.connector.connect(
                        host= "localhost",
                        user= "root",
                        password= "tartaruga",
                        database= "pythonmysql") 
        except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Something is wrong with your user name or password")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist")
                    else:
                        print(err)
        print("bancu")
        cursor=con.cursor()

        nome = self.ui.ui_pages.le_nome.text()
        email = self.ui.ui_pages.le_email.text()
        cpf = self.ui.ui_pages.le_cpf.text()
        celular = self.ui.ui_pages.le_celular.text()
        print(nome, email, cpf, celular)
        
        sql = "INSERT INTO clientes (nome, email, cpf, celular) VALUES (%s, %s, %s, %s)"
        val = (nome, email, cpf, celular)
        cursor.execute(sql, val)
        con.commit()
        print("bancu2")
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
