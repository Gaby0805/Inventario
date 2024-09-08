from banco_de_dados import connectios
import logs_ as lg
class Autenticador():
    
    lista =[]
    @classmethod
    def autentfy(cls,gmail_client, password_client):
        try:
            #SELECT  ranking  from clients WHERE gmail="b"
            cnx = connectios()
            cursor = cnx.cursor()
            cursor.execute("select ranking from clients where gmail=%s and password_client=%s",(gmail_client, password_client))
            result = cursor.fetchone()
            #caso encontrar login, retorne que existe
            cnx.close()
            if result:
                print(result)
                print('tudo deu certo autentica')
                cls.lista.append(result)
                print(cls.lista)
                return True, result
            else:
                print(result)
                print('tudo deu errado autentifca')
                return False, result
        except TabError as e:
            lg.logs(e)

        










#tratamento de erro, login 