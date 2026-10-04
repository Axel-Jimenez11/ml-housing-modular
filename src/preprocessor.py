from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import COLUMNA_CATEGORICA
from src.features import construir_transformador_variables


def construir_preprocesador(columnas_numericas: list[str]) -> ColumnTransformer:
    return ColumnTransformer(
        [
            ("numericas", StandardScaler(), columnas_numericas),
            (
                "categoricas",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                [COLUMNA_CATEGORICA],
            ),
        ]
    )


def construir_pipeline_modelo(modelo, columnas_numericas: list[str]) -> Pipeline:
    preprocesador = construir_preprocesador(columnas_numericas)
    return Pipeline(
        [
            ("variables", construir_transformador_variables()),
            ("preprocesamiento", preprocesador),
            ("modelo", modelo),
        ]
    )
