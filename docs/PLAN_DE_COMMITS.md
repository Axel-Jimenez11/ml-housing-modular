# Plan de commits y reparto de trabajo

## Orden propuesto para mantener `main` estable

1. Commit base de estructura.
2. Bloque [INTEGRANTE_1].
3. Bloque [INTEGRANTE_2].
4. Bloque [INTEGRANTE_3].
5. Bloque [INTEGRANTE_4].
6. Commit final de README.

Dependencias:
- [INTEGRANTE_2] depende de `config.py` de [INTEGRANTE_1].
- [INTEGRANTE_3] depende de módulos de [INTEGRANTE_2].
- [INTEGRANTE_4] depende de los bloques 1, 2 y 3.
- README final depende de tener métricas reales generadas por `train.py`.

## Commit inicial de base del repositorio

- Rama sugerida: `chore/base-estructura-proyecto`
- Archivos:
  - `.gitignore`
  - `requirements.txt`
  - `data/housing/.gitkeep`
  - `src/__init__.py`
  - `docs/PLAN_DE_COMMITS.md`
- Mensaje de commit sugerido:
  - `Crear estructura base del proyecto modular de housing`
- Borrador de PR:
  - Qué cambió: se creó la estructura mínima del proyecto, exclusiones de git y dependencias iniciales.
  - Por qué: habilitar trabajo paralelo por módulos sin romper la rama principal.
  - Cómo verificar: revisar árbol de archivos y ejecutar `pip install -r requirements.txt`.
- Observación de revisión sugerida:
  - `Verifica que .gitignore sí excluya data/housing/*.csv y conserve data/housing/.gitkeep para no versionar el dataset.`

## Bloque 1 · [INTEGRANTE_1]

- Rama sugerida: `feature/config-y-carga`
- Archivos:
  - `src/config.py`
  - `src/data_io.py`
  - `scripts/download_data.py`
- Mensaje de commit sugerido:
  - `Configurar rutas y carga de datos con validación de archivo`
- Borrador de PR:
  - Qué cambió: se centralizaron constantes de rutas, semilla, objetivo y proporciones; se implementó carga/limpieza/separación y script de descarga.
  - Por qué: evitar valores mágicos y garantizar mensaje claro si falta el CSV.
  - Cómo verificar: ejecutar `python scripts/download_data.py` y luego importar `cargar_datos()` desde Python.
- Observación de revisión sugerida:
  - `Revisa que el mensaje de error en cargar_datos indique explícitamente el comando python scripts/download_data.py cuando no existe el CSV.`
- Revisión cruzada:
  - Revisor: `[INTEGRANTE_2]`

## Bloque 2 · [INTEGRANTE_2]

- Rama sugerida: `feature/split-features-preprocess`
- Archivos:
  - `src/splitter.py`
  - `src/features.py`
  - `src/preprocessor.py`
- Mensaje de commit sugerido:
  - `Implementar partición 60-20-20 y pipeline de variables y preprocesamiento`
- Borrador de PR:
  - Qué cambió: se implementó split reproducible en dos pasos, creación de variables derivadas y pipeline con `FunctionTransformer` + `ColumnTransformer`.
  - Por qué: asegurar consistencia del flujo entre entrenamiento, validación y prueba sin fuga de información.
  - Cómo verificar: correr una sesión de Python y validar que el pipeline entrene con `fit` usando `x_train`.
- Observación de revisión sugerida:
  - `Confirma que rooms_per_household y bedrooms_per_household usen households.replace(0, 1) para evitar división entre cero.`
- Revisión cruzada:
  - Revisor: `[INTEGRANTE_3]`

## Bloque 3 · [INTEGRANTE_3]

- Rama sugerida: `feature/modelos-y-evaluacion`
- Archivos:
  - `src/models.py`
  - `src/evaluation.py`
- Mensaje de commit sugerido:
  - `Agregar fábrica de modelos y evaluación comparativa por MAE y RMSE`
- Borrador de PR:
  - Qué cambió: se añadieron baseline y tres modelos, además de funciones de métricas, tabla comparativa y selección por MAE de validación.
  - Por qué: permitir extender modelos con cambios mínimos y seleccionar de forma objetiva.
  - Cómo verificar: ejecutar funciones de evaluación con datos de entrenamiento/validación.
- Observación de revisión sugerida:
  - `Valida que la selección del mejor modelo se haga con MAE_valid y no con métricas de entrenamiento.`
- Revisión cruzada:
  - Revisor: `[INTEGRANTE_4]`

## Bloque 4 · [INTEGRANTE_4]

- Rama sugerida: `feature/orquestacion-train`
- Archivos:
  - `train.py`
- Mensaje de commit sugerido:
  - `Orquestar entrenamiento, selección por validación y evaluación final en prueba`
- Borrador de PR:
  - Qué cambió: se integró el flujo completo de ejecución desde carga hasta evaluación final en prueba.
  - Por qué: cumplir el proceso de ML requerido de punta a punta con una sola entrada ejecutable.
  - Cómo verificar: ejecutar `python train.py` tras descargar datos.
- Observación de revisión sugerida:
  - `Revisa que el pipeline final se cree de nuevo y se evalúe en prueba una sola vez, después de seleccionar modelo por validación.`
- Revisión cruzada:
  - Revisor: `[INTEGRANTE_1]`

## Commit final de README

- Rama sugerida: `docs/readme-final`
- Archivos:
  - `README.md`
- Mensaje de commit sugerido:
  - `Documentar ejecución, resultados y limitaciones del proyecto`
- Borrador de PR:
  - Qué cambió: se documentó problema, estructura, instalación, resultados reales, limitaciones y flujo de colaboración.
  - Por qué: dejar evidencia reproducible de decisiones y desempeño.
  - Cómo verificar: seguir comandos del README desde un entorno limpio.
- Observación de revisión sugerida:
  - `Comprueba que la tabla de resultados del README use métricas reales de la ejecución y no valores inventados.`
