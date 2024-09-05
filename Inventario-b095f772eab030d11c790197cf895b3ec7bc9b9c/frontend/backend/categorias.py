from banco_de_dados import connectios


def criar_categoria(nome):
    cnx = connectios()
    cursor = cnx.cursor()
    cursor.execute('insert into category(name_category) value(%s)',(nome,))
    cnx.commit()
    cnx.close()
    print('tudo deu certo categoria')
criar_categoria('bolos')

