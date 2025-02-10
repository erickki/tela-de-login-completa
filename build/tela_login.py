import flet as ft
import time
import os
import sqlite3

cor_cinza = "#1a1a1a"
cor_branca = "#ebebeb"
cor_azul = "#1968a8"
cor_vermelha = "#f22929"
cor_transparente = ft.colors.TRANSPARENT
negrito = ft.FontWeight.BOLD
fonte = "Roboto"

def tela_login(page: ft.Page):
    page.bgcolor = cor_cinza
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.title = "Faça seu login."
    page.window.alignment = ft.alignment.top_center
    page.window.width = 1000 # Largura
    page.window.height = 500 # Altura
    page.window.maximizable = False
    page.window.minimizable = False

    def botao_cadastrar_se(e):
        from build.tela_cadastro import tela_cadastro
        page.clean()
        tela_cadastro(page)
        page.update()

    def botao_logar_se(e):
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        id_empresa_data = entrada1_login.content.value
        senha_data = entrada2_login.content.value
        cursor.execute("""
        SELECT * FROM tabela_cadastros
        WHERE (id_empresa = ? and senha = ?)
        """, (id_empresa_data, senha_data))
        verificacao = cursor.fetchone()
        try:
            if (id_empresa_data in verificacao and senha_data in verificacao):
                page.open(alerta1_login)
            else:
                pass
        except:
            page.open(alerta2_login)

    def botao_esqueci_a_senha(e):
        from build.tela_esqueci_a_senha import tela_esqueci_a_senha
        page.clean()
        tela_esqueci_a_senha(page)
        page.update()

    def fechar_programa(e):
        page.window.close()

    def tentar_novamente(e):
        page.close(alerta2_login)

    def mudar_visibilidade_senha(e):
        entrada2_login.content.password = not entrada2_login.content.password
        if icone1_login.content.icon == ft.icons.VISIBILITY:
            icone1_login.content.icon = ft.icons.VISIBILITY_OFF
        else:
            icone1_login.content.icon = ft.icons.VISIBILITY
        entrada2_login.update()
        icone1_login.update()

    # Tela de Login
    texto1_login = ft.Container(
        content=ft.Text(
            value="BEM-VINDO(A) DE VOLTA", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    divisao1_login = ft.Container(
        content=ft.Divider(
            height=0, thickness=2, color=cor_branca
        ),
        alignment=ft.alignment.center,
        width=292
    )

    texto2_login = ft.Container(
        content=ft.Text(
            value="Se ainda não possui uma conta,\nclique no botão abaixo.", text_align=ft.TextAlign.CENTER,
            font_family=fonte, size=16, italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    botao1_login = ft.Container(
        content=ft.Text(
            value="Cadastrar-se", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
            italic=True, color=cor_cinza
        ),
        alignment=ft.alignment.center,
        width=150,
        height=40,
        bgcolor=cor_branca,
        border_radius=15,
        on_click=botao_cadastrar_se
    )

    fundo1_login = ft.Container(
        content=ft.Column(
            [
                texto1_login,
                divisao1_login,
                texto2_login,
                botao1_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_cinza,
        width=475,
        height=425,
        border_radius=15
    )

    texto3_login = ft.Container(
        content=ft.Text(
            value="FAÇA SEU LOGIN.", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_cinza
        ),
        alignment=ft.alignment.center
    )

    divisao2_login = ft.Container(
        content=ft.Divider(
            height=0, thickness=2, color=cor_cinza
        ),
        alignment=ft.alignment.center,
        width=292
    )

    entrada1_login = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="ID Empresa", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito)
        ),
        alignment=ft.alignment.center,
        width=250,
        height=40
    )

    entrada2_login = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Senha", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito), password=True
        ),
        alignment=ft.alignment.center,
        width=200,
        height=40
    )

    icone1_login = ft.Container(
        content=ft.IconButton(
            icon=ft.icons.VISIBILITY, icon_color=cor_cinza, icon_size=30, on_click=mudar_visibilidade_senha,
            focus_color=cor_transparente, hover_color=cor_transparente, splash_color=cor_transparente,
            highlight_color=cor_transparente
        ),
        alignment=ft.alignment.center,
        width=50,
        height=40
    )

    linha1_login = ft.Container(
        content=ft.Row(
            [
                entrada2_login,
                icone1_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        alignment=ft.alignment.center
    )

    botao2_login = ft.Container(
        content=ft.Text(
            value="Logar-se", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
            italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center,
        width=150,
        height=40,
        bgcolor=cor_cinza,
        border_radius=15,
        on_click=botao_logar_se
    )

    botao3_login = ft.Container(
        content=ft.Text(
            value="Esqueci a senha", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
            italic=True, color=cor_vermelha
        ),
        alignment=ft.alignment.center,
        width=150,
        height=40,
        on_click=botao_esqueci_a_senha
    )

    fundo2_login = ft.Container(
        content=ft.Column(
            [
                texto3_login,
                divisao2_login,
                entrada1_login,
                linha1_login,
                botao2_login,
                botao3_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_branca,
        width=475,
        height=425,
        border_radius=15
    )

    tela_login = ft.Container(
        content=ft.Row(
            [
                fundo1_login,
                fundo2_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        alignment=ft.alignment.center
    )

    alerta1_login = ft.AlertDialog(
        modal=True, title=ft.Text(value="Logado com sucesso!", text_align=ft.TextAlign.START, font_family=fonte,
        size=20, weight=negrito, color=cor_cinza), content=ft.Text("Aperte no botão abaixo.",
        text_align=ft.TextAlign.START, font_family=fonte, size=16, color=cor_cinza), actions=[
            ft.Container(
                content=ft.Text(
                    value="Entrar", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
                    italic=True, color=cor_branca
                ),
                alignment=ft.alignment.center,
                width=70,
                height=30,
                bgcolor=cor_cinza,
                border_radius=15,
                on_click=fechar_programa
            )
        ], bgcolor=cor_branca
    )

    alerta2_login = ft.AlertDialog(
        modal=True, title=ft.Text(value="Erro no Login!", text_align=ft.TextAlign.START, font_family=fonte,
        size=20, weight=negrito, color=cor_cinza), content=ft.Text("Erro ao localizar!",
        text_align=ft.TextAlign.START, font_family=fonte, size=16, color=cor_cinza), actions=[
            ft.Container(
                content=ft.Text(
                    value="Tentar Novamente", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16,
                    weight=negrito, italic=True, color=cor_branca
                ),
                alignment=ft.alignment.center,
                width=160,
                height=30,
                bgcolor=cor_cinza,
                border_radius=15,
                on_click=tentar_novamente
            )
        ], bgcolor=cor_branca
    )

    tela_atual = ft.Container(
        content=ft.Column(
            [
                tela_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)

#ft.app(target=tela_login)