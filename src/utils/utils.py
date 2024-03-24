import ctypes
import webbrowser
import customtkinter as ctk
import re
import hashlib

class Utilities:

    def __init__(self) -> None:
        pass
        

    @staticmethod
    def msgbox(title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue

        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    @staticmethod
    def open_website(url):
        # URL do site que deseja abrir
        website_url = url
        # Abrir o site no navegador padrão
        webbrowser.open(website_url)

    @staticmethod
    def restart_interface(frame):
        # Destruir todos os widgets existentes
        for widget in frame.winfo_children():
            widget.grid_remove()


