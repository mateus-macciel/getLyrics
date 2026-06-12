from faster_whisper import WhisperModel

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)


def transcribe(audio_file):

    segments, info = model.transcribe(
        audio_file,
        beam_size=10,
        vad_filter=False,
        condition_on_previous_text=True
    )

    print(f"Idioma detectado: {info.language}")

    lines = []

    count = 0

    for segment in segments:
        count += 1

        print(
            f"[{segment.start:.2f}s -> {segment.end:.2f}s] "
            f"{segment.text}"
        )

        lines.append(segment.text.strip())

    print(f"Segmentos encontrados: {count}")

    return "\n".join(lines)