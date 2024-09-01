import flet as ft

#concerta import
def produtos_view(page: ft.Page):



    def submite_button_action(e):

        pass

    

    nome_product = ft.TextField(label='nome do produto')
    # category_product =ft.Dropdown(
    #     ft.dropdown.Option('1'),
    #     ft.dropdown.Option('2'),
    #     ft.dropdown.Option('3')
        
        
        
    #     )
    description_product = ft.TextField(label='descrição do produto')
    # tem que ajeitar o price_product para aceitar float, tem que ver primeiro nO BD isso
    price_product =ft.TextField(label='preço do produto', input_filter=ft.NumbersOnlyInputFilter())
    quantity_product = ft.TextField(label='quantidade de protudo', input_filter=ft.NumbersOnlyInputFilter() )
    submite_button = ft.ElevatedButton('enviar', on_click=submite_button_action)

    page.add( nome_product,description_product,price_product,quantity_product,submite_button)

ft.app(target=produtos_view)