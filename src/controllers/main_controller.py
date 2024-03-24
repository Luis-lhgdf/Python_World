import os
import openai
import threading
from dotenv import load_dotenv
from src.utils.utils import Utilities
from src.utils.instruction import ANALYSIS_INSTRUCTION_GPT, RESPONSE_INSTRUCTION

load_dotenv()

class Controller:
    def __init__(self, view, utils):
        self.view = view
        self.utils = utils
        openai.api_key = os.environ["KEY_API"]

        self.list_message = []

        # Inicializa uma variável para a thread de resposta da análise da OpenAI
        self.response_thread = None

    def send_response(self):
        # Verifica se há uma thread de resposta em andamento e aguarda sua conclusão antes de iniciar uma nova
        if self.response_thread and self.response_thread.is_alive():
            # Exibe uma mensagem de aviso se a análise anterior ainda estiver em andamento
            self.utils.msgbox("Aviso", "A análise anterior ainda está em andamento. Por favor, aguarde a conclusão.", 0)
            return

        # Obtém o conteúdo da caixa de texto de resposta do usuário
        response_user = self.view.solution_textbox.get("1.0", "end-1c")
        message = ANALYSIS_INSTRUCTION_GPT + "\nQuestão: " + self.view.questions_label._text + "\nE a resposta do usuário foi:" + f'\n{response_user}'

        # Inicia uma nova thread para chamar a função send_message
        self.response_thread = threading.Thread(target=self.send_message, args=(message,))
        self.response_thread.start()

        # Insere uma mensagem indicando que a resposta foi enviada para análise
        self.view.solution_textbox.insert("end", "\n\nSua resposta foi enviada para análise\naguarde um momento...")

    def see_solution(self):
        # Verifica se há uma thread de resposta em andamento e aguarde sua conclusão antes de iniciar uma nova
        if self.response_thread and self.response_thread.is_alive():
            self.utils.msgbox("Aviso", "A análise anterior ainda está em andamento. Por favor, aguarde a conclusão.", 0)
            return

        self.view.solution_textbox.insert("end", "\n\nCarregando a resposta, aguarde um momento...")

        message = self.view.questions_label._text + RESPONSE_INSTRUCTION

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
            print(resposta)
            # Verifica se a resposta foi recebida corretamente
            if resposta and 'choices' in resposta and resposta['choices']:
                content = resposta['choices'][0]['message'].get('content')
                if content:
                    # Atualiza o textbox com a resposta na thread principal
                    self.view.after(0, self.update_textbox, content)
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
        # Atualiza a caixa de texto com o conteúdo fornecido
        self.view.solution_textbox.insert("end", f"\n\n{content}")
        
    def clear_textbox(self):
        # Limpa o conteúdo da caixa de texto
        self.view.solution_textbox.delete("1.0", "end")

    def copy_question(self):
        # Copia o texto da questão para a área de transferência
        self.view.clipboard_clear()
        self.view.clipboard_append(self.view.questions_label._text)
        # Exibe uma mensagem informando que o texto foi copiado com sucesso
        self.utils.msgbox("Copiar", "Texto copiado para sua área de transferência com sucesso", 0)

