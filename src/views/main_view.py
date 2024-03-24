from CTkXYFrame import *
import customtkinter as ctk
from src.views.icones import *
from src.utils.utils import Utilities
from src.controllers import main_controller
from src.utils.questions import WORLD_ONE, WORLD_TWO, WORLD_THREE




class MainView(ctk.CTk):
    def __init__(self):
        # Chama o método de inicialização da classe pai para configurar a janela principal da aplicação
        super().__init__()

        # Define diferentes fontes para uso na interface
        self.FONT_TITLE = ("Fixedsys", 50, "bold")
        self.FONT_SUBTITLE = ("Fixedsys", 22,)
        self.FONT_BODY = ("Fixedsys", 20,)
        self.FONT_CODE = ("Consolas", 20,)

        # Define URLs para perfis de redes sociais e site do curso em video
        self.LINKEDIN_URL = "https://linkedin.com/in/luis-henrique-281b97186"
        self.GITHUB_URL = "https://github.com/Luis-lhgdf"
        self.SITE_URL = "https://luis-lhgdf.github.io/portfolio/"
        self.CURSOEMVIDEO_URL = "https://www.cursoemvideo.com/curso/python-3-mundo-1/"



        # Inicializa listas para armazenar o mundo atual e mensagens da interface
        self.current_world = []
        

        # Cria uma instância da classe Utilities para usar em toda a aplicação
        self.utils = Utilities()
        self.controller = main_controller.Controller(self, self.utils)


        # Configura a geometria e as cores padrão da interface
        self.geometry("1200x650")
        self.configure(fg_color="#558FAD")

        # Configurando função de fechamento do sistema
        self.protocol("WM_DELETE_WINDOW", self.exit)

        # Chama o método para criar a visualização do menu principal da aplicação
        self.menu_view()

        # Inicia o loop principal da interface
        self.mainloop()
     
    def menu_view(self):
        # Configuração da grade para expansão e redimensionamento dos widgets
        self.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.grid_columnconfigure(1, weight=1)  # Coluna 1 vai expandir
        self.grid_rowconfigure(0, weight=1)     # Linha 0 vai expandir

        # Define o título da janela
        self.title("Escolha o Mundo")

        # Criação do frame para navegação do menu
        self.menu_navigation = ctk.CTkFrame(self, width=500, corner_radius=0, fg_color="#171D23")
        self.menu_navigation.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.menu_navigation.grid_columnconfigure((0, 1, 2), weight=1)
        self.menu_navigation.grid_rowconfigure((6), weight=1)

        # Criação do frame para os botões de seleção de mundo
        self.word_frame = ctk.CTkFrame(self, width=100, fg_color="#D78A1E", corner_radius=20)
        self.word_frame.grid(row=0, column=1, padx=(10, 10), pady=10, sticky="nsew")
        self.word_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Label do título do menu
        self.title_label = ctk.CTkLabel(self.menu_navigation, font=self.FONT_TITLE, text="PYTHON WORD", text_color="white")
        self.title_label.grid(column=0, row=0, padx=(80), pady=(15, 30), sticky="nsew", columnspan=3)

        # Botões de redes sociais e sites
        self.github_icon = ctk.CTkButton(self.menu_navigation, image=github_icon, text="", fg_color="transparent", width=0,
                                         hover_color="#D78A1E",
                                         command=lambda: self.utils.open_website(self.GITHUB_URL))
        self.github_icon.grid(column=0, row=1, padx=(0, 0), sticky="e")

        self.linkedin_icon = ctk.CTkButton(self.menu_navigation, image=linkedin_icon, text="", fg_color="transparent", width=0,
                                           hover_color="#D78A1E",
                                           command=lambda: self.utils.open_website(self.LINKEDIN_URL))
        self.linkedin_icon.grid(column=1, row=1, padx=(0, 0))

        self.site_icon = ctk.CTkButton(self.menu_navigation, image=website_icon, text="", fg_color="transparent", width=0,
                                       hover_color="#D78A1E", command=lambda: self.utils.open_website(self.SITE_URL))
        self.site_icon.grid(column=2, row=1, padx=(0, 0), sticky="w")

        # Botão de link para o curso em vídeo
        self.cursoemvideo_img = ctk.CTkButton(self.menu_navigation, width=0, image=cursoemvideo_image, text="", fg_color="transparent",  hover_color="#D78A1E",  command=lambda: self.utils.open_website(self.CURSOEMVIDEO_URL))
        self.cursoemvideo_img.grid(column=0, row=6, padx=(10), pady=(60, 10), sticky="s", columnspan=3)

        # Botões para selecionar os mundos de exercícios
        self.world1_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world1_icon, fg_color="transparent", hover_color="#4C76D9", corner_radius=20, command=lambda: self.show_questions(WORLD_ONE))
        self.world1_btn.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.world2_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world2_icon, fg_color="transparent",  hover_color="#4C76D9", corner_radius=20, command=lambda: self.show_questions(WORLD_TWO))
        self.world2_btn.grid(column=1, row=0, padx=5, pady=5,sticky="nsew")

        self.world3_btn = ctk.CTkButton(self.word_frame, width=0, text="", image=world3_icon, fg_color="transparent",  hover_color="#4C76D9", corner_radius=20, command=lambda: self.show_questions(WORLD_THREE))
        self.world3_btn.grid(column=2, row=0, padx=5, pady=5,sticky="nsew")

    def show_questions(self, world):
        # Define o mundo atual
        self.current_world = world

        # Reinicia a interface do menu de navegação
        self.utils.restart_interface(self.menu_navigation)

        # Remove o frame de seleção de mundo
        self.word_frame.grid_remove()

        # Configura a grade para expansão e redimensionamento dos widgets
        self.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.grid_columnconfigure(1, weight=1)  # Coluna 1 vai expandir
        self.grid_rowconfigure(0, weight=1)     # Linha 0 vai expandir
        self.grid_rowconfigure(1, weight=0)     # Linha 1 não se expandirá

        # Configuração do menu de navegação
        self.menu_navigation.configure(fg_color="#D78A1E", corner_radius=20, width=200)
        self.menu_navigation.grid_columnconfigure((0), weight=1)
        self.menu_navigation.grid_rowconfigure((0), weight=1)
        self.menu_navigation.grid_configure(rowspan=1, padx=5, pady=5)

        # Define o título da janela para a seleção de exercícios
        self.title("Escolha o exercicio")
        
        # Cria o botão de retorno ao menu principal
        self.back_bt = ctk.CTkButton(self.menu_navigation, text="", width=1, image=back_icon, fg_color="transparent", hover_color="#95A2FC", corner_radius=10, command=lambda: self.toggle_view(True))
        self.back_bt.grid(column=0, row=0, pady=(10, 0))

        # Cria um label para exibir a imagem do mundo selecionado
        self.word_img = ctk.CTkLabel(self.menu_navigation, text="", image=world1_icon, fg_color="transparent")
        self.word_img.grid(column=0, row=1, sticky="nsew")

        # Exibe o número total de exercícios disponíveis para o mundo selecionado
        self.exercise_count_label = ctk.CTkLabel(self.menu_navigation, font=self.FONT_TITLE, text=f"TOTAL\n{len(self.current_world)}", fg_color="transparent", text_color="black")
        self.exercise_count_label.grid(column=0, row=2, sticky="s", pady=(0, 50))

        # Cria um frame para os botões de seleção de exercícios
        self.questions_options = CTkXYFrame(self, width=100, fg_color="#FFF6E9", corner_radius=20)
        self.questions_options.grid(row=0, column=1, padx=(10, 10), pady=10, sticky="nsew")

        # Cria botões para cada exercício disponível no mundo selecionado
        for i, question in enumerate(world):
            row = i // 4
            column = i % 4
            button = ctk.CTkButton(self.questions_options, width=210, height=50, font=self.FONT_SUBTITLE, corner_radius=5, text=f"EXERCÍCIO {i+1}", 
                                   hover_color="#FAB52F", fg_color="#D78A1E", text_color="BLACK", command=lambda idx=i, q=question: self.questions_solution(idx+1, q))
            button.grid(row=row, column=column, padx=5, pady=10)
    
    def questions_solution(self, index, question):
        # Remove a contagem de exercícios e as opções de seleção de exercícios
        self.exercise_count_label.grid_remove()
        self.questions_options.grid_remove()

        # Configura a grade para expansão das duas linhas
        self.grid_rowconfigure((0, 1), weight=1)

        # Configura o menu de navegação para expandir a quarta linha
        self.menu_navigation.grid_rowconfigure(4, weight=1)
        self.menu_navigation.grid_configure(rowspan=2)
        
        # Configura o botão de retorno ao menu principal para chamar a função toggle_view para voltar à seleção de mundo
        self.back_bt.configure(command=lambda: self.toggle_view(False))

        # Define o título da janela para a resolução do exercício
        self.title("Responda o exercicio")

        # Cria um label para exibir o número e título do exercício
        self.questions_name = ctk.CTkLabel(self.menu_navigation, text=f"Exercicio {index}", font=self.FONT_SUBTITLE, width=180, height=50, fg_color="#D78A1E", text_color="black", corner_radius=5)
        self.questions_name.grid(column=0, row=2, pady=(5, 5))

        # Cria botões para enviar a resposta e visualizar a solução
        self.analyze_response = ctk.CTkButton(self.menu_navigation, text="ENVIAR SUA\nRESPOSTA", width=180, height=50, font=self.FONT_BODY, fg_color="#171D23", hover_color="#95A2FC", corner_radius=5, command=self.controller.send_response)
        self.analyze_response.grid(column=0, row=3, pady=(5, 10))

        self.show_solution_bt = ctk.CTkButton(self.menu_navigation, text="VER RESPOSTA", width=180, height=50, font=self.FONT_BODY, fg_color="#171D23", hover_color="#95A2FC", corner_radius=5, command=self.controller.see_solution)
        self.show_solution_bt.grid(column=0, row=4, pady=(5), sticky="S")

        # Exibe o enunciado do exercício
        self.questions_label = ctk.CTkLabel(self, fg_color="#171D23", text_color="#4C76D9", text=question, corner_radius=20, font=self.FONT_SUBTITLE, justify="left", wraplength=800)
        self.questions_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Cria um botão para copiar o enunciado do exercício
        self.copy_question_bt = ctk.CTkButton(self.questions_label, image=copy_icon, text="", width=0, height=50, fg_color="transparent", hover=False, corner_radius=10, command=self.controller.copy_question)
        self.copy_question_bt.grid(row=0, column=0, padx=(0, 30), pady=(8, 0), sticky="ne")

        # Cria uma caixa de texto para a resposta do usuário
        self.solution_textbox = ctk.CTkTextbox(self, width=100, fg_color="#23272D", font=self.FONT_CODE, corner_radius=20, text_color="white")
        self.solution_textbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.solution_textbox.insert("0.0", "Digite aqui o seu codigo:")
        self.solution_textbox.bind("<FocusIn>", self.remove_placeholder)

        # Cria um botão para limpar a caixa de texto
        self.clear_textbox_bt = ctk.CTkButton(self.solution_textbox, image=delete_icon, text="", width=0, height=50, fg_color="transparent", hover=False, corner_radius=10, command=self.controller.clear_textbox)
        self.clear_textbox_bt.grid(row=0, column=0, padx=(0), pady=(8, 0), sticky="ne")
        
    def toggle_view(self, show_menu=True):
        # Limpa completamente a interface
        self.utils.restart_interface(self)

        # Verifica se deve exibir o menu principal ou a seleção de exercícios
        if show_menu:
            self.menu_view()
            # Exibe a visualização do menu principal
        else:
            self.menu_view()
            # Exibe a seleção de exercícios do mundo atual
            self.show_questions(self.current_world)

    def remove_placeholder(self, event):
        """Remove o texto de placeholder quando a caixa de texto ganha foco."""
        if self.solution_textbox.get("1.0", "end-1c") == "Digite aqui o seu codigo:":
            # Verifica se o texto na caixa de texto é o placeholder e remove-o se for
            self.solution_textbox.delete("1.0", "end")

    def exit(self):
        resp = self.utils.msgbox("SAIR", "Deseja realmente encerrar o sistema?", 4)
        if resp == 6:
            self.destroy()

