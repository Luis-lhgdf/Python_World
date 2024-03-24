ANALYSIS_INSTRUCTION_GPT = """Por favor, analise o código Python abaixo e a questão fornecida. Caso encontre algum erro, liste-os detalhadamente, explicando onde estão os equívocos:
- Se o código estiver correto e atender às exigências da pergunta, retorne uma mensagem de confirmação.
- Caso haja erros, liste-os em tópicos para que o usuário possa corrigi-los de forma adequada.
- Se o usuário enviar algo em branco ou perguntar qualquer coisa fora do contexto, solicite gentilmente que ele forneça o código novamente, pois está vazio.

A questão que o usuário deve responder é a seguinte:..."""


RESPONSE_INSTRUCTION = """Por favor, analise esta questão e responda retornando apenas a resposta em python nao precisa adicionar comentarios aspas, caracteres especiais ou explicações."""
