import flet as ft
from flet import colors
from flet_route import Params, Basket
from sys import path
# from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
from backend.categorias import criar_categoria
from backend.logs_ import logs
def categorias_views(page:ft.Page,params: Params, basket: Basket ):
    page.title = 'criar categorias'
    page.bgcolor = '#000'
    page.window.height = 700
    page.window.width = 500
    page.window.resizable = False
    page.window.center()
    
    def on_cliked (e):
        
        try:
            value = text_field.value 
            criar_categoria(value)
        except NameError as e:
            print(e)

    
    button_voltar = ft.ElevatedButton('voltar', on_click= lambda _: page.go("/"))
    text_field = ft.TextField(label='nome da categoria', border_color= colors.WHITE, width=450 )
    submite_button = ft.ElevatedButton('enviar', on_click=on_cliked, width=150, color=colors.WHITE)
    return ft.View(
        "/categorias",
        controls=[
        ft.Column(

            controls=[
            ft.Container(padding=110
            ),
            text_field, submite_button,button_voltar],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
        )

        ]
    )

