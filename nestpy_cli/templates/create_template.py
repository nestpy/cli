from pathlib import Path

def create_template(path: Path, content: str) -> None:
    with open(path, "w") as f:
        f.write(content)
