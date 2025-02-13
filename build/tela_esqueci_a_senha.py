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
valor_erro = ""

def tela_esqueci_a_senha(page: ft.Page):
    page.bgcolor = cor_cinza
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.title = "Esqueci a senha." 
    page.window.alignment = ft.alignment.top_center 
    page.window.width = 1000 # Largura
    page.window.height = 750 # Altura
    page.window.maximizable = False
    page.window.minimizable = False

    def botao_logar_se(e):
        from build.tela_login import tela_login
        page.clean()
        tela_login(page)
        page.update()

    def botao_cadastrar_se(e):
        from build.tela_cadastro import tela_cadastro
        page.clean()
        tela_cadastro(page)
        page.update()

    def fechar_alerta1(e):
        if entrada1_alerta1.content.value != entrada2_alerta1.content.value:
            valor_erro = "As senhas são diferentes!"
            texto1_alerta1.content.value = valor_erro
            texto1_alerta1.content.update()
        elif entrada1_alerta1.content.value == "" or entrada2_alerta1.content.value == "":
            valor_erro = "Preencha todos os campos!"
            texto1_alerta1.content.value = valor_erro
            texto1_alerta1.content.update()
        else:
            banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
            banco_cadastros = os.path.abspath(banco_cadastros)
            conn = sqlite3.connect(banco_cadastros)
            cursor = conn.cursor()
            id_empresa_data = entrada1_esqueci_a_senha.content.value
            email_data = entrada3_esqueci_a_senha.content.value
            pergunta_secreta_data = selecao1_esqueci_a_senha.content.value
            resposta_secreta_data = entrada3_esqueci_a_senha.content.value
            senha_data = entrada1_alerta1.content.value
            cursor.execute("""
            UPDATE tabela_cadastros 
            SET senha = ?
            WHERE id_empresa = ? 
            AND email = ? 
            AND pergunta_secreta = ? 
            AND resposta_secreta = ?;
            """, (senha_data, id_empresa_data, email_data, pergunta_secreta_data, resposta_secreta_data))
            conn.commit()
            page.close(alerta1_esqueci_a_senha)
            page.open(alerta3_esqueci_a_senha)

    def fechar_alerta2(e):
        page.close(alerta2_esqueci_a_senha)

    def botao_alterar_senha(e):
        if (entrada1_esqueci_a_senha.content.value == "" or entrada2_esqueci_a_senha.content.value == ""
        or selecao1_esqueci_a_senha.content.value == "" or entrada3_esqueci_a_senha.content.value == ""):
            valor_erro = "Preencha todos os campos!"
            alerta2_esqueci_a_senha.content.value = valor_erro
            page.open(alerta2_esqueci_a_senha)
        else:
            banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
            banco_cadastros = os.path.abspath(banco_cadastros)
            conn = sqlite3.connect(banco_cadastros)
            cursor = conn.cursor()
            id_empresa_data = entrada1_esqueci_a_senha.content.value
            email_data = entrada3_esqueci_a_senha.content.value
            pergunta_secreta_data = selecao1_esqueci_a_senha.content.value
            resposta_secreta_data = entrada3_esqueci_a_senha.content.value
            cursor.execute("""
            SELECT * FROM tabela_cadastros
            WHERE (id_empresa = ? and email = ? and pergunta_secreta = ? and resposta_secreta = ?)
            """, (id_empresa_data, email_data, pergunta_secreta_data, resposta_secreta_data))
            verificacao = cursor.fetchone()
            try:
                if (id_empresa_data in verificacao and email_data in verificacao
                and pergunta_secreta_data in verificacao and resposta_secreta_data in verificacao):
                    page.open(alerta1_esqueci_a_senha)
                else:
                    None
            except:
                valor_erro = "Cadastro não localizado!"
                alerta2_esqueci_a_senha.content.value = valor_erro
                page.open(alerta2_esqueci_a_senha)

    def mudar_visibilidade_senha(e):
        entrada1_alerta1.content.password = not entrada1_alerta1.content.password
        entrada2_alerta1.content.password = not entrada2_alerta1.content.password
        if icone1_alerta1.content.icon == ft.icons.VISIBILITY:
            icone1_alerta1.content.icon = ft.icons.VISIBILITY_OFF
        else:
            icone1_alerta1.content.icon = ft.icons.VISIBILITY
        entrada1_alerta1.update()
        entrada2_alerta1.update()
        icone1_alerta1.update()

    def fechar_alerta3(e):
        page.close(alerta3_esqueci_a_senha)
        time.sleep(0.1)
        botao_logar_se(e)

    # Tela de Esqueci a senha
    texto1_esqueci_a_senha = ft.Container(
        content=ft.Text(
            value="SEJA MUITO BEM-VINDO(A)", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    divisao1_esqueci_a_senha = ft.Container(
        content=ft.Divider(
            height=0, thickness=2, color=cor_branca
        ),
        alignment=ft.alignment.center,
        width=292
    )

    texto2_esqueci_a_senha = ft.Container(
        content=ft.Text(
            value="Se já possui uma conta,\nclique no botão abaixo.", text_align=ft.TextAlign.CENTER,
            font_family=fonte, size=16, italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    botao1_esqueci_a_senha = ft.Container(
        content=ft.Text(
            value="Logar-se", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
            italic=True, color=cor_cinza
        ),
        alignment=ft.alignment.center,
        width=150,
        height=40,
        bgcolor=cor_branca,
        border_radius=15,
        on_click=botao_logar_se
    )

    texto3_esqueci_a_senha = ft.Container(
        content=ft.Text(
            value="Se ainda não possui uma conta,\nclique no botão abaixo.", text_align=ft.TextAlign.CENTER,
            font_family=fonte, size=16, italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    botao2_esqueci_a_senha = ft.Container(
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

    fundo1_esqueci_a_senha = ft.Container(
        content=ft.Column(
            [
                texto1_esqueci_a_senha,
                divisao1_esqueci_a_senha,
                texto2_esqueci_a_senha,
                botao1_esqueci_a_senha,
                texto3_esqueci_a_senha,
                botao2_esqueci_a_senha
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_cinza,
        width=475,
        height=675,
        border_radius=15
    )

    texto4_esqueci_a_senha = ft.Container(
        content=ft.Text(
            value="MUDE SUA SENHA.", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_cinza
        ),
        alignment=ft.alignment.center
    )

    divisao2_esqueci_a_senha = ft.Container(
        content=ft.Divider(
            height=0, thickness=2, color=cor_cinza
        ),
        alignment=ft.alignment.center,
        width=292
    )

    entrada1_esqueci_a_senha = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="ID Empresa", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito)
        ),
        alignment=ft.alignment.center,
        width=450,
        height=40
    )

    entrada2_esqueci_a_senha = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Email", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito)
        ),
        alignment=ft.alignment.center,
        width=450,
        height=40
    )

    selecao1_esqueci_a_senha = ft.Container(
        content=ft.Dropdown(
            options=[
                ft.dropdown.Option(text="Qual era o nome do seu primeiro animal de estimação?"),
                ft.dropdown.Option(text="Qual é o nome do seu melhor amigo de infância?"),
                ft.dropdown.Option(text="Em que cidade você nasceu?"),
                ft.dropdown.Option(text="Qual é o nome do seu professor favorito da escola?"),
                ft.dropdown.Option(text="Qual era o modelo do seu primeiro celular?"),
                ft.dropdown.Option(text="Qual foi o primeiro jogo que você zerou?"),
                ft.dropdown.Option(text="Se você pudesse viver em um universo fictício, qual escolheria?"),
                ft.dropdown.Option(text="Qual foi o primeiro show ou evento que você participou?"),
                ft.dropdown.Option(text="Qual é o nome de um personagem fictício que marcou sua infância?"),
                ft.dropdown.Option(text="Qual era o apelido que você tinha quando criança?")
            ], alignment=ft.alignment.center_left, padding=0, text_size=13, label="Pergunta Secreta", color=cor_cinza,
            bgcolor=cor_branca, border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(
            size=16, weight=negrito, font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20,
            weight=negrito, font_family=fonte, color=cor_cinza)
        ),
        alignment=ft.alignment.center,
        width=450,
        height=40
    )

    entrada3_esqueci_a_senha = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Resposta Pergunta", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito)
        ),
        alignment=ft.alignment.center,
        width=450,
        height=40
    )

    botao3_esqueci_a_senha = ft.Container(
        content=ft.Text(
            value="Alterar senha", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
            italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center,
        width=150,
        height=40,
        bgcolor=cor_cinza,
        border_radius=15,
        on_click=botao_alterar_senha
    )

    fundo2_esqueci_a_senha = ft.Container(
        content=ft.Column(
            [
                texto4_esqueci_a_senha,
                divisao2_esqueci_a_senha,
                entrada1_esqueci_a_senha,
                entrada2_esqueci_a_senha,
                selecao1_esqueci_a_senha,
                entrada3_esqueci_a_senha,
                botao3_esqueci_a_senha
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_branca,
        width=475,
        height=675,
        border_radius=15
    )

    entrada1_alerta1 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Senha", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito), password=True
        ),
        alignment=ft.alignment.center,
        width=450,
        height=40
    )

    entrada2_alerta1 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Mesma Senha", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito), password=True
        ),
        alignment=ft.alignment.center,
        width=400,
        height=40
    )

    icone1_alerta1 = ft.Container(
        content=ft.IconButton(
            icon=ft.icons.VISIBILITY, icon_color=cor_cinza, icon_size=30, on_click=mudar_visibilidade_senha,
            focus_color=cor_transparente, hover_color=cor_transparente, splash_color=cor_transparente,
            highlight_color=cor_transparente
        ),
        alignment=ft.alignment.center,
        width=50,
        height=40
    )

    linha1_alerta1 = ft.Container(
        content=ft.Row(
            [
                entrada2_alerta1,
                icone1_alerta1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        alignment=ft.alignment.center
    )

    texto1_alerta1 = ft.Container(
        content=ft.Text(
            value="", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_vermelha
        ),
        alignment=ft.alignment.center
    )

    fundo1_alerta1 = ft.Container(
        content=ft.Column(
            [
                entrada1_alerta1,
                linha1_alerta1,
                texto1_alerta1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        width=450,
        height=100
    )

    alerta1_esqueci_a_senha = ft.AlertDialog(
        modal=True, title=ft.Text(value="Mude sua senha!", text_align=ft.TextAlign.START, font_family=fonte,
        size=20, weight=negrito, color=cor_cinza), content=fundo1_alerta1, actions=[
            ft.Container(
                content=ft.Text(
                    value="Mudar", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
                    italic=True, color=cor_branca
                ),
                alignment=ft.alignment.center,
                width=70,
                height=30,
                bgcolor=cor_cinza,
                border_radius=15,
                on_click=fechar_alerta1
            )
        ],
        bgcolor=cor_branca
    )

    alerta2_esqueci_a_senha = ft.AlertDialog(
        modal=True, title=ft.Text(value="Erro ao modificar!", text_align=ft.TextAlign.START, font_family=fonte,
        size=20, weight=negrito, color=cor_cinza), content=ft.Text(valor_erro,
        text_align=ft.TextAlign.START, font_family=fonte, size=16, color=cor_cinza), actions=[
            ft.Container(
                content=ft.Text(
                    value="Tentar Novamente", text_align=ft.TextAlign.CENTER, font_family=fonte,
                    size=16, weight=negrito, italic=True, color=cor_branca
                ),
                alignment=ft.alignment.center,
                width=160,
                height=30,
                bgcolor=cor_cinza,
                border_radius=15,
                on_click=fechar_alerta2
            )
        ], bgcolor=cor_branca
    )

    alerta3_esqueci_a_senha = ft.AlertDialog(
        modal=True, title=ft.Text(value="Modificado com sucesso!!", text_align=ft.TextAlign.START, font_family=fonte,
        size=20, weight=negrito, color=cor_cinza), content=ft.Text("Aperte no botão abaixo.",
        text_align=ft.TextAlign.START, font_family=fonte, size=16, color=cor_cinza), actions=[
            ft.Container(
                content=ft.Text(
                    value="Logar", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16,
                    weight=negrito, italic=True, color=cor_branca
                ),
                alignment=ft.alignment.center,
                width=160,
                height=30,
                bgcolor=cor_cinza,
                border_radius=15,
                on_click=fechar_alerta3
            )
        ], bgcolor=cor_branca
    )

    tela_esqueci_a_senha = ft.Container(
        content=ft.Row(
            [
                fundo1_esqueci_a_senha,
                fundo2_esqueci_a_senha
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        alignment=ft.alignment.center
    )

    tela_atual = ft.Container(
        content=ft.Column(
            [
                tela_esqueci_a_senha
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)

#ft.app(target=tela_esqueci_a_senha)