import flet as ft
from flet_route import Params,Basket


def clt_view(page:ft.Page, params:Params, basket:Basket):
    
    return ft.View(
        '/clt/',
        controls=[
            ft.Text('voce está no clt')

        ]
    )