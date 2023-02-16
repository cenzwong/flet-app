import flet as ft
import ai21_func

class Prompt(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.new_button = ft.FloatingActionButton(icon=ft.icons.SEND, on_click=self.send_clicked)
        self.response = ft.Column()

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        self.new_button,
                    ],
                ),
                self.response,
            ],
        )

    def send_clicked(self, e):
        ai21_response = ai21_func.ai21_rewrite(self.new_task.value, "formal")
        for suggestions in ai21_response:
            self.response.controls.append(ft.Checkbox(label=suggestions["text"]))

        self.new_task.value = ""
        self.update()