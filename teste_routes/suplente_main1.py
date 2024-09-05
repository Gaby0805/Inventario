import flet as ft
from flet_route import Basket, Params


def page_inicial(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/",
        controls=[
            ft.Text('vai se fuder'),
            ft.ElevatedButton('clique aqui', on_click= lambda _: page.go("/sexo/"))


        ]
            )