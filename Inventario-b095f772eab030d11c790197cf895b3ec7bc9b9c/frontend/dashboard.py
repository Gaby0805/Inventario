import flet as ft
from flet_route import Params,Basket


def clt_view(page:ft.Page, params:Params, basket:Basket):
    page.title = 'page_view'


    return ft.View(
        '/dashboard/clt',
        controls=[
            ft.Text('voce está no clt')

        ]
    )


    # falta aleart dialogm e os dashboard
    ''