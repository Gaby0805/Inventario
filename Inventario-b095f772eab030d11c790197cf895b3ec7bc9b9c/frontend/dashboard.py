import flet as ft
from flet_route import Params,Basket


def clt_view(page:ft.Page, params:Params, basket:Basket):
    page.title = 'page_view'
    page.window.maximized = True

    return ft.View(
        "/dashboard/clt",
        controls=[
            ft.Row(
                controls=[
                    ft.Text('Dashboard Funcionario CLT')
                ],
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton('produtos', on_click= lambda _: page.go('/produtos')),
                    ft.ElevatedButton('relatorios', on_click= lambda _: page.go('/relatorios')),
                    ft.ElevatedButton('categorias', on_click= lambda _: page.go('/categorias')),
                    ft.ElevatedButton('sair do aplicativo', on_click= lambda _: page.window.close())
                ]


                
            )


        ]
    )