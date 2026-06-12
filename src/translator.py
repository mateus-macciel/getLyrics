import ollama


def translate_to_ptbr(text):

    prompt = f"""
Traduza a letra abaixo para português brasileiro.

Regras:
- Preserve a estrutura dos versos.
- Preserve repetições.
- Não explique nada.
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