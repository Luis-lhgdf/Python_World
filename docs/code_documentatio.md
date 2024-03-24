# Documentação do Código

## Introdução

Este código Python faz parte de um projeto com propósito acadêmico e nostálgico, inspirado nos cursos de Python do Canal Curso em Vídeo com Gustavo Guanabara. O projeto visa permitir aos usuários relembrar os exercícios dos "Mundos" 1, 2 e 3 do curso, bem como receber correções automáticas através da integração com a API da OpenAI.

## Funcionalidades Principais

O código oferece as seguintes funcionalidades:

1. **Escolha do Mundo**: Os usuários podem escolher entre os "Mundos" 1, 2 e 3 do curso, clicando nos respectivos botões na interface gráfica.
2. **Visualização dos Exercícios**: Após escolher um mundo, os exercícios correspondentes a esse mundo são exibidos na interface.
3. **Resposta e Correção Automática**: Os usuários podem responder aos exercícios através de uma caixa de texto na interface. As respostas são então enviadas para a API da OpenAI para correção automática.
4. **Visualização da Solução**: Além da correção automática, os usuários podem visualizar a solução dos exercícios.

## Dependências Externas

- `customtkinter`: Uma biblioteca personalizada de Tkinter com recursos adicionais.
- `openai`: Uma biblioteca para interagir com a API da OpenAI.
- `dotenv`: Para carregar variáveis de ambiente a partir de um arquivo `.env`.

## Estrutura do Código

O código está estruturado da seguinte forma:

- **Classe `MainView`**: Responsável pela interface gráfica principal e interação com o usuário.

  - **Métodos**:
    - ... (listar os principais métodos e suas funcionalidades)

- **Outras Classes e Funções Auxiliares**:
  - `Utilities`: Contém funções utilitárias para interações diversas, como abrir URLs.
  - `CTkXYFrame`: Uma classe personalizada para criar frames com layouts específicos.

## Uso

1. Certifique-se de ter as dependências instaladas no ambiente Python.
2. Configure as variáveis de ambiente necessárias, especialmente a chave da API da OpenAI.
3. Execute o código Python.
4. Escolha o mundo desejado e responda aos exercícios conforme solicitado.
