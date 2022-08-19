from msilib.schema import Error
from multiprocessing import connection
from pickle import TRUE
from socket import create_connection
import sys
import os
from unittest import result

from qt_core import *
import db
from gui.windows.main_window.ui_main_window import *

from msilib.schema import Error
from multiprocessing import connection
from socket import create_connection
import mysql.connector
from mysql.connector import errorcode

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python e PySide6")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.Refresh_Table()

        # self.ui.ui_pages.delete_btn.hide()
        # self.ui.ui_pages.update_btn.hide()
        # self.ui.ui_pages.le_nome.hide()
        # self.ui.ui_pages.le_nome_label.hide()
        # self.ui.ui_pages.le_cpf.hide()
        # self.ui.ui_pages.le_cpf_label.hide()
        # self.ui.ui_pages.le_email.hide()
        # self.ui.ui_pages.le_email_label.hide()
        # self.ui.ui_pages.le_id.hide()
        # self.ui.ui_pages.le_id_label.hide()
        
  

        self.ui.toggle_button.clicked.connect(self.toggle_button)
        self.ui.btn1.clicked.connect(self.show_page_2)
        # self.ui.btn2.clicked.connect(self.show_page_2)
        # self.ui.btn3.clicked.connect(self.show_page_3)
        self.ui.ui_pages.add_btn.clicked.connect(self.ADD_DATA)
        self.ui.ui_pages.update_btn.clicked.connect(self.UPDATE_DATA)
        self.ui.ui_pages.delete_btn.clicked.connect(self.DELETE_DATA)
        self.ui.ui_pages.buscar_btn.clicked.connect(self.SEARCH_NUMBER)
        self.ui.ui_pages.return_btn.clicked.connect(self.RETURN)
        self.ui.ui_pages.le_celular_3.textChanged.connect(self.TEST)

        self.show()

 

    def TEST(self):
        # var = "(00)00000-0000"
        # pos = self.ui.ui_pages.le_celular_3.cursorPosition() - 1
        # print(pos)
        # self.ui.ui_pages.le_celular_3.setInputMask(var[pos]+var[pos+1]+var[pos+2])
        # self.ui.ui_pages.le_celular_3.setCursorPosition(pos)
        # pos = pos+3
        
        
        

        # if self.ui.ui_pages.le_celular_3.cursorPosition == 1:
        #     self.ui.ui_pages.le_celular_3.setInputMask("(")
        pass

    def show_page_1(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        

    def show_page_2(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        event = self.ui.ui_pages.le_celular_3
        if (event.type() == event.KeyPress):
            print("foi")

    # def show_page_3(self):
    #     self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)

    def toggle_button(self):
        # Pegar Largura Menu Esquerdo
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

    def Update_Table(self):
        self.ui.ui_pages.update_btn.clicked.connect(self.UPDATE_DATA)

    def SEARCH_NUMBER(self):

        celular = self.ui.ui_pages.le_celular_3.text()
        print(celular)
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pythonmysql")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        cursor = con.cursor()

        sql = "SELECT EXISTS(SELECT celular FROM clientes WHERE celular = %s)"
        data = (celular,)

        cursor.execute(sql,data)

        result = cursor.fetchone()[0]

        print("Resultado: ", result)
        print("Type: ",type(result))

        print(result)

        if result == 1:
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
            self.ui.ui_pages.add_btn.hide()
            self.ui.ui_pages.update_btn.show()
            self.ui.ui_pages.delete_btn.show()
            

            # self.celular = 0
            # self.nome = 0
            # self.email = 0
            # self.cpf = 0
            # self.cep = 0
            # self.rua = 0
            # self.bairro = 0
            # self.cidade = 0
            # self.estado = 0
            sql = "SELECT * FROM clientes WHERE celular = %s"
            data = (celular,)
            cursor.execute(sql,data)

            row = cursor.fetchall()

            
            print(type(row))

            print("Deu: ", row[0][0])

            self.ui.ui_pages.le_celular.setText(celular)
            self.ui.ui_pages.le_nome.setText(row[0][1])
            self.ui.ui_pages.le_email.setText(row[0][2])
            self.ui.ui_pages.le_cpf.setText(row[0][3])
            self.ui.ui_pages.le_cep.setText(row[0][4])
            self.ui.ui_pages.le_rua.setText(row[0][5])
            self.ui.ui_pages.le_num.setText(row[0][6])
            self.ui.ui_pages.le_bairro.setText(row[0][7])
            self.ui.ui_pages.le_cidade.setText(row[0][8])
            self.ui.ui_pages.le_estado.setText(row[0][9])
            self.unblock()
          
            
        elif result == 0:
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
            self.ui.ui_pages.update_btn.hide()
            self.ui.ui_pages.delete_btn.hide()
            self.ui.ui_pages.add_btn.show()
            self.ui.ui_pages.le_celular.setText(celular)
            self.ui.ui_pages.le_celular.setReadOnly(True)
            

    def RETURN(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.ui_pages.le_celular.setText("")
        self.ui.ui_pages.le_nome.setText("")
        self.ui.ui_pages.le_email.setText("")
        self.ui.ui_pages.le_cpf.setText("")
        self.ui.ui_pages.le_cep.setText("")
        self.ui.ui_pages.le_rua.setText("")
        self.ui.ui_pages.le_num.setText("")
        self.ui.ui_pages.le_bairro.setText("")
        self.ui.ui_pages.le_cidade.setText("")
        self.ui.ui_pages.le_estado.currentText("AC")

        
        
        self.ui.ui_pages.ve_resposta.setText("Exclusão Realizada")


    def GET_DATA(self):
 
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pythonmysql")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        cursor = con.cursor()

        cursor.execute("SELECT * FROM clientes")

        result = cursor.fetchall()

        print(result)

        self.ui.ui_pages.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.ui.ui_pages.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.ui_pages.table.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

    def ADD_DATA(self):

        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pythonmysql")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        cursor = con.cursor()

        celular = self.ui.ui_pages.le_celular.text()
        nome = self.ui.ui_pages.le_nome.text()
        email = self.ui.ui_pages.le_email.text()
        cpf = self.ui.ui_pages.le_cpf.text()
        cep = self.ui.ui_pages.le_cep.text()
        rua = self.ui.ui_pages.le_rua.text()
        num = self.ui.ui_pages.le_num.text()
        bairro = self.ui.ui_pages.le_bairro.text()
        cidade = self.ui.ui_pages.le_cidade.text()
        estado = self.ui.ui_pages.le_estado.currentText()
        
        print(celular, nome, email, cpf, cep, rua, num, bairro, cidade, estado)

        sql = "INSERT INTO clientes (celular, nome, email, cpf, cep, rua, num, bairro, cidade, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (celular, nome, email, cpf, cep, rua, num, bairro, cidade, estado)
        cursor.execute(sql, val)
        con.commit()
        print("bancu2")

        # self.ui.ui_pages.le_celular.clear()
        # self.ui.ui_pages.le_nome.clear()
        # self.ui.ui_pages.le_email.clear()
        # self.ui.ui_pages.le_cpf.clear()
        # self.ui.ui_pages.le_cep.clear()
        # self.ui.ui_pages.le_rua.clear()
        # self.ui.ui_pages.le_num.clear()
        # self.ui.ui_pages.le_bairro.clear()
        # self.ui.ui_pages.le_cidade.clear()
        
        self.ui.ui_pages.ve_resposta.setText("Cadastro Realizado")

    def SELECT_DATA(self):

        pass

    def UPDATE_DATA(self):
        
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pythonmysql")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        cursor = con.cursor()

        celular = self.ui.ui_pages.le_celular.text()
        nome = self.ui.ui_pages.le_nome.text()
        email = self.ui.ui_pages.le_email.text()
        cpf = self.ui.ui_pages.le_cpf.text()
        cep = self.ui.ui_pages.le_cep.text()
        rua = self.ui.ui_pages.le_rua.text()
        num = self.ui.ui_pages.le_num.text()
        bairro = self.ui.ui_pages.le_bairro.text()
        cidade = self.ui.ui_pages.le_cidade.text()
        estado = self.ui.ui_pages.le_estado.currentText()
        

        
        print(nome, email, cpf, cep, rua, num, bairro, cidade, estado, celular)

        sql = "UPDATE clientes SET nome=%s, email=%s, cpf=%s, cep=%s, rua=%s, num=%s, bairro=%s, cidade=%s, estado=%s WHERE celular = %s" 
        data = (nome, email, cpf, cep, rua, num, bairro, cidade, estado, celular)
        cursor.execute(sql,data)
        con.commit()
        cursor.close()
        con.close()
        
        # self.ui.ui_pages.le_celular.clear()
        # self.ui.ui_pages.le_nome.clear()
        # self.ui.ui_pages.le_email.clear()
        # self.ui.ui_pages.le_cpf.clear()
        # self.ui.ui_pages.le_cep.clear()
        # self.ui.ui_pages.le_rua.clear()
        # self.ui.ui_pages.le_num.clear()
        # self.ui.ui_pages.le_bairro.clear()
        # self.ui.ui_pages.le_cidade.clear()
        self.ui.ui_pages.ve_resposta.setText("Alteração Realizada")

    def DELETE_DATA(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pythonmysql")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        cursor = con.cursor()

        celular = self.ui.ui_pages.le_celular.text()
        
        print(celular)

        sql = "DELETE FROM clientes WHERE celular = %s"
        data = (celular,)
        cursor.execute(sql,data)
        con.commit()
        cursor.close()
        con.close()
        
        # self.ui.ui_pages.le_celular.clear()
        # self.ui.ui_pages.le_nome.clear()
        # self.ui.ui_pages.le_email.clear()
        # self.ui.ui_pages.le_cpf.clear()
        # self.ui.ui_pages.le_cep.clear()
        # self.ui.ui_pages.le_rua.clear()
        # self.ui.ui_pages.le_num.clear()
        # self.ui.ui_pages.le_bairro.clear()
        # self.ui.ui_pages.le_cidade.clear()
    
        self.block()
        self.ui.ui_pages.ve_resposta.setText("Exclusão Realizada")

    def block(self):
        self.ui.ui_pages.le_celular.setReadOnly(True)
        self.ui.ui_pages.le_nome.setReadOnly(True)
        self.ui.ui_pages.le_email.setReadOnly(True)
        self.ui.ui_pages.le_cpf.setReadOnly(True)
        self.ui.ui_pages.le_cep.setReadOnly(True)
        self.ui.ui_pages.le_rua.setReadOnly(True)
        self.ui.ui_pages.le_num.setReadOnly(True)
        self.ui.ui_pages.le_bairro.setReadOnly(True)
        self.ui.ui_pages.le_cidade.setReadOnly(True)
        self.ui.ui_pages.le_estado.setEnabled(False)
        print("bloqueio")

    def unblock(self):
        
        print("desbloqueio")
        self.ui.ui_pages.le_nome.setReadOnly(False)
        self.ui.ui_pages.le_email.setReadOnly(False)
        self.ui.ui_pages.le_cpf.setReadOnly(False)
        self.ui.ui_pages.le_cep.setReadOnly(False)
        self.ui.ui_pages.le_rua.setReadOnly(False)
        self.ui.ui_pages.le_num.setReadOnly(False)
        self.ui.ui_pages.le_bairro.setReadOnly(False)
        self.ui.ui_pages.le_cidade.setReadOnly(False)
        self.ui.ui_pages.le_estado.setEnabled(True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
