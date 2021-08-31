import numpy as np
import pandas as pd
from functools import partial


def generate_table1() -> pd.DataFrame:
    """
    generate_table() creates pandas DataFrame
    with randomly generated data.
    Number of columns varies from 3 to 7, number of rows from 500 to 2999
    Used distributions are standard normal, poisson, binomial and exponential.
    :return: pd.DataFrame with random data
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

    # Randomly assign missing values:
    for col in data_frame.columns:
        data_frame.loc[data_frame.sample(frac=0.1).index, col] = np.nan

    return data_frame


def generate_table2() -> pd.DataFrame:
    """
    generate_table2() - creates pandas DataFrame with categorical data
    :return: pd.DataFrame with randomly assigned categorical data
    """
    groups = ['A', 'B', 'C', 'D', 'E']
    n_rows = np.random.randint(300, 800)
    d_dict = {"id": np.arange(1, n_rows + 1),
              "group": np.random.choice(groups, n_rows)}
    data_frame = pd.DataFrame(d_dict)
    return data_frame


def join_tables() -> pd.DataFrame:
    """
    join_tables() - joins the results from generate_table1() and
    generate_table2() and drops missing values from generate_table1()
    :return: merged pd.DataFrame
    """
    table1 = generate_table1()
    table1.dropna(axis=0, inplace=True)
    table2 = generate_table2()
    result = pd.merge(table1, table2, left_index=True, right_index=True)
    return result


def json_return(include: str):
    """
    json_return() - converts pandas DataFrame to json
    :param include: valid options are "all", "float", "integer", "number"
    :return: json file with data description
    """
    table = join_tables()
    table_stat = table.describe(include=include).to_json()
    return table_stat


def json_return_user_file(file, include: str):
    df = pd.read_csv(file)
    df_stat = df.describe(include=include).to_json()
    return df_stat
