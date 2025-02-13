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

def tela_cadastro(page: ft.Page):
    page.bgcolor = cor_cinza
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.title = "Faça seu cadastro." 
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
        if (entrada1_cadastro.content.value == "" or entrada2_cadastro.content.value == ""
        or entrada3_cadastro.content.value == "" or entrada4_cadastro.content.value == ""
        or entrada5_cadastro.content.value == "" or entrada6_cadastro.content.value == ""):
            valor_erro = "Preencha todos os campos!"
            alerta2_cadastro.content.value = valor_erro
            page.open(alerta2_cadastro)
        elif entrada4_cadastro.content.value != entrada5_cadastro.content.value:
            valor_erro = "As senhas são diferentes!"
            alerta2_cadastro.content.value = valor_erro
            page.open(alerta2_cadastro)
        else:
            banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
            banco_cadastros = os.path.abspath(banco_cadastros)
            conn = sqlite3.connect(banco_cadastros)
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tabela_cadastros (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    id_empresa TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    pergunta_secreta TEXT NOT NULL,
                    resposta_secreta TEXT NOT NULL,
                    cargo TEXT NOT NULL
            );
            """)
            nome_data = entrada1_cadastro.content.value
            email_data = entrada2_cadastro.content.value
            id_empresa_data = entrada3_cadastro.content.value
            senha_data = entrada4_cadastro.content.value
            pergunta_secreta_data = selecao1_cadastro.content.value
            resposta_secreta_data = entrada6_cadastro.content.value
            cargo_data = "none"
            cursor.execute("""
            INSERT INTO tabela_cadastros(nome, email, id_empresa, senha, pergunta_secreta, resposta_secreta,
            cargo) VALUES(?,?,?,?,?,?,?)
            """, (nome_data, email_data, id_empresa_data, senha_data, pergunta_secreta_data,
                resposta_secreta_data, cargo_data))
            conn.commit()
            page.open(alerta1_cadastro)

    def fechar_alerta1(e):
        page.close(alerta1_cadastro)
        time.sleep(0.1)
        botao_logar_se(e)

    def fechar_alerta2(e):
        page.close(alerta2_cadastro)

    def mudar_visibilidade_senha(e):
        entrada4_cadastro.content.password = not entrada4_cadastro.content.password
        entrada5_cadastro.content.password = not entrada5_cadastro.content.password
        if icone1_cadastro.content.icon == ft.icons.VISIBILITY:
            icone1_cadastro.content.icon = ft.icons.VISIBILITY_OFF
        else:
            icone1_cadastro.content.icon = ft.icons.VISIBILITY
        entrada4_cadastro.update()
        entrada5_cadastro.update()
        icone1_cadastro.update()

    # Tela de Cadastro
    texto1_cadastro = ft.Container(
        content=ft.Text(
            value="SEJA MUITO BEM-VINDO(A)", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    divisao1_cadastro = ft.Container(
        content=ft.Divider(
            height=0, thickness=2, color=cor_branca
        ),
        alignment=ft.alignment.center,
        width=292
    )

    texto2_cadastro = ft.Container(
        content=ft.Text(
            value="Se já possui uma conta,\nclique no botão abaixo.", text_align=ft.TextAlign.CENTER,
            font_family=fonte, size=16, italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center
    )

    botao1_cadastro = ft.Container(
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

    fundo1_cadastro = ft.Container(
        content=ft.Column(
            [
                texto1_cadastro,
                divisao1_cadastro,
                texto2_cadastro,
                botao1_cadastro
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

    texto3_cadastro = ft.Container(
        content=ft.Text(
            value="FAÇA SEU CADASTRO.", text_align=ft.TextAlign.CENTER, font_family=fonte, size=20, weight=negrito,
            color=cor_cinza
        ),
        alignment=ft.alignment.center
    )

    divisao2_cadastro = ft.Container(
        content=ft.Divider(
            height=0, thickness=2, color=cor_cinza
        ),
        alignment=ft.alignment.center,
        width=292
    )

    entrada1_cadastro = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_cinza, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Nome Completo", color=cor_cinza,
            border_radius=15, border_width=2, border_color=cor_cinza, text_style=ft.TextStyle(size=16,
            font_family=fonte, color=cor_cinza), label_style=ft.TextStyle(size=20, font_family=fonte, color=cor_cinza,
            weight=negrito)
        ),
        alignment=ft.alignment.center,
        width=450,
        height=40
    )

    entrada2_cadastro = ft.Container(
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

    entrada3_cadastro = ft.Container(
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

    entrada4_cadastro = ft.Container(
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

    entrada5_cadastro = ft.Container(
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

    icone1_cadastro = ft.Container(
        content=ft.IconButton(
            icon=ft.icons.VISIBILITY, icon_color=cor_cinza, icon_size=30, on_click=mudar_visibilidade_senha,
            focus_color=cor_transparente, hover_color=cor_transparente, splash_color=cor_transparente,
            highlight_color=cor_transparente
        ),
        alignment=ft.alignment.center,
        width=50,
        height=40
    )

    linha1_cadastro = ft.Container(
        content=ft.Row(
            [
                entrada5_cadastro,
                icone1_cadastro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        alignment=ft.alignment.center
    )

    selecao1_cadastro = ft.Container(
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

    entrada6_cadastro = ft.Container(
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

    botao2_cadastro = ft.Container(
        content=ft.Text(
            value="Cadastrar-se", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
            italic=True, color=cor_branca
        ),
        alignment=ft.alignment.center,
        width=150,
        height=40,
        bgcolor=cor_cinza,
        border_radius=15,
        on_click=botao_cadastrar_se
    )

    fundo2_cadastro = ft.Container(
        content=ft.Column(
            [
                texto3_cadastro,
                divisao2_cadastro,
                entrada1_cadastro,
                entrada2_cadastro,
                entrada3_cadastro,
                entrada4_cadastro,
                linha1_cadastro,
                selecao1_cadastro,
                entrada6_cadastro,
                botao2_cadastro
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

    tela_cadastro = ft.Container(
        content=ft.Row(
            [
                fundo1_cadastro,
                fundo2_cadastro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        alignment=ft.alignment.center
    )

    alerta1_cadastro = ft.AlertDialog(
        modal=True, title=ft.Text(value="Cadastrado com sucesso!", text_align=ft.TextAlign.START, font_family=fonte,
        size=20, weight=negrito, color=cor_cinza),
        content=ft.Text("Aguarde alguem ativar seu Login\nAperte no botão abaixo.", text_align=ft.TextAlign.START,
        font_family=fonte, size=16, color=cor_cinza), actions=[
            ft.Container(
                content=ft.Text(
                    value="Voltar", text_align=ft.TextAlign.CENTER, font_family=fonte, size=16, weight=negrito,
                    italic=True, color=cor_branca
                ),
                alignment=ft.alignment.center,
                width=70,
                height=30,
                bgcolor=cor_cinza,
                border_radius=15,
                on_click=fechar_alerta1
            )
        ], bgcolor=cor_branca
    )

    alerta2_cadastro = ft.AlertDialog(
        modal=True, title=ft.Text(value="Erro no Cadastro!", text_align=ft.TextAlign.START, font_family=fonte,
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

    tela_atual = ft.Container(
        content=ft.Column(
            [
                tela_cadastro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)

#ft.app(target=tela_cadastro)