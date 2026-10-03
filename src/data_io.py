import pandas as pd

from src.config import DATA_FILE, DATA_URL, TARGET


def cargar_datos() -> pd.DataFrame:
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de datos en {DATA_FILE}. "
            f"Ejecuta: python scripts/download_data.py para descargarlo desde {DATA_URL}."
        )
    return pd.read_csv(DATA_FILE)


def limpiar_nulos(tabla: pd.DataFrame) -> pd.DataFrame:
    return tabla.dropna().copy()


def separar_variables_y_objetivo(tabla: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    x = tabla.drop(columns=TARGET)
    y = tabla[TARGET]
    return x, y
