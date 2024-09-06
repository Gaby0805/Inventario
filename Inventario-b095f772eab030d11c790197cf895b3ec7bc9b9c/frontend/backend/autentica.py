from banco_de_dados import connectios
import logs_ as lg
class Autenticador():
    def autentfy(gmail_client, password_client):

        try:
            #SELECT  ranking  from clients WHERE gmail="b"

            cnx = connectios()
            cursor = cnx.cursor()
            cursor.execute("select ranking from clients where gmail=%s and password_client=%s",(gmail_client, password_client))
            result = cursor.fetchone()
            #caso encontrar login, retorne que existe
            cnx.close()
            if result:
                print('tudo deu certo autentica')
                return True, result
            #se n, n existe logim
            else:
                print('tudo deu certo aqui atentica')
                return False
            
        except TabError as e:
            lg.logs(e)