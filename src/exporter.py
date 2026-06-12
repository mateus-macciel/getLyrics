import json
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_txt(content, filename):

    with open(
        OUTPUT_DIR / filename,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)


def save_json(content, filename):

    with open(
        OUTPUT_DIR / filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {"lyrics": content},
            f,
            ensure_ascii=False,
            indent=4
        )