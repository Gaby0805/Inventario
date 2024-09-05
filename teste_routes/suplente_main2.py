import flet as ft
from flet_route import Params, Basket


def page_final(page: ft.Page, params: Params, basket: Basket):

    return ft.View(
        "/sexo/",
        controls=[

            ft.Text('se fuder vai ir agr'),
            ft.ElevatedButton('clique aqui, porra', on_click= lambda _: page.go("/"))
        ]
    


    )