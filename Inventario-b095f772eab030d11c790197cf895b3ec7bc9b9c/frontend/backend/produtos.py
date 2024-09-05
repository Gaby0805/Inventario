import banco_de_dados as bd

def listar_produts():
    cnx = bd.connectios()
    cursor = cnx.cursor()
    cursor.execute("select * from produts")
    result = cursor.fetchal

