import flet as ft

#concerta import
def produtos_view(page: ft.Page):



    def submite_button_action(e):

        pass

    
    nome_product = ft.TextField(label='nome do produto')
    #ajeitar drop box
    category_product =ft.Dropdown()



    description_product = ft.TextField(label='descrição do produto')
    # tem que ajeitar o price_product para aceitar float, tem que ver primeiro nO BD isso
    price_product =ft.TextField(label='preço do produto', input_filter=ft.NumbersOnlyInputFilter())
    quantity_product = ft.TextField(label='quantidade de protudo', input_filter=ft.NumbersOnlyInputFilter() )
    submite_button = ft.ElevatedButton('enviar', on_click=submite_button_action)

    page.add( category_product,nome_product,description_product,price_product,quantity_product,submite_button)

ft.app(target=produtos_view)