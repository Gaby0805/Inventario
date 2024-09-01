import flet as ft
#erro aqui no import
def login_view(page: ft.Page):

    def button_send(e):
        bread = tru.autentfy()
        text_name = textfield_name.value
        text_password = textfield_senha.value
        bread(text_name, text_password)
        bread(text_name,text_password)
        if bread:
            print('tudo cecrto  flet')
        else:
            print('erro no flet')


    login_text = ft.Text()
    textfield_name = ft.TextField(label='Nome',input_filter=ft.TextOnlyInputFilter() ,width=450, )
    textfield_senha = ft.TextField(label='senha' ,width=450)
    button_create = ft.ElevatedButton('Enviar', on_click=button_send)


    page.add(textfield_name, textfield_senha, button_create)

ft.app(target=login_view)
