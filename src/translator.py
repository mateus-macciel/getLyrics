import ollama

def normalize_lyrics(text):

    prompt = f"""
Você receberá uma transcrição de música.

A música pode misturar idiomas.

Corrija apenas erros óbvios de reconhecimento.

Não invente versos.
Não complete trechos ausentes.

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