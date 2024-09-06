import flet as ft
from sys import path
# from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
from backend.categorias import criar_categoria
from backend.logs_ import logs
def categorias_views(page:ft.Page):

    def on_cliked (e):
        
        try:
            value = text_field.value 
            criar_categoria(value)
        except NameError as e:
            print(e)

    
    
    text_field = ft.TextField(label='nome da categoria')
    submite_button = ft.ElevatedButton('enviar', on_click=on_cliked)
    page.add(text_field, submite_button)
ft.app(target=categorias_views)