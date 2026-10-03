from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from src.config import SEED


def obtener_modelos() -> dict:
    return {
        "Referencia mediana": DummyRegressor(strategy="median"),
        "Regresión lineal": LinearRegression(),
        "Bosque aleatorio": RandomForestRegressor(n_estimators=100, random_state=SEED),
        "Árbol de decisión": DecisionTreeRegressor(max_depth=6, random_state=SEED),
    }
