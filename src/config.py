from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "housing"
DATA_FILE = DATA_DIR / "housing.csv"
DATA_URL = "https://raw.githubusercontent.com/IvTole/Intro_IA_ML_CUGDL/refs/heads/main/data/housing/housing.csv"

SEED = 42
TARGET = "median_house_value"
COLUMNA_CATEGORICA = "ocean_proximity"
COLUMNAS_NUMERICAS_BASE = [
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
]
VARIABLES_DERIVADAS = ["rooms_per_household", "bedrooms_per_household"]

TEST_SIZE = 0.20
VALID_SIZE_OF_DEV = 0.25
