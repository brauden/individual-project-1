from data_generation import generate_table1, generate_table2


def test_rows_table1():
    table1 = generate_table1()
    assert 500 <= table1.shape[0] < 3000


def test_cols_table1():
    table1 = generate_table1()
    assert 3 <= table1.shape[1] < 8


def test_groups_table2():
    table2 = generate_table2()
    groups_table2 = table2['group'].unique()
    assert all(i in ['A', 'B', 'C', 'D', 'E'] for i in groups_table2)
