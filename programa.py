import flet as ft

from build.tela_login import tela_login

def programa(page: ft.Page):
    tela_login(page)

ft.app(target=programa)