import flet as ft
import flet as ft
from sys import path
from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.produtos as prods
import backend.logs_ as lgs
from fpdf import FPDF
import backend.autentica as aut
def criar_pdf_produtos(categoria):
    listar = prods.listar_produts(categoria)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Lista de Itens", ln=True, align="C")

    for i in listar:
        name = f'id: {i[0]}, nome: {i[1]}, descrição: {i[2]} , preço: {i[3]} , quantidade: {i[4]}, categoria: {i[5]}'
    
        pdf.cell(200, 10, txt=name, ln=True, align="L")
    pdf.output('relatorio.pdf')




def criar_relatorio(page:ft.Page, params: Params, basket: Basket):
    listar = prods.listar_produts(0)

    def clicacao(e):
        # caso n tenha valor ele vai imprimir a tabela inteira
        if categorias.value == None:
            criar_pdf_produtos(0)
        else:
            criar_pdf_produtos(int(categorias.value))


    #selecionar categorias
    categorias = ft.Dropdown(label='categorias', options=[ft.dropdown.Option(str(i[0]), text=i[1])for i in listar])
    gerar_relatorio = ft.ElevatedButton('gerar PDF', on_click=clicacao)
    return_button = ft.ElevatedButton('voltar', on_click= lambda _: page.go('/relatorios'))
    return ft.View(
     "/relatorio/produtos",
    controls=[
            categorias,
            gerar_relatorio,
            return_button

        ]

             )


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------



def criar_pdf_logs():
    listar = prods.lgs.listar_logs()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Logs", ln=True, align="C")

    for i in listar:
        name = f'id: {i[0]}, Log: {i[1]} '
    
        pdf.cell(200, 10, txt=name, ln=True, align="L")
    pdf.output('relatorio_logs.pdf')

def criar_relatorio_logs(page:ft.Page, params: Params, basket:Basket):

    def clicacao(e):
        criar_pdf_logs()
    return_button = ft.ElevatedButton('voltar', on_click= lambda _: page.go('/relatorios'))
    gerar_relatorio = ft.ElevatedButton('gerar PDF', on_click=clicacao)
    return ft.View(
        '/relatorios/logs',
        controls=[
            gerar_relatorio,
            return_button

        ]
        
        )


def relatorios(page:ft.Page, params: Params, basket: Basket):
    def send(e):
        
        instancia = aut.Autenticador.lista
        print(instancia[0])
        if instancia[0] == ('adm',):
            page.go(f'/dashboard/adm')
            print('tudo certo adm page')
        elif instancia[0] == ('clt',):
            print(instancia[0])
            page.go(f'/dashboard/clt')
            print('tudo certo, clt page')
        else:
            print('bananiha frita')

    botao = ft.ElevatedButton('relatorio produtos', on_click= lambda _: page.go('/relatorios/produtos'))
    bb = ft.ElevatedButton('relatorio lolgs', on_click=lambda _: page.go('/relatorios/logs'))
    po = ft.ElevatedButton('voltar', on_click=send)

    return ft.View(
        '/relatorios',
        controls=[
            botao,
            bb,
            po
        ]
        )