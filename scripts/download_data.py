import sys
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config import DATA_DIR, DATA_FILE, DATA_URL


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(DATA_URL, DATA_FILE)
    print(f"Datos descargados en: {DATA_FILE}")


if __name__ == "__main__":
    main()
