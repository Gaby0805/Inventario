import flet as ft
from sys import path
from flet_route import Params, Basket
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')

def produtos_view(page: ft.Page, params:Params, basket: Basket):



    def submite_button_action(e):
        
        pass

    
    nome_product = ft.TextField(label='nome do produto')
    



    description_product = ft.TextField(label='descrição do produto')
    # tem que ajeitar o price_product para aceitar float, tem que ver primeiro nO BD isso
    price_product =ft.TextField(label='preço do produto', input_filter=ft.NumbersOnlyInputFilter())
    quantity_product = ft.TextField(label='quantidade de protudo', input_filter=ft.NumbersOnlyInputFilter() )
    submite_button = ft.ElevatedButton('enviar', on_click=submite_button_action)

    return ft.View(
        "/sexo/1",
        controls=[
        nome_product,description_product,price_product,quantity_product,submite_button]
        )

