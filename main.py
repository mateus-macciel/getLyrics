import sys

from src.transcriber import transcribe
from src.translator import translate_to_ptbr
from src.exporter import save_txt, save_json


def main():

    if len(sys.argv) != 2:
        print("Uso:")
        print("python main.py musica.mp3")
        return

    music = sys.argv[1]

    print("Transcrevendo áudio...")

    lyrics = transcribe(music)

    print("Salvando letra original...")

    save_txt(
        lyrics,
        "lyrics_original.txt"
    )

    save_json(
        lyrics,
        "lyrics_original.json"
    )

    try:

        print("Traduzindo para PT-BR...")

        translated = translate_to_ptbr(
            lyrics
        )

        save_txt(
            translated,
            "lyrics_ptbr.txt"
        )

        save_json(
            translated,
            "lyrics_ptbr.json"
        )

        print("Tradução concluída.")

    except Exception as e:

        print(
            "Falha ao usar Ollama:"
        )

        print(e)

    print("Concluído.")


if __name__ == "__main__":
    main()