# Documentação do Código

## Introdução

Este código Python faz parte de um projeto com propósito acadêmico e nostálgico, inspirado nos cursos de Python do Canal Curso em Vídeo com Gustavo Guanabara. O projeto visa permitir aos usuários relembrar os exercícios dos "Mundos" 1, 2 e 3 do curso, bem como receber correções automáticas através da integração com a API da OpenAI.

## Funcionalidades Principais

O código oferece as seguintes funcionalidades:

- **Escolha do Mundo:** Os usuários podem escolher entre os "Mundos" 1, 2 e 3 do curso, clicando nos respectivos botões na interface gráfica.
- **Visualização dos Exercícios:** Após escolher um mundo, os exercícios correspondentes a esse mundo são exibidos na interface.
- **Resposta e Correção Automática:** Os usuários podem responder aos exercícios através de uma caixa de texto na interface. As respostas são então enviadas para a API da OpenAI para correção automática.

## Dependências Externas

- `customtkinter`: Uma biblioteca personalizada de Tkinter com recursos adicionais.
- `openai`: Uma biblioteca para interagir com a API da OpenAI.
- `dotenv`: Para carregar variáveis de ambiente a partir de um arquivo .env.

## Estrutura do Código

O código está estruturado da seguinte forma:

### Classe MainView

Responsável pela interface gráfica principal e interação com o usuário.

#### Métodos

- `__init__`: Inicializa a interface e configurações iniciais.
- `menu_view`: Exibe o menu inicial com opções de escolha de mundo.
- `show_questions`: Exibe os exercícios correspondentes ao mundo escolhido.
- `questions_solution`: Exibe um exercício específico para que o usuário responda.
- `toggle_view`: Alterna entre a visualização do menu e dos exercícios.
- `remove_placeholder`:Remove o placehold do textbox

### Classe Controller

Responsável pela lógica de controle e comunicação entre a interface e a API da OpenAI.

#### Métodos

- `__init__`: Inicializa o controlador com referências para a visualização e utilitários.
- `send_response`: Envia a resposta do usuário para correção automática.
- `see_solution`: Permite ao usuário ver a solução do exercício.
- `send_message`: Envia a mensagem para a API da OpenAI para correção automática.
- `update_textbox`: Atualiza a caixa de texto com o conteúdo recebido.
- `clear_textbox`: Limpa o conteúdo da caixa de texto.
- `copy_question`: Copia o enunciado do exercício para a área de transferência.

### Outras Classes e Funções Auxiliares

- `Utilities`: Contém funções utilitárias para interações diversas, como abrir URLs.
- `CTkXYFrame`: Uma classe personalizada para criar frames com layouts específicos. (clone do github, link: https://github.com/Akascape/CTkXYFrame)

## Variáveis de Ambiente

O código faz uso da biblioteca dotenv para carregar variáveis de ambiente a partir de um arquivo .env, especialmente a chave da API da OpenAI.

## Uso

1. Certifique-se de ter as dependências instaladas no ambiente Python.
2. Configure as variáveis de ambiente necessárias, especialmente a chave da API da OpenAI.
3. Execute o código Python.
4. Escolha o mundo desejado e responda aos exercícios conforme solicitado.
