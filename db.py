from msilib.schema import Error
from multiprocessing import connection
from socket import create_connection




import mysql.connector
from mysql.connector import errorcode

class Mysql:
    def __init__(self):
    

        def mysql(self):
 
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

