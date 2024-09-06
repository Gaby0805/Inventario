import flet as ft
from sys import path
from flet_route import Params, Basket
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.produtos as prod
def produtos_view(page: ft.Page):


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
    submite_button = ft.ElevatedButton('enviar', on_click=submite_button_action)

    # return ft.View(
    #     "/sexo/1",
    #     controls=[
    #     category,nome_product,description_product,price_product,quantity_product,submite_button]
    #     )
    page.add(category,nome_product,description_product,price_product,quantity_product, submite_button )



def excluir(page: ft.Page):


    def send(e):
        id_target_value = id_target.value
        prod.delete_produto(id_target_value)
        print('deu tudo certo')
    id_target = ft.TextField(label='id do produto', input_filter=ft.NumbersOnlyInputFilter())
    send_button = ft.ElevatedButton('enviar', on_click=send)
    page.add(id_target,send_button)

def editar(page: ft.Page):
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
    preco = ft.TextField(label='preço')
    quantidade = ft.TextField(label='quantidade')
    id_produto = ft.TextField(label='id do produto a ser mudado')
    category = ft.Dropdown(label='categoria', options=[ft.dropdown.Option(str(i[0]), text=i[1]) for i in listar ])
    submite_button = ft.ElevatedButton('enviar', on_click=send)
    page.add(id_produto,category,nome,descricao,preco,quantidade, submite_button)


ft.app(target=editar)