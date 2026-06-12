import subprocess
import sys
from pathlib import Path


def extract_vocals(audio_file):

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "demucs",
            audio_file
        ]
    )

    if result.returncode != 0:
        raise RuntimeError(
            "Falha ao executar Demucs."
        )

    song_name = Path(audio_file).stem

    return (
        f"separated/htdemucs/"
        f"{song_name}/vocals.wav"
    )