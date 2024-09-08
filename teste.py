import flet as ft


def main(page: ft.Page):
    page.title = "AlertDialog examples"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def handle_close(e):
        page.close(dlg_modal)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please a"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("ok", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        )


    page.add(
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),
    )


ft.app(main)