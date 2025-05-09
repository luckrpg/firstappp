import flet as ft
from flet import AppBar, Text, View, Column
from flet.core.colors import Colors



def main(page: ft.Page):
    # Configurações
    page.title = "Profissões e Salários"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    def salvar_informacoes(e):
        if input_profissao.value == "" or input_salario.value == "":
            page.snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campo"), bgcolor=Colors.RED)
            page.snack_bar.open = True
            page.update()
        else:
            profissao = input_profissao.value
            salario = input_salario.value

            # Salvar no banco de dados
            if salvar_profissao(profissao, salario):
                input_profissao.value = ""
                input_salario.value = ""
                page.snack_bar = ft.SnackBar(content=ft.Text("Informação salva com sucesso!"), bgcolor=Colors.GREEN)
            else:
                page.snack_bar = ft.SnackBar(content=ft.Text("Erro ao salvar informação!"), bgcolor=Colors.RED)

            page.snack_bar.open = True
            page.update()

    def exibir_informacoes(e):
        lv_informacoes.controls.clear()

        # Buscar do banco de dados
        profissoes = listar_profissoes()

        for profissao in profissoes:
            lv_informacoes.controls.append(ft.Text(value=str(profissao)))

        page.update()

    def gerencia_rotas(e):
        page.views.clear()

        # Tela principal
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    Column(
                        controls=[
                            input_profissao,
                            input_salario,
                            ft.Button(
                                text="Salvar Informação",
                                on_click=salvar_informacoes,
                            ),
                            ft.Button(
                                text="Exibir Informações",
                                on_click=lambda _: page.go("/segunda")
                            ),
                        ]
                    ),
                ],
            )
        )

        # Tela de exibição
        if page.route == "/segunda":
            exibir_informacoes(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Informações Salvas"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_informacoes,
                        ft.FloatingActionButton(text="Voltar", on_click=lambda _: page.go("/"))
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")
    lv_informacoes = ft.ListView(height=500, spacing=10)

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
ft.app(main)
