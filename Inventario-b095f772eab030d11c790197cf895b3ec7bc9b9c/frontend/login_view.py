
import flet as ft
from sys import path
from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.autentica as aut
import backend.logs_ as lgs
from flet import colors
def login_view__(page: ft.Page, params: Params, basket:Basket):
    page.title = 'Login'
    page.bgcolor = '#000'
    page.window.height = 700
    page.window.width = 500
    page.window.resizable = False
    page.window.minimizable = False
    page.window.center()
    
    def fechar_tela(e):
        page.close(dlg)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text('algum erro no login'),
        content=ft.Text('nome ou senha está errado'),
        actions=[
            ft.ElevatedButton('ok', on_click=fechar_tela)])


    
    def button_send(e):
        try:
            
            text_gmail = textfield_name.value
            text_password = textfield_senha.value
            
            if '@' not in text_gmail:
                print('n tem arroba no flet')
            
            else:
                bread,tipo = aut.Autenticador.autentfy(text_gmail,text_password)
                
                if tipo == None:
                    page.open(dlg)
                else:
                    if bread and tipo[0] =="adm":
                        lgs.logs('usuario logado administrador')
                        page.go('/dashboard/adm')
                        
                        
                    elif bread and tipo[0] =='clt':
                        print('seu CLT DE BOSTA')
                        page.go('/dashboard/clt/')
                        lgs.logs('usuario logado padrão')
                        



        except NameError as e:
            lgs.logs(e)
            #fazer error dialog 



    login_text = ft.Text('Login de usuario')
    textfield_name = ft.TextField(label='gmail',input_filter=ft.InputFilter(allow=True, regex_string=r'^[a-z,@,.,1-9, A-Z]*$') ,width=450,border_color=colors.WHITE, hint_text='coloque @' )
    textfield_senha = ft.TextField(label='senha' ,width=450, border_color=colors.WHITE)
    button_create = ft.ElevatedButton('Enviar', color=colors.WHITE,on_click=button_send,bgcolor=colors.GREY)
    page.add(textfield_name, textfield_senha, button_create)
    return ft.View(
        "/",
        controls=[
            login_text,
            ft.Column(controls=[
            ft.Container(padding=110),
            textfield_name,
            textfield_senha,
            button_create
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
            
        ]
    )