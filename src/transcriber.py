from faster_whisper import WhisperModel


MODELS = {
    "fast": "small",
    "quality": "medium",
    "extreme": "large-v3"
}


def transcribe(audio_file, mode):

    model_name = MODELS[mode]

    print(
        f"Carregando modelo: "
        f"{model_name}"
    )

    model = WhisperModel(
        model_name,
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        audio_file,
        beam_size=15,
        vad_filter=False,
        condition_on_previous_text=False,
        multilingual=True
    )
    
    print(
        f"Idioma principal detectado: "
        f"{info.language}"
    )

    lines = []

    count = 0

    for segment in segments:

        count += 1

        print(
            f"[{segment.start:.2f}s -> "
            f"{segment.end:.2f}s] "
            f"{segment.text}"
        )

        lines.append(
            segment.text.strip()
        )

    print(
        f"Segmentos encontrados: "
        f"{count}"
    )

    return "\n".join(lines)