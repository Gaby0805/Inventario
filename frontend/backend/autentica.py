from banco_de_dados import connectios

class Autenticador():
    def autentfy(gmail_client, password_client):

        try:

            cnx = connectios()
            cursor = cnx.cursor()
            cursor.execute('select * from clients  where gmail=%s and password_client=%s',(gmail_client, password_client))
            result = cursor.fetchone()
            cursor.close()
            #caso encontrar login, retorne que existe
            if result:
                print('tudo deu certo autentica')
                return True
            #se n, n existe logim
            else:
                print('tudo deu certo aqui atentica')
                return False
        except TabError as e:
            print(f'o error é {e}')
