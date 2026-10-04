import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import SEED, TEST_SIZE, VALID_SIZE_OF_DEV


def dividir_train_valid_test(
    x: pd.DataFrame,
    y: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    x_desarrollo, x_test, y_desarrollo, y_test = train_test_split(
        x,
        y,
        test_size=TEST_SIZE,
        random_state=SEED,
    )
    x_train, x_valid, y_train, y_valid = train_test_split(
        x_desarrollo,
        y_desarrollo,
        test_size=VALID_SIZE_OF_DEV,
        random_state=SEED,
    )
    return x_train, x_valid, x_test, y_train, y_valid, y_test
