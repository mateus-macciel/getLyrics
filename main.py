import sys

from src.audio import extract_vocals
from src.transcriber import transcribe
from src.translator import translate_to_ptbr
from src.exporter import (
    save_txt,
    save_json
)


VALID_MODES = [
    "fast",
    "quality",
    "extreme"
]


def main():

    if len(sys.argv) < 2:

        print(
            "Uso:"
        )

        print(
            "python main.py "
            "musica.mp3"
        )

        print(
            "python main.py "
            "musica.mp3 quality"
        )

        return

    music = sys.argv[1]

    mode = (
        sys.argv[2]
        if len(sys.argv) >= 3
        else "quality"
    )

    if mode not in VALID_MODES:

        print(
            "Modo inválido."
        )

        return

    audio_source = music

    if mode == "extreme":

        print(
            "Extraindo vocais..."
        )

        audio_source = extract_vocals(
            music
        )

    print(
        "Transcrevendo..."
    )

    lyrics = transcribe(
        audio_source,
        mode
    )

    save_txt(
        lyrics,
        "lyrics_original.txt"
    )

    save_json(
        lyrics,
        "lyrics_original.json"
    )

    try:

        print(
            "Traduzindo..."
        )

        translated = (
            translate_to_ptbr(
                lyrics
            )
        )

        save_txt(
            translated,
            "lyrics_ptbr.txt"
        )

        save_json(
            translated,
            "lyrics_ptbr.json"
        )

    except Exception as e:

        print(
            "Ollama indisponível:"
        )

        print(e)

    print(
        "Concluído."
    )


if __name__ == "__main__":
    main()