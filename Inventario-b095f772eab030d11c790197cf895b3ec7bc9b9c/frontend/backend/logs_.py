from banco_de_dados import connectios

def logs(texto):
    try:
        cnx = connectios()
        cursor = cnx.cursor()
        cursor.execute('insert into logs_geral(logs_text)  values (%s)', (texto,))
        cnx.commit()
        print('add aos logs')
        cnx.close()
    except NameError as e:
        lgs(e)
#     CREATE TABLE logs_geral(
#     id_logs int PRIMARY KEY,
#     logs_text LONGTEXT
# )
def listar_logs():
    cnx = connectios()
    cursor = cnx.cursor()
    cursor.execute('select * from logs_geral')
    result = cursor.fetchall()
    return result