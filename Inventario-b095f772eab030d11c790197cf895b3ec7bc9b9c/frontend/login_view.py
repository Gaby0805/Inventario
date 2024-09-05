import flet as ft
from sys import path
from flet_route import Basket, Params
path.append('./Inventario-b095f772eab030d11c790197cf895b3ec7bc9b9c/frontend/backend')
import backend.autentica as aut
def login_view__(page: ft.Page, params: Params, basket:Basket):
    
    def button_send(e):
        
        text_gmail = textfield_name.value
        text_password = textfield_senha.value
        bread,tipo = aut.Autenticador.autentfy(text_gmail,text_password)
        if bread and tipo[0] =="adm":
            print('tudo cecrto  flet')
            page.go('/adm/')
            
        elif bread and tipo[0] =='clt':
            print('seu CLT DE BOSTA')
            page.go('/clt')

        else:
            print('erro no flet')
        print(bread, tipo)

    login_text = ft.Text()
    textfield_name = ft.TextField(label='gmail',input_filter=ft.TextOnlyInputFilter() ,width=450, )
    textfield_senha = ft.TextField(label='senha' ,width=450)
    button_create = ft.ElevatedButton('Enviar', on_click=button_send)
    
    return ft.View(
        "/",
        controls=[
        textfield_name, textfield_senha, button_create

        ]
    )


