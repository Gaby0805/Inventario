import flet as ft
import ..backend.autenticação

def login_view(page: ft.Page):
    

    def button_send(e):
        
        pass

    textfield_name = ft.TextField(label='Nome',input_filter=ft.TextOnlyInputFilter())
    textfield_senha = ft.TextField(label='senha')
    button_create = ft.ElevatedButton('Enviar', on_click=button_send)


    page.add()

ft.app(target=login_view)
