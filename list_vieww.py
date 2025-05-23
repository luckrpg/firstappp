import flet as ft
from flet import AppBar, Text, View, Column
from flet.core.colors import Colors


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplos de listas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_informacoes(e):
        if input_nome.value == "" or input_profissao.value == "" or input_salario.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            nome = input_nome.value
            profissao = input_profissao.value
            salario = input_salario.value
            lista.append({
                "nome": nome,
                "profissao": profissao,
                "salario": salario
            })
            input_nome.value = ""
            input_profissao.value = ""
            input_salario.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def exibir_informacoes(e):
        lv_informacoes.controls.clear()
        for info in lista:
            lv_informacoes.controls.append(
                ft.Text(value=f"Nome: {info['nome']} - Profissão: {info['profissao']} - Salário: R$ {info['salario']}")
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    Column(
                        controls=[
                            input_nome,
                            input_profissao,
                            input_salario,
                            ft.Button(
                                text="Salvar",
                                on_click=salvar_informacoes,
                            ),
                            ft.Button(
                                text="Exibir informações",
                                on_click=lambda _: page.go("/segunda")
                            )
                        ]
                    )
                ],
            )
        )
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
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN
        )
    msg_erro = ft.SnackBar(
        content=ft.Text("Erro ao salvar. Preencha todos os campos."),
        bgcolor=Colors.RED
    )
    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

    lv_informacoes = ft.ListView(
        height=500,
        spacing=10
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
ft.app(main)