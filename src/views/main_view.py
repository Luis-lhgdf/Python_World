import customtkinter as ctk
from src.utils.utils import Utilities
from src.views.icones import *
from CTkXYFrame import *
import openai
import threading
import tkinter as tk


class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.utils = Utilities()

        
        self.geometry("1200x650")
        self.configure(fg_color="#558FAD")


        self.font_title = ("Fixedsys", 50, "bold")
        self.font_subtitle = ("Fixedsys", 22,)
        self.font_body = ("Fixedsys", 20,)

        self.font_code = ("Consolas", 20,)
        

        self.linkedin_url = "https://linkedin.com/in/luis-henrique-281b97186"
        self.github_url = "https://github.com/Luis-lhgdf"
        self.site_url = "https://luis-lhgdf.github.io/portfolio/"
        self.cursoemvideo_url = "https://www.cursoemvideo.com/curso/python-3-mundo-1/"


        self.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.grid_columnconfigure(1, weight=1)  # Coluna 1 vai expandir
        self.grid_rowconfigure(0, weight=1)


        # Frame para os botões de navegação à esquerda
        self.menu_navigation = ctk.CTkFrame(self, width=500, corner_radius=0, fg_color="#171D23")
        self.menu_navigation.grid(row=0, column=0, sticky="nsew")
        
        self.word_frame = ctk.CTkFrame(self, width=100, fg_color="#D78A1E", corner_radius=20)
        self.word_frame.grid(row=0, column=1, padx=(10,10), pady=10, sticky="nsew")


        # label principal para exibição dos titulos dos exercicios
        self.exercise_label = ctk.CTkLabel(self, text="", fg_color="#171D23", text_color="#4C76D9" )
        #self.exercise_label.grid(row=0, column=1, sticky="nsew")


        # Frame principal para exibição das opções dos exercicios
        self.exercise_options = CTkXYFrame(self, width=100, fg_color="#FFF6E9", corner_radius=20)

        self.solution_textbox = ctk.CTkTextbox(self, width=100, fg_color="#23272D", font=self.font_code, corner_radius=20, text_color="white")
        

        self.show_exercises()

        # self.menu_view()
        self.mainloop()


    def menu_view(self):
        self.title("Escolha o Mundo")

        self.menu_navigation.grid_columnconfigure((0, 1, 2), weight=1)
        self.menu_navigation.grid_rowconfigure((0, 1, 6), weight=1)

        self.title_label = ctk.CTkLabel(self.menu_navigation, font=self.font_title, text="PYTHON WORD", text_color="white")
        self.title_label.grid(column=0, row=0, padx=(80), pady=(15, 30), sticky="nsew", columnspan=3)

        self.github_icon = ctk.CTkButton(self.menu_navigation, image=github_icon, text="", fg_color="transparent", width=0,
                                         hover_color="#D78A1E",
                                         command=lambda: self.utils.open_website(self.github_url))
        self.github_icon.grid(column=0, row=1, padx=(0, 0), sticky="e")

        self.linkedin_icon = ctk.CTkButton(self.menu_navigation, image=linkedin_icon, text="", fg_color="transparent", width=0,
                                           hover_color="#D78A1E",
                                           command=lambda: self.utils.open_website(self.linkedin_url))
        self.linkedin_icon.grid(column=1, row=1, padx=(0, 0))

        self.site_icon = ctk.CTkButton(self.menu_navigation, image=website_icon, text="", fg_color="transparent", width=0,
                                       hover_color="#D78A1E", command=lambda: self.utils.open_website(self.site_url))
        self.site_icon.grid(column=2, row=1, padx=(0, 0), sticky="w")

        self.illustration_label = ctk.CTkButton(self.menu_navigation, width=0, image=illustration_image, text="", fg_color="transparent",  hover_color="#D78A1E",  command=lambda: self.utils.open_website(self.cursoemvideo_url))
        self.illustration_label.grid(column=0, row=6, padx=(10), pady=(60, 10), sticky="s", columnspan=3)

        
        self.word_frame.grid_columnconfigure((0, 1, 2), weight=1)



        self.world1_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world1_icon, fg_color="transparent", hover_color="#4C76D9", corner_radius=20)
        self.world1_btn.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.world2_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world2_icon, fg_color="transparent",  hover_color="#4C76D9", corner_radius=20)
        self.world2_btn.grid(column=1, row=0, padx=5, pady=5,sticky="nsew")

        self.world3_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world3_icon, fg_color="transparent",  hover_color="#4C76D9", corner_radius=20)
        self.world3_btn.grid(column=2, row=0, padx=5, pady=5,sticky="nsew")

    def show_exercises(self):
        self.title("Escolha o exercicio")

        self.word_frame.grid_remove()


        self.menu_navigation.grid_columnconfigure((0), weight=1)
        self.menu_navigation.grid_rowconfigure((1), weight=1)


        self.menu_navigation.configure(fg_color="#D78A1E", corner_radius=20, width=200, )
        self.menu_navigation.grid_configure(padx=5, pady=5)

        self.exercise_options.grid(row=0, column=1, padx=(10,10), pady=10, sticky="nsew")


        self.back_bt = ctk.CTkButton(self.menu_navigation, text="", width=1, image=back_icon, fg_color="transparent", hover_color="#95A2FC", corner_radius=10)
        self.back_bt.grid(column=0, row=0, pady=(10,0))

        self.word_img = ctk.CTkLabel(self.menu_navigation, text="", image=world1_icon, fg_color="transparent")
        self.word_img.grid(column=0, row=1, sticky="nsew")

        self.total_text = ctk.CTkLabel(self.menu_navigation,font=self.font_title, text="TOTAL\n30", fg_color="transparent", text_color="black")
        self.total_text.grid(column=0, row=2, sticky="s", pady=(0,50))


        for i in range(0,30):

            row = i // 4
            column = i % 4
    
            button = ctk.CTkButton(self.exercise_options, width=210, height=50,font=self.font_subtitle, corner_radius=5, text=f"EXERCÍCIO {i+1}", 
                                   hover_color="#FAB52F", fg_color="#D78A1E", text_color="BLACK", command=self.exercise_solution)
            button.grid(row=row, column=column, padx=5, pady=10)
    
    def exercise_solution(self):
        self.title("Responda o exercicio")

        self.grid_columnconfigure(1, weight=1)  # Coluna 1 vai expandir
        self.grid_rowconfigure((0,1), weight=1)

        self.menu_navigation.grid_configure(rowspan=2)

        self.total_text.grid_remove()
        self.exercise_options.grid_remove()
        self.word_frame.grid_remove()


        self.exercise_name = ctk.CTkLabel(self.menu_navigation, text="Exercicio 01", font=self.font_subtitle, width=180, height=50,  fg_color="#D78A1E", text_color="black", corner_radius=5)
        self.exercise_name.grid(column=0, row=2, pady=(5,5))


        self.show_solution_bt = ctk.CTkButton(self.menu_navigation, text="VER RESPOSTA", width=180,  height=50,font=self.font_body, fg_color="#171D23", hover_color="#95A2FC", corner_radius=5)
        self.show_solution_bt.grid(column=0, row=3, pady=(20,20))

        self.analyze_response  = ctk.CTkButton(self.menu_navigation, text="ANALISAR SUA\nRESPOSTA", width=180,  height=50, font=self.font_body, fg_color="#171D23", hover_color="#95A2FC", corner_radius=5)
        self.analyze_response.grid(column=0, row=4, pady=(5,10))

       

        texto = """crie um script python que leia o nome de uma pessoa e mostra uma mensagem de boas-vindas de acordo com o valor digitado"""
        self.exercise_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.exercise_label.configure(text=texto, corner_radius=20, font=self.font_subtitle, justify="left", wraplength=800)

        self.copy_code = ctk.CTkButton(self.solution_textbox, image=copy_icon, text="", width=0,  height=50, fg_color="transparent", hover_color="#95A2FC", corner_radius=5)
        self.copy_code.grid(row=0, column=0,  pady=(5,0), sticky="ne")


        self.solution_textbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.solution_textbox.insert("0.0", "Digite aqui o seu codigo:")






        