
import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplos de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_nome(e):
        if input_nome.value == "":
            page.overlay.append(mgss_erro)
            mgss_erro.open = True
            page.update()

        else:
            lista.append(input_nome.value)
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def exibir_nomes(e):
        lv_Nomes.controls.clear()
        for nome in lista:
            lv_Nomes.controls.append(
                ft.Text(value=nome)
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_nome(e),
                    ),
                        ft.Button(
                            text="Exibir nomes",
                            on_click=lambda _: page.go("/segunda")
                        )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_nomes(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_Nomes,
                        ft.FloatingActionButton(text="+")
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("nome ta salvo bro"),
        bgcolor=Colors.RED
        )
    mgss_erro = ft.SnackBar(
        content=ft.Text("erro ao salvar"),
        bgcolor=Colors.RED
    )
    input_nome = ft.TextField("Nomes")
    btn_salvar = ft.Button("Salvar")

    lv_Nomes = ft.ListView(
        height=500,
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)

