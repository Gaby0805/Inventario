from banco_de_dados import connectios


def logs(log_error):
    cnx = connectios()
    cursor = cnx.cursor()
    cursor.execute('insert into logs_geral(logs_text) values(%s)',(log_error,))
    cnx.commit()
    print('add aos logs')
    cnx.close()
logs('error quando o sistema foi rebola de ladinho para os crias')
