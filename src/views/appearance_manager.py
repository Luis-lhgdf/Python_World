
import customtkinter as ctk
import os
import json
import pkg_resources

class AppearanceManager:
    def __init__(self):

        self.font_title = ("Open Sans", 30, "bold", "italic")
        self.font_subtitle = ("Open Sans", 20)
        self.font_body = ("Open Sans", 12)


    

    def get_font_title(self):
        return self.font_title
    

    def get_font_subtitle(self, bold=False):
        if bold:
            return ("Open Sans", 20, "bold")
        else:
            return self.font_subtitle


    def get_font_body(self, bold=False):  # Adicionando um parâmetro opcional para negrito
        if bold:
            return ("Open Sans", 12, "bold")
        else:
            return self.font_body
        
