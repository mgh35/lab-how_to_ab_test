import numpy as np
import pandas as pd

def random_contingency_table_2x2(*, scale=10, is_equal_p=False):
    p1 = np.random.uniform()
    if is_equal_p:
        p2 = p1
    else:
        p2 = np.random.uniform()

    n1 = np.random.poisson(scale)
    s1 = np.random.binomial(n1, p1)
    n2 = np.random.poisson(scale)
    s2 = np.random.binomial(n2, p2)

    return pd.DataFrame(data=[
        [s1, n1-s1],
        [s2, n2-s2]
    ], columns=['Success', 'Fail'])


def random_contingency_tables_2x2(n, **kwargs):
    for i in range(n):
        yield random_contingency_table_2x2(**kwargs)