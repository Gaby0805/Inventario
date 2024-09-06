from banco_de_dados import connectios
from logs_ import logs 

def criar_categoria(nome):
    try:
        cnx = connectios()
        cursor = cnx.cursor()
        cursor.execute('insert into category(name_category) value(%s)',(nome,))
        cnx.commit()
        cnx.close()
        print('tudo deu certo categoria')
    except NameError as e:
        logs(e)
