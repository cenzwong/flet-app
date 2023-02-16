import flet as ft
import component



def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # add application's root control to the page
    # create application instance
    app1 = component.Prompt()

    # add application's root control to the page
    page.add(app1)

ft.app(target=main)