# Proyecto modular de regresión para California Housing

Proyecto de la actividad de Introducción a la IA y Machine Learning (CUGDL). Reorganiza en módulos de Python un notebook de exploración, entrenamiento y evaluación de modelos de regresión.

## 1. Descripción del problema y del conjunto de datos

Este proyecto resuelve un problema de regresión: predecir `median_house_value`, que representa el valor mediano de las casas en una zona censal. Cada fila del conjunto de datos corresponde a una zona censal completa, no a una casa individual.

Fuente de datos:
- https://raw.githubusercontent.com/IvTole/Intro_IA_ML_CUGDL/refs/heads/main/data/housing/housing.csv

Variables originales:
- `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income`, `ocean_proximity` (categórica) y `median_house_value` (variable objetivo).

Tamaño de los datos: 20,640 filas originales. Después de eliminar las filas con valores nulos (solo `total_bedrooms` los tiene) quedan 20,433.

División de los datos (semilla 42):

| Conjunto | Filas | Proporción |
|---|---:|---:|
| Entrenamiento | 12,259 | 60% |
| Validación | 4,087 | 20% |
| Prueba | 4,087 | 20% |

## 2. Integrantes y usuarios de GitHub

| Integrante | Usuario de GitHub |
|---|---|
| Axel Salvador Jimenez Lopez | [Axel-Jimenez11](https://github.com/Axel-Jimenez11) |
| Diego Vazquez Hernandez | [diegovazquez5803-cyber](https://github.com/diegovazquez5803-cyber) |
| Miguel Angel Torres Monroy | [migueltorres5238](https://github.com/migueltorres5238) |
| Ana Patricia Ponce Santero | [anaponce5994-lang](https://github.com/anaponce5994-lang) |

## 3. Organización de los archivos

```text
.
├── README.md                 # documentación del proyecto
├── requirements.txt          # dependencias
├── .gitignore                # archivos que no se versionan
├── train.py                  # script principal: coordina todo el flujo
├── data/
│   └── housing/
│       └── .gitkeep          # el CSV se descarga aquí, no se versiona
├── notebooks/
│   └── actividad_01_housing_referencia.py   # notebook original de referencia (marimo)
├── scripts/
│   └── download_data.py      # descarga el conjunto de datos
└── src/
    ├── __init__.py
    ├── config.py             # rutas, URL, semilla, variable objetivo y listas de variables
    ├── data_io.py            # carga del CSV, limpieza de nulos y separación de X e y
    ├── splitter.py           # división en entrenamiento, validación y prueba
    ├── features.py           # creación de variables derivadas
    ├── preprocessor.py       # preprocesamiento y pipeline con el modelo
    ├── models.py             # modelos a comparar y referencia de mediana
    └── evaluation.py         # métricas, tabla comparativa y evaluación final
```

## 4. Instalación de dependencias y datos

Desde la raíz del repositorio, crear y activar un entorno virtual.

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En Mac o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

El archivo CSV no se versiona. Se descarga con:

```bash
python scripts/download_data.py
```

El archivo se guarda en `data/housing/housing.csv`.

## 5. Comandos para preparar datos y ejecutar el proyecto

Desde la raíz del repositorio y con el entorno virtual activo:

```bash
python scripts/download_data.py
python train.py
```

`train.py` carga y limpia los datos, los divide, entrena y compara los modelos con entrenamiento y validación, selecciona el mejor por MAE de validación y lo evalúa una sola vez en prueba.

Para abrir el notebook de referencia:

```bash
marimo edit notebooks/actividad_01_housing_referencia.py
```

## 6. Modelos utilizados, resultados e interpretación

Modelos evaluados:
- Referencia: `DummyRegressor(strategy="median")`
- `LinearRegression`
- `DecisionTreeRegressor(max_depth=6, random_state=42)`
- `RandomForestRegressor(n_estimators=100, random_state=42)`

El preprocesamiento se ajusta únicamente con los datos de entrenamiento y se integra con cada modelo mediante un `Pipeline`. Las métricas son MAE y RMSE, en dólares.

Resultado de la ejecución de `python train.py`:

| Modelo | MAE entrenamiento | RMSE entrenamiento | MAE validación | RMSE validación |
|---|---:|---:|---:|---:|
| Bosque aleatorio | 12,476.74 | 19,072.13 | 33,149.99 | 50,117.12 |
| Árbol de decisión | 45,788.84 | 64,745.58 | 48,081.18 | 68,629.32 |
| Regresión lineal | 49,195.14 | 67,474.04 | 50,383.50 | 71,859.24 |
| Referencia mediana | 88,597.14 | 118,610.21 | 86,833.32 | 117,527.45 |

Modelo seleccionado por menor MAE de validación:
- **Bosque aleatorio**

Evaluación final en prueba (una sola vez, con el modelo seleccionado):
- **MAE de prueba: 33,711.37 dólares**
- **RMSE de prueba: 51,026.94 dólares**

Interpretación breve:
- El MAE es el error promedio absoluto, en dólares, por zona censal. El RMSE penaliza más los errores grandes, por eso es mayor que el MAE.
- Los tres modelos superan a la referencia de mediana. El bosque aleatorio reduce el MAE de validación de 86,833 a 33,150 dólares, cerca de 62%.
- El orden en validación es: bosque aleatorio, árbol de decisión, regresión lineal y referencia de mediana. El bosque es el que mejor captura relaciones no lineales entre las variables.
- El bosque aleatorio muestra sobreajuste claro: su MAE es de 12,477 en entrenamiento contra 33,150 en validación. Aun así sigue siendo el mejor modelo en validación.
- El error de prueba (MAE 33,711) es muy cercano al de validación (33,150), lo que indica que la elección del modelo no se debió a una partición de validación favorable.
- Los resultados corresponden a una sola partición con semilla 42; con otra partición o versiones distintas de las bibliotecas pueden variar ligeramente.

## 7. Limitaciones y problemas conocidos

- Se eliminan las filas con nulos (`dropna`), lo que pierde 207 zonas censales y puede cambiar la población representada.
- La partición es aleatoria y puede introducir sesgo geográfico, porque zonas cercanas tienen valores parecidos y pueden quedar repartidas entre entrenamiento y prueba.
- Las razones por hogar usan `.replace(0, 1)` en el denominador, que evita la división entre cero pero puede distorsionar filas con cero hogares.
- No se hizo ajuste de hiperparámetros: los modelos usan valores fijos tomados del notebook de referencia.
- El reentrenamiento final del modelo seleccionado se hace solo con entrenamiento, sin incorporar los datos de validación.
- Los resultados se obtienen con una sola partición, sin validación cruzada.
- El conjunto de datos refleja condiciones históricas cercanas a 1990 y cada fila es una zona censal, por lo que los resultados no aplican a casas individuales ni al mercado actual.

## 8. Flujo de colaboración

El trabajo se distribuyó en cuatro bloques de código, uno por integrante. Cada bloque se desarrolló en su propia rama, con commits descriptivos en español, y se integró a `main` mediante un pull request que describe qué cambió, por qué y cómo se verificó. Otro integrante revisó cada pull request y dejó observaciones concretas antes de la fusión.

| Bloque | Archivos | Rama | Responsable | Revisó |
|---|---|---|---|---|
| 1 | `src/config.py`, `src/data_io.py`, `scripts/download_data.py` | `feature/config-y-carga` | Axel Salvador Jimenez Lopez | Diego Vazquez Hernandez |
| 2 | `src/splitter.py`, `src/features.py`, `src/preprocessor.py` | `feature/division-y-preprocesamiento` | Diego Vazquez Hernandez | Miguel Angel Torres Monroy |
| 3 | `src/models.py`, `src/evaluation.py` | `feature/modelos-y-evaluacion` | Miguel Angel Torres Monroy | Ana Patricia Ponce Santero |
| 4 | `train.py` | `feature/orquestacion-train` | Ana Patricia Ponce Santero | Axel Salvador Jimenez Lopez |

Los bloques se fusionaron en el orden 1, 2, 3 y 4, porque cada uno depende de los anteriores. La documentación (este archivo) se agregó en un pull request aparte.
