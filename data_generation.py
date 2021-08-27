import numpy as np
import pandas as pd
from functools import partial


def generate_table1() -> pd.DataFrame:
    """

    :return:
    """
    n_cols = np.random.randint(3, 8)
    n_rows = np.random.randint(500, 3000)
    col_names = [f"Var{i}" for i in range(1, n_cols + 1)]
    distribution = [np.random.rand,
                    partial(np.random.binomial, 100, 0.5),
                    partial(np.random.poisson, 3),
                    partial(np.random.exponential, 5.)]
    data = [np.random.choice(distribution)(n_rows) for _ in range(n_cols)]
    d_dict = {k: v for k, v in zip(col_names, data)}
    data_frame = pd.DataFrame(d_dict)

    for col in data_frame.columns:
        data_frame.loc[data_frame.sample(frac=0.1).index, col] = np.nan

    return data_frame


def generate_table2() -> pd.DataFrame:
    """

    :return:
    """
    groups = ['A', 'B', 'C', 'D', 'E']
    n_rows = np.random.randint(300, 800)
    d_dict = {"id": np.arange(1, n_rows + 1),
              "group": np.random.choice(groups, n_rows)}
    data_frame = pd.DataFrame(d_dict)
    return data_frame


def join_tables() -> pd.DataFrame:
    """

    :return:
    """
    table1 = generate_table1()
    table1.dropna(axis=0, inplace=True)
    table2 = generate_table2()
    result = pd.merge(table1, table2, left_index=True, right_index=True)
    return result


def json_return():
    """

    :return:
    """
    table = join_tables()
    table_stat = table.describe().to_json()
    return table_stat
