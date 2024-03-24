import customtkinter as ctk
from src.utils.utils import Utilities
from src.utils.questions import world_one, world_two, world_three
from src.views.icones import *
from CTkXYFrame import *
import openai
from dotenv import load_dotenv

import os
import threading
import tkinter as tk
load_dotenv()
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

        self.response_thread = None

        self.current_world = []
        self.list_message = []

        openai.api_key = os.environ["key_api"]

        self.analysis_instruction_gpt = """Por favor, analise o código Python abaixo e a questão fornecida. Caso encontre algum erro, liste-os detalhadamente, explicando onde estão os equívocos:
- Se o código estiver correto e atender às exigências da pergunta, retorne uma mensagem de confirmação.
- Caso haja erros, liste-os em tópicos para que o usuário possa corrigi-los de forma adequada.
- Se o usuário enviar algo em branco ou perguntar qualquer coisa fora do contexto, solicite gentilmente que ele forneça o código novamente, pois está vazio.

A questão que o usuário deve responder é a seguinte:..."""




        self.response_instruction = """Por favor, analise esta questão e responda retornando apenas a resposta em python nao precisa adicionar comentarios aspas, caracteres especiais ou explicações."""

         

        self.menu_view()
        self.mainloop()

    def menu_view(self):
        
        self.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.grid_columnconfigure(1, weight=1)  # Coluna 1 vai expandir
        self.grid_rowconfigure(0, weight=1)

        self.title("Escolha o Mundo")

        self.menu_navigation= ctk.CTkFrame(self, width=500, corner_radius=0, fg_color="#171D23")
        self.menu_navigation.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.menu_navigation.grid_columnconfigure((0, 1, 2), weight=1)
        self.menu_navigation.grid_rowconfigure((6), weight=1)


        self.word_frame = ctk.CTkFrame(self, width=100, fg_color="#D78A1E", corner_radius=20)
        self.word_frame.grid(row=0, column=1, padx=(10,10), pady=10, sticky="nsew")
        self.word_frame.grid_columnconfigure((0, 1, 2), weight=1)


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

        self.cursoemvideo_img = ctk.CTkButton(self.menu_navigation, width=0, image=cursoemvideo_image, text="", fg_color="transparent",  hover_color="#D78A1E",  command=lambda: self.utils.open_website(self.cursoemvideo_url))
        self.cursoemvideo_img.grid(column=0, row=6, padx=(10), pady=(60, 10), sticky="s", columnspan=3)

        
        
        self.world1_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world1_icon, fg_color="transparent", hover_color="#4C76D9", corner_radius=20, command=lambda: self.show_questions(world_one))
        self.world1_btn.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.world2_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world2_icon, fg_color="transparent",  hover_color="#4C76D9", corner_radius=20, command=lambda: self.show_questions(world_two))
        self.world2_btn.grid(column=1, row=0, padx=5, pady=5,sticky="nsew")

        self.world3_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world3_icon, fg_color="transparent",  hover_color="#4C76D9", corner_radius=20, command=lambda: self.show_questions(world_three))
        self.world3_btn.grid(column=2, row=0, padx=5, pady=5,sticky="nsew")

    def show_questions(self, world):
         

        self.current_world = world

        self.utils.restart_interface(self.menu_navigation)

        self.word_frame.grid_remove()



        self.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.grid_columnconfigure(1, weight=1)  # Coluna 1 vai expandir
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)


        self.menu_navigation.configure(fg_color="#D78A1E", corner_radius=20, width=200, )
        self.menu_navigation.grid_columnconfigure((0), weight=1)
        self.menu_navigation.grid_rowconfigure((0), weight=1)
        self.menu_navigation.grid_configure(rowspan=1, padx=5, pady=5)


        self.title("Escolha o exercicio")
        
        self.back_bt = ctk.CTkButton(self.menu_navigation, text="", width=1, image=back_icon, fg_color="transparent", hover_color="#95A2FC", corner_radius=10, command=lambda: self.toggle_view(True))
        self.back_bt.grid(column=0, row=0, pady=(10,0))

        self.word_img = ctk.CTkLabel(self.menu_navigation, text="", image=world1_icon, fg_color="transparent")
        self.word_img.grid(column=0, row=1, sticky="nsew")

        self.exercise_count_label = ctk.CTkLabel(self.menu_navigation,font=self.font_title, text=f"TOTAL\n{len(self.current_world)}", fg_color="transparent", text_color="black")
        self.exercise_count_label.grid(column=0, row=2, sticky="s", pady=(0,50))


        self.questions_options = CTkXYFrame(self, width=100, fg_color="#FFF6E9", corner_radius=20)
        self.questions_options.grid(row=0, column=1, padx=(10,10), pady=10, sticky="nsew")


        for i, question in enumerate(world):
            
            row = i // 4
            column = i % 4
    
            button = ctk.CTkButton(self.questions_options, width=210, height=50,font=self.font_subtitle, corner_radius=5, text=f"EXERCÍCIO {i+1}", 
                                   hover_color="#FAB52F", fg_color="#D78A1E", text_color="BLACK",command=lambda idx=i, q=question: self.questions_solution(idx+1, q))
            button.grid(row=row, column=column, padx=5, pady=10)
    
    def questions_solution(self, index, question):
       

        self.exercise_count_label.grid_remove()
        self.questions_options.grid_remove()


        self.grid_rowconfigure((0,1), weight=1)

        self.menu_navigation.grid_rowconfigure(4, weight=1)
        self.menu_navigation.grid_configure(rowspan=2)
        self.back_bt.configure(command=lambda: self.toggle_view(False))


        self.title("Responda o exercicio")

        self.questions_name = ctk.CTkLabel(self.menu_navigation, text=f"Exercicio {index}", font=self.font_subtitle, width=180, height=50,  fg_color="#D78A1E", text_color="black", corner_radius=5)
        self.questions_name.grid(column=0, row=2, pady=(5,5))




        self.analyze_response  = ctk.CTkButton(self.menu_navigation, text="ENVIAR SUA\nRESPOSTA", width=180,  height=50, font=self.font_body, fg_color="#171D23", hover_color="#95A2FC", corner_radius=5, command=self.send_response)
        self.analyze_response.grid(column=0, row=3, pady=(5,10))


        self.show_solution_bt = ctk.CTkButton(self.menu_navigation, text="VER RESPOSTA", width=180,  height=50,font=self.font_body, fg_color="#171D23", hover_color="#95A2FC", corner_radius=5, command=self.see_solution)
        self.show_solution_bt.grid(column=0, row=4, pady=(5), sticky="S")


        self.questions_label = ctk.CTkLabel(self, fg_color="#171D23", text_color="#4C76D9", text=question, corner_radius=20, font=self.font_subtitle, justify="left", wraplength=800)
        self.questions_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


        self.copy_question_bt = ctk.CTkButton(self.questions_label, image=copy_icon, text="", width=0,  height=50, fg_color="transparent", hover=False, corner_radius=10, command=self.copy_question)
        self.copy_question_bt.grid(row=0, column=0, padx=(0,30), pady=(8,0), sticky="ne")


        self.solution_textbox = ctk.CTkTextbox(self, width=100, fg_color="#23272D", font=self.font_code, corner_radius=20, text_color="white")
        self.solution_textbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.solution_textbox.insert("0.0", "Digite aqui o seu codigo:")
        self.solution_textbox.bind("<FocusIn>", self.remove_placeholder)

        self.clear_textbox_bt = ctk.CTkButton(self.solution_textbox, image=delete_icon, text="", width=0,  height=50, fg_color="transparent", hover=False, corner_radius=10, command=self.clear_textbox)
        self.clear_textbox_bt.grid(row=0, column=0, padx=(0), pady=(8,0), sticky="ne")
        


 
    def toggle_view(self, show_menu=True):
        # Limpa completamente a interface
        self.utils.restart_interface(self)

        if show_menu:
            self.menu_view()
              # Exibe a visualização do menu
        else:
            self.menu_view()
            self.show_questions(self.current_world)

    def remove_placeholder(self, event):
        """Remove o texto de placeholder quando a caixa de texto ganha foco."""
        if self.solution_textbox.get("1.0", "end-1c") == "Digite aqui o seu codigo:":
            self.solution_textbox.delete("1.0", "end")

    def send_response(self):
        # Verifica se há uma thread de resposta em andamento e aguarde sua conclusão antes de iniciar uma nova
        if self.response_thread and self.response_thread.is_alive():
            self.utils.msgbox("Aviso", "A análise anterior ainda está em andamento. Por favor, aguarde a conclusão.", 0)
            return

        # Obtenha o conteúdo da caixa de texto de resposta do usuário
        response_user = self.solution_textbox.get("1.0", "end-1c")
        message = self.analysis_instruction_gpt + "\nQuestão: " + self.questions_label._text + "\nE a resposta do usuário foi:" + f'\n{response_user}'

        # Inicie uma nova thread para chamar a função send_message
        self.response_thread = threading.Thread(target=self.send_message, args=(message,))
        self.response_thread.start()

        self.solution_textbox.insert("end", "\n\nSua resposta foi enviada para análise\naguarde um momento...")

    def see_solution(self):
        # Verifica se há uma thread de resposta em andamento e aguarde sua conclusão antes de iniciar uma nova
        if self.response_thread and self.response_thread.is_alive():
            self.utils.msgbox("Aviso", "A análise anterior ainda está em andamento. Por favor, aguarde a conclusão.", 0)
            return

        self.solution_textbox.insert("end", "\n\nCarregando a resposta, aguarde um momento...")

        message = self.questions_label._text + self.response_instruction 

        # Inicie uma nova thread para chamar a função send_message
        self.response_thread = threading.Thread(target=self.send_message, args=(message,))
        self.response_thread.start()

    def send_message(self, message):
        try:
            self.list_message.append({"role": "user", "content": message})

            # Chama a API OpenAI para análise da mensagem
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.list_message,
            )

            # Verifica se a resposta foi recebida corretamente
            if resposta and 'choices' in resposta and resposta['choices']:
                content = resposta['choices'][0]['message'].get('content')
                if content:
                    # Atualiza o textbox com a resposta na thread principal
                    self.after(0, self.update_textbox, content)
                else:
                    # A resposta está vazia ou em um formato inesperado
                    self.utils.msgbox("Erro", "Não foi possível obter uma resposta válida do modelo.", 0)
            else:
                # Não foi possível obter uma resposta do modelo
                self.utils.msgbox("Erro", "Não foi possível obter uma resposta do modelo.", 0)
        except Exception as e:
            # Trata qualquer exceção que possa ocorrer durante o processo
            print("Erro ao enviar mensagem:", e)
            self.utils.msgbox("Erro", "Ocorreu um erro ao enviar a mensagem.", 0)
        finally:
            # Libera recursos e finaliza a thread
            self.response_thread = None

    def update_textbox(self, content):
        self.solution_textbox.insert("end", f"\n\n{content}")
        
    def clear_textbox(self):
        self.solution_textbox.delete("1.0", "end")


    def copy_question(self):
        self.clipboard_clear()
        self.clipboard_append(self.questions_label._text)
        self.utils.msgbox("Copiar", "Texto copiado para sua area de transferencia com sucesso", 0)
        