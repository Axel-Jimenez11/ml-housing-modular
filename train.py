from src.config import COLUMNAS_NUMERICAS_BASE
from src.data_io import cargar_datos, limpiar_nulos, separar_variables_y_objetivo
from src.evaluation import (
    entrenar_y_evaluar_modelos,
    evaluar_en_prueba,
    seleccionar_mejor_modelo,
)
from src.models import obtener_modelos
from src.preprocessor import construir_pipeline_modelo
from src.splitter import dividir_train_valid_test


def main() -> None:
    datos = cargar_datos()
    datos_limpios = limpiar_nulos(datos)
    x, y = separar_variables_y_objetivo(datos_limpios)
    x_train, x_valid, x_test, y_train, y_valid, y_test = dividir_train_valid_test(x, y)

    modelos = obtener_modelos()

    def construir_pipeline(modelo):
        return construir_pipeline_modelo(modelo, COLUMNAS_NUMERICAS_BASE)

    resultados = entrenar_y_evaluar_modelos(
        modelos=modelos,
        construir_pipeline=construir_pipeline,
        x_train=x_train,
        y_train=y_train,
        x_valid=x_valid,
        y_valid=y_valid,
    )

    print("\nTabla comparativa (entrenamiento y validación):")
    print(resultados.to_string(index=False, float_format=lambda x: f"{x:,.2f}"))

    mejor_modelo = seleccionar_mejor_modelo(resultados)
    print(f"\nModelo seleccionado por menor MAE de validación: {mejor_modelo}")

    pipeline_final = construir_pipeline(modelos[mejor_modelo])
    pipeline_final.fit(x_train, y_train)
    metricas_prueba = evaluar_en_prueba(pipeline_final, x_test, y_test)

    print("\nEvaluación final en prueba:")
    print(f"MAE prueba: {metricas_prueba['MAE']:,.2f} dólares")
    print(f"RMSE prueba: {metricas_prueba['RMSE']:,.2f} dólares")


if __name__ == "__main__":
    main()
