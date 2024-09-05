import banco_de_dados as bd

def listar_produts(category:int):
    cnx = bd.connectios()
    cursor = cnx.cursor()
    #ver se a categoria tem algum valor para mostrar resultado
    if category == 0:
        cursor.execute("select * from produtos ")
        print('caso 1')
        #variavel para tratamento de erro
    elif category > 0:
        cursor.execute("select * from produtos where category_id=%s ",(category,))
        print('caso2')
    result = cursor.fetchall()
    cnx.close()
    return result 


def add_produtos(nome,preco,descricao,quantidade,categoria):
    cnx = bd.connectios()
    cursor = cnx.cursor()
    # id_produtos int auto_increment PRIMARY KEY,
    # name_produtos varchar(30) not null,
    # description_produtos varchar(60),
    # price_produtos int not null,
    # quantity_produtos int not null,
    # category_id INT,
    cursor.execute('insert into produtos(name_produtos, description_produtos, price_produtos, quantity_produtos, category_id) values (%s,%s,%s,%s,%s)',(nome,descricao,preco,quantidade,categoria))
    cnx.commit()
    print('tudo deu certo_ enviado para bd')
    cnx.close()

def edit_produtos(nome,preco,descricao,quantidade,categoria,id__):
    cnx = bd.connectios()
    cursor = cnx.cursor()
    cursor.execute('update produtos set name_produtos=%s, description_produtos=%s, price_produtos=%s, quantity_produtos=%s, category_id=%s where id_produtos=%s ',(nome,descricao,preco,quantidade,categoria,id__))
    cnx.commit()
    print('deu tudo certo edit')
    cnx.close()

def delete_produto(id):
    cnx = bd.connectios()
    cursor = cnx.cursor()
    cursor.execute(f'delete from produtos where id_produtos={id}')
    cnx.commit()
    print('item foi deletado')
    cnx.close()