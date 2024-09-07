import flet as ft
import flet as ft
from sys import path
from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.produtos as prods
import backend.logs_ as lgs


def criar_relatorio(page:ft.Page):
    listar = prods.listar_produts
    text_field = ft.TextField(disabled=True, value=(str))