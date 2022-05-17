from pathlib import Path


def get_cwd() -> str:
    return Path(__file__).resolve(strict=True).parent.parent
