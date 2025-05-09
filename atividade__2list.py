import flet as ft
from flet import AppBar, Text, View, Column, Row
from flet.core.colors import Colors


def main(page: ft.Page):
    # Configurações
    page.title = "Biblioteca de Livros"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Lista de livros
    livros = []

    # Funções
    def salvar_livro(e):
        if input_titulo.value == "" or input_autor.value == "" or input_resumo.value == "":
            page.snack_bar = ft.SnackBar(content=ft.Text("Preencha todos os campos!"), bgcolor=Colors.RED)
            page.snack_bar.open = True
            page.update()
        else:
            titulo = input_titulo.value
            autor = input_autor.value
            ano = input_ano.value
            resumo = input_resumo.value
            livros.append({"titulo": titulo, "autor": autor, "ano": ano, "resumo": resumo})
            input_titulo.value = ""
            input_autor.value = ""
            input_ano.value = ""
            input_resumo.value = ""
            page.snack_bar = ft.SnackBar(content=ft.Text("Livro salvo com sucesso!"), bgcolor=Colors.GREEN)
            page.snack_bar.open = True
            page.update()

    def exibir_livros(e):
        lv_livros.controls.clear()
        for livro in livros:
            lv_livros.controls.append(
                Row(
                    controls=[
                        ft.Text(f"{livro['titulo']} - {livro['autor']} ({livro['ano']})", expand=True),
                        ft.Button("Detalhes", on_click=lambda e, livro=livro: mostrar_detalhes(livro)),
                    ],
                    spacing=10,
                )
            )
        page.update()

    def mostrar_detalhes(livro):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Detalhes do Livro"),
            content=ft.Text(f"Título: {livro['titulo']}\nAutor: {livro['autor']}\nAno: {livro['ano']}\n\nResumo:\n{livro['resumo']}"),
            actions=[
                ft.TextButton("Fechar", on_click=lambda _: page.dialog.close()),
            ],
        )
        page.dialog.open = True
        page.update()

    def gerenciar_rotas(e):
        page.views.clear()

        # Tela principal
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de Livros"), bgcolor=Colors.PRIMARY_CONTAINER),
                    Column(
                        controls=[
                            input_titulo,
                            input_autor,
                            input_ano,
                            input_resumo,
                            ft.Button("Salvar Livro", on_click=salvar_livro),
                            ft.Button("Exibir Livros", on_click=lambda _: page.go("/listar")),
                        ]
                    ),
                ],
            )
        )

        # Tela de listagem
        if page.route == "/listar":
            exibir_livros(e)
            page.views.append(
                View(
                    "/listar",
                    [
                        AppBar(title=Text("Lista de Livros"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_livros,
                        ft.FloatingActionButton(text="Voltar", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    input_titulo = ft.TextField(label="Título")
    input_autor = ft.TextField(label="Autor")
    input_ano = ft.TextField(label="Ano", hint_text="Opcional")
    input_resumo = ft.TextField(label="Resumo", multiline=True, min_lines=3, max_lines=5)

    lv_livros = ft.ListView(height=500, spacing=10)

    # Eventos
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
ft.app(main)
