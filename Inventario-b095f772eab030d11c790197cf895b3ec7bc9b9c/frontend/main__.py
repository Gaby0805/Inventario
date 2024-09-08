#voce tem que criar o produtos


import flet as ft
from flet_route import Routing, path
from login_view import login_view__
from protuts_view import produtos_view
from relatorios import criar_relatorio,criar_relatorio_logs
from categoria_view import categorias_views
from dashboard import clt_view
def main(page: ft.Page):
    try:
        app_routes= [
            path(
                url='/',
                clear=True,
                view= login_view__
            ),
            path(
                url='/relatorio/produtos',
                clear=False,
                view=criar_relatorio
            ),
            path(
                url='/relatorio/logs',
                clear=False,
                view=criar_relatorio_logs
            ),
            path(
                url='/categorias',
                clear=False,
                view=categorias_views
            ),
            path(
                url='/produtos',
                clear=False,
                view=produtos_view
            ),
            # path(
            #     url='/produtos/editar',
            #     clear=False,
            #     view=
            # ),
            # path(
            #     url='/produtos/excluir',
            #     clear=False,
            #     view=
            # ),
            path(
                url='/dashboard/clt',
                clear=False,
                view=clt_view
            ),
            # path(
            #     url='/dashboard/adm',
            #     clear=False,
            #     view=
            # )

        ]

    except SyntaxError as e:
        print(f'ERRO AQUI SEU TROUXA {e}')

    Routing(page=page,app_routes=app_routes)
    page.go(page.route)

ft.app(target=main)