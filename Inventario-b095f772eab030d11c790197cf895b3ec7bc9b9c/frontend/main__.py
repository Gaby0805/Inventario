#voce tem que criar o produtos


import flet as ft
from flet_route import Routing, path
from login_view import login_view__
from protuts_view import produtos_view

def main(page: ft.Page):
    try:
        app_routes= [
            path(
                url='/',
                clear=True,
                view=login_view__
            ),
            path(
                url='/produtos/',
                clear=False,
                view=produtos_view
            )
    
        ]

    except SyntaxError as e:
        print(f'ERRO AQUI SEU TROUXA {e}')

    Routing(page=page,app_routes=app_routes)
    page.go(page.route)
ft.app(target=main)