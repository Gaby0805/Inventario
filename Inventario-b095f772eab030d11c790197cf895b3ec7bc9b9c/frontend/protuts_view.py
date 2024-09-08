import flet as ft
from sys import path
from flet_route import Params, Basket
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.produtos as prod
import  backend.autentica as aut


def produtos_view(page: ft.Page,params: Params,basket: Basket):
    page.title = 'adicionar produto'
    page.bgcolor = '#000'
    page.window.height = 700
    page.window.width = 500
    page.window.center()



    instancia = aut.Autenticador.lista
    def submite_button_action(e):
        
        nome_produto_value = nome_product.value 
        descricao_value = description_product.value 
        preco_value = price_product.value 
        quantidade_value = quantity_product.value 
        categoria_value = category.value 
        prod.add_produtos(nome_produto_value,preco_value,descricao_value,quantidade_value,categoria_value)

    



    nome_product = ft.TextField(label='nome do produto')
    description_product = ft.TextField(label='descrição do produto')


    #resolver hj
    listar = prod.listar_produts(0)
    category = ft.Dropdown(label='categoria', options=[ft.dropdown.Option(str(i[0]), text=i[1]) for i in listar])
    
    
    
    price_product =ft.TextField(label='preço do produto', input_filter=ft.NumbersOnlyInputFilter())
    quantity_product = ft.TextField(label='quantidade de protudo', input_filter=ft.NumbersOnlyInputFilter() )
    submite_button = ft.ElevatedButton('enviar', on_click=submite_button_action)# ver como direcionar para dashboard desejado se vai ser o clt ou adm
    def qual_pagina(e):
        print(instancia[0])
        if instancia[0] == ('adm',):
            valor_ranking = 'adm'
            page.go(f'/produtos/{valor_ranking}')
            print('tudo certo adm page')
        elif instancia[0] == ('clt',):
            print(instancia[0])
            valor_ranking = 'clt'
            page.go(f'/produtos/{valor_ranking}')
            print('tudo certo, clt page')
        else:
            print('bananiha frita')
            
    return_button = ft.ElevatedButton('voltar ao dashboard', on_click= qual_pagina)
    return ft.View(
        '/produtos',
        controls=[
        category,
        nome_product,
        description_product,
        price_product,
        quantity_product,
        submite_button,
        return_button
            ]
        )







def excluir(page: ft.Page,params:Params, basket: Basket):
    page.title = 'criar excluit'
    page.bgcolor = '#000'
    page.window.height = 700
    page.window.width = 500
    page.window.center()
    page.window.always_on_top = True
    def send(e):
        id_target_value = id_target.value
        prod.delete_produto(id_target_value)
    print('deu tudo certo')
    

    return_button = ft.ElevatedButton('voltar', on_click= lambda _: page.go("/produtos"))    
    id_target = ft.TextField(label='id do produto', input_filter=ft.NumbersOnlyInputFilter())
    send_button = ft.ElevatedButton('enviar', on_click=send)

    return ft.View(
        '/produtos/excluir',
        controls=[
            id_target,
            send_button,
            return_button
        ]


    )

def editar_view(page: ft.Page):
    page.title = 'adicionar produto'
    page.bgcolor = '#000'
    page.window.height = 700
    page.window.width = 500
    page.window.center()
    
    listar = prod.listar_produts(0)
    def send(e):
        nome_value = nome.value 
        descricao_value = descricao.value 
        preco_value = preco.value
        quantidade_value = quantidade.value 
        category_value = category.value
        id_value = id_produto.value
        prod.edit_produtos(nome_value,preco_value,descricao_value,quantidade_value,category_value,id_value)

    nome = ft.TextField(label='nome')
    descricao = ft.TextField(label='descrição')
    preco = ft.TextField(label='preço',input_filter=ft.NumbersOnlyInputFilter())
    quantidade = ft.TextField(label='quantidade',input_filter=ft.NumbersOnlyInputFilter())
    id_produto = ft.TextField(label='id do produto a ser mudado')
    category = ft.Dropdown(label='categoria', options=[ft.dropdown.Option(str(i[0]), text=i[1]) for i in listar ])
    submite_button = ft.ElevatedButton('enviar', on_click=send)
    return_button = ft.ElevatedButton('voltar', on_click= lambda _: page.go("/produtos"))
    return ft.View(
        '/produtos/editar',
        controls=[
            nome,
            descricao,
            preco,
            quantidade,
            id_produto,
            category,
            submite_button,
            return_button
        ]


    )


