# Proyecto modular de regresión para California Housing

## 1. Descripción del problema y del conjunto de datos

Este proyecto resuelve un problema de regresión: predecir `median_house_value`, que representa el valor mediano de las casas en una zona censal. Cada fila del conjunto de datos corresponde a una zona censal completa, no a una casa individual.

Fuente de datos:
- https://raw.githubusercontent.com/IvTole/Intro_IA_ML_CUGDL/refs/heads/main/data/housing/housing.csv

Variables originales:
- `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income`, `ocean_proximity` y `median_house_value`.

## 2. Integrantes y usuarios de GitHub

| Integrante | Usuario de GitHub |
|---|---|
| [NOMBRE_1] | [@usuario_1] |
| [NOMBRE_2] | [@usuario_2] |
| [NOMBRE_3] | [@usuario_3] |
| [NOMBRE_4] | [@usuario_4] |

## 3. Organización de los archivos

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── train.py
├── data/
│   └── housing/
│       └── .gitkeep
├── notebooks/
│   └── actividad_01_housing_referencia.py
├── scripts/
│   └── download_data.py
├── docs/
│   └── PLAN_DE_COMMITS.md
└── src/
    ├── __init__.py
    ├── config.py
    ├── data_io.py
    ├── splitter.py
    ├── features.py
    ├── preprocessor.py
    ├── models.py
    └── evaluation.py
```

## 4. Instalación de dependencias y datos

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

El archivo CSV no se versiona. Se descarga con:

```bash
python scripts/download_data.py
```

El archivo se guarda en `data/housing/housing.csv`.

## 5. Comandos para preparar datos y ejecutar el proyecto

Desde la raíz del repositorio:

```bash
python scripts/download_data.py
python train.py
```

## 6. Modelos utilizados, resultados e interpretación

Modelos evaluados:
- Referencia: `DummyRegressor(strategy="median")`
- `LinearRegression`
- `DecisionTreeRegressor(max_depth=6, random_state=42)`
- `RandomForestRegressor(n_estimators=100, random_state=42)`

Resultado real de ejecución de `python train.py`:

| Modelo | MAE entrenamiento | RMSE entrenamiento | MAE validación | RMSE validación |
|---|---:|---:|---:|---:|
| Bosque aleatorio | 12,163.27 | 18,747.81 | 32,198.82 | 49,373.83 |
| Árbol de decisión | 45,541.50 | 64,631.65 | 47,835.61 | 68,326.66 |
| Regresión lineal | 49,412.54 | 67,681.89 | 50,408.29 | 71,520.00 |
| Referencia mediana | 88,597.14 | 118,610.21 | 86,833.32 | 117,527.45 |

Modelo seleccionado por MAE de validación:
- **Bosque aleatorio**

Evaluación final en prueba (una sola vez):
- **MAE prueba: 32,924.25 dólares**
- **RMSE prueba: 49,946.52 dólares**

Interpretación breve:
- El MAE representa el error promedio absoluto en dólares por zona censal.
- Todos los modelos mejoran claramente contra la referencia de mediana.
- El bosque aleatorio muestra sobreajuste moderado porque su error de entrenamiento es mucho menor que el de validación.
- El error de prueba del bosque es cercano al de validación, lo que sugiere consistencia razonable para esta partición.

## 7. Limitaciones y problemas conocidos

- Se eliminan filas con nulos (`dropna`), lo que puede cambiar la población representada.
- La partición es aleatoria y puede introducir sesgo geográfico.
- Las razones por hogar usan `.replace(0, 1)`, que evita división entre cero pero puede distorsionar filas con hogares en cero.
- No se hizo ajuste de hiperparámetros.
- El reentrenamiento final se hace solo con entrenamiento, sin incorporar validación.
- El dataset refleja condiciones históricas cercanas a 1990.

## 8. Flujo de colaboración

- Trabajar con ramas por bloque funcional y commits descriptivos en español.
- Abrir pull requests con secciones: qué cambió, por qué cambió y cómo se verificó.
- Aplicar revisión cruzada por otro integrante con observaciones concretas del código.
- Usar el plan en `docs/PLAN_DE_COMMITS.md` para mantener `main` estable tras cada fusión.
