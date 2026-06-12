import ollama


def normalize_lyrics(text):

    prompt = f"""
Você receberá uma transcrição de música.

A música pode misturar idiomas.

Corrija apenas erros óbvios de reconhecimento.

Não invente versos.
Não complete trechos ausentes.
Preserve a estrutura da letra.

Retorne apenas a letra corrigida.

Texto:

{text}
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def translate_to_ptbr(text):

    prompt = f"""
Você receberá uma letra de música.

Regras:

- Traduza para português brasileiro.
- Preserve versos e refrões.
- Preserve quebras de linha.
- Preserve repetições.
- Não explique nada.
- Não adicione comentários.
- Retorne apenas a tradução.

Letra:

{text}
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]