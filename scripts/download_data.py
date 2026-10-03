import urllib.request

from src.config import DATA_DIR, DATA_FILE, DATA_URL


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(DATA_URL, DATA_FILE)
    print(f"Datos descargados en: {DATA_FILE}")


if __name__ == "__main__":
    main()
