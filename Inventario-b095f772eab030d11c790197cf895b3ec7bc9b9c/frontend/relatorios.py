import flet as ft
import flet as ft
from sys import path
from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.produtos as prods
import backend.logs_ as lgs
from fpdf import FPDF

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

def criar_relatorio(page:ft.Page):
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
    page.add(categorias,gerar_relatorio)


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

def criar_relatorio_logs(page:ft.Page):

    def clicacao(e):
        criar_pdf_logs()

    gerar_relatorio = ft.ElevatedButton('gerar PDF', on_click=clicacao)
    page.add(gerar_relatorio)


ft.app(target=criar_relatorio_logs)














