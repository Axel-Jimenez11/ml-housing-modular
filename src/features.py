import pandas as pd
from sklearn.preprocessing import FunctionTransformer


def crear_variables(tabla: pd.DataFrame) -> pd.DataFrame:
    resultado = tabla.copy()
    divisor = resultado["households"].replace(0, 1)
    resultado["rooms_per_household"] = resultado["total_rooms"] / divisor
    resultado["bedrooms_per_household"] = resultado["total_bedrooms"] / divisor
    return resultado


def construir_transformador_variables() -> FunctionTransformer:
    return FunctionTransformer(crear_variables)
