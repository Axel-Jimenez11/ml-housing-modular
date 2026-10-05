import pandas as pd
from sklearn.metrics import mean_absolute_error, root_mean_squared_error


def calcular_metricas(y_real, y_pred) -> dict:
    return {
        "MAE": mean_absolute_error(y_real, y_pred),
        "RMSE": root_mean_squared_error(y_real, y_pred),
    }


def evaluar_modelo(pipe, x_train, y_train, x_valid, y_valid) -> dict:
    pred_train = pipe.predict(x_train)
    pred_valid = pipe.predict(x_valid)
    metricas_train = calcular_metricas(y_train, pred_train)
    metricas_valid = calcular_metricas(y_valid, pred_valid)
    return {
        "MAE_train": metricas_train["MAE"],
        "RMSE_train": metricas_train["RMSE"],
        "MAE_valid": metricas_valid["MAE"],
        "RMSE_valid": metricas_valid["RMSE"],
    }


def entrenar_y_evaluar_modelos(
    modelos: dict,
    construir_pipeline,
    x_train,
    y_train,
    x_valid,
    y_valid,
) -> pd.DataFrame:
    resultados = []
    for nombre, modelo in modelos.items():
        pipeline = construir_pipeline(modelo)
        pipeline.fit(x_train, y_train)
        metricas = evaluar_modelo(pipeline, x_train, y_train, x_valid, y_valid)
        resultados.append({"Modelo": nombre, **metricas})
    return pd.DataFrame(resultados).sort_values("MAE_valid", ascending=True).reset_index(drop=True)


def seleccionar_mejor_modelo(tabla_resultados: pd.DataFrame) -> str:
    return tabla_resultados.loc[0, "Modelo"]


def evaluar_en_prueba(pipe, x_test, y_test) -> dict:
    pred_test = pipe.predict(x_test)
    return calcular_metricas(y_test, pred_test)