"""Script principal: coordina el flujo completo del proyecto.

Orden:
1. Cargar y limpiar los datos.
2. Separar predictores (X) y objetivo (y).
3. Dividir en entrenamiento, validación y prueba (60/20/20).
4. Entrenar cada modelo con entrenamiento y compararlos en validación.
5. Elegir el modelo con menor MAE de validación.
6. Reentrenar ese modelo solo con entrenamiento y evaluarlo en prueba una sola vez.

Uso:
    python scripts/download_data.py
    python train.py
"""

from sklearn.base import clone

from src.config import COLUMNAS_NUMERICAS_BASE, VARIABLES_DERIVADAS
from src.data_io import cargar_datos, limpiar_nulos, separar_variables_y_objetivo
from src.evaluation import (
    entrenar_y_evaluar_modelos,
    evaluar_en_prueba,
    seleccionar_mejor_modelo,
)
from src.models import obtener_modelos
from src.preprocessor import construir_pipeline_modelo
from src.splitter import dividir_train_valid_test

# El escalador recibe las columnas numéricas originales MÁS las derivadas
# (rooms_per_household, bedrooms_per_household). Si solo se pasan las base,
# el ColumnTransformer descarta las derivadas aunque features.py las cree.
# En el notebook se usaban todas las numéricas de X_train_feat.
COLUMNAS_NUMERICAS = COLUMNAS_NUMERICAS_BASE + VARIABLES_DERIVADAS


def construir_pipeline(modelo):
    """Arma un pipeline nuevo (variables + preprocesamiento + modelo).

    Se usa clone() para que cada pipeline reciba una copia sin entrenar
    del modelo y no se reutilice un objeto ya ajustado en otra etapa.
    """
    return construir_pipeline_modelo(clone(modelo), COLUMNAS_NUMERICAS)


def main() -> None:
    # 1 y 2. Carga, limpieza y separación de X e y
    datos = cargar_datos()
    datos_limpios = limpiar_nulos(datos)
    print(f"Filas originales: {len(datos):,} | sin nulos: {len(datos_limpios):,}")

    x, y = separar_variables_y_objetivo(datos_limpios)

    # 3. División 60/20/20
    x_train, x_valid, x_test, y_train, y_valid, y_test = dividir_train_valid_test(x, y)
    total = len(x)
    print(
        f"Entrenamiento: {len(x_train):,} ({len(x_train) / total:.0%}) | "
        f"Validación: {len(x_valid):,} ({len(x_valid) / total:.0%}) | "
        f"Prueba: {len(x_test):,} ({len(x_test) / total:.0%})"
    )

    # 4. Entrenar con entrenamiento y comparar en validación
    modelos = obtener_modelos()
    resultados = entrenar_y_evaluar_modelos(
        modelos=modelos,
        construir_pipeline=construir_pipeline,
        x_train=x_train,
        y_train=y_train,
        x_valid=x_valid,
        y_valid=y_valid,
    )

    print("\nTabla comparativa (entrenamiento y validación):")
    print(resultados.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

    # 5. Selección por validación (prueba todavía no se ha usado)
    mejor_modelo = seleccionar_mejor_modelo(resultados)
    print(f"\nModelo seleccionado por menor MAE de validación: {mejor_modelo}")

    # 6. Reentrenar solo con entrenamiento y evaluar en prueba una sola vez
    pipeline_final = construir_pipeline(modelos[mejor_modelo])
    pipeline_final.fit(x_train, y_train)
    metricas_prueba = evaluar_en_prueba(pipeline_final, x_test, y_test)

    print("\nEvaluación final en prueba:")
    print(f"MAE prueba:  {metricas_prueba['MAE']:,.2f} dólares")
    print(f"RMSE prueba: {metricas_prueba['RMSE']:,.2f} dólares")


if __name__ == "__main__":
    main()