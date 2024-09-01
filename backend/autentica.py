import banco_de_dados as bd


def autentfy(name_client, password_client):

    try:

        cnx = bd.connectios()
        cursor = cnx.cursor()
        cursor.execute('select * from clients  where gmail_client =%s and password_client=%s',(name_client, password_client))
        result = cursor.fetchone()
        cursor.close()
        #caso encontrar login, retorne que existe
        if result:
            return True
        #se n, n existe logim
        else:
            return False
    except TypeError as e:
        print(f'o error é {e}')

