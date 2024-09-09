import mysql.connector
from mysql.connector import errorcode
#criação da connecção banco de dados
def connectios():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='estoque_produtos'
            )
        if cnx.is_connected():
            print('tudo certo')
        else:
            print('tudo errado')
        return cnx    
    except errorcode as e:
        print(e)
    