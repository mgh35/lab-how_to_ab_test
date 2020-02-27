import numpy as np
import pandas as pd

import scipy.stats as scs
from statsmodels.stats.proportion import proportions_ztest

import how_to_ab_test.sample_data as sample_data


def pvalues(table, *, exclude=None):
    if exclude is None:
        exclude = []
    data = []
    cols = []
    if not 'fisher' in exclude:
        _, p_fisher = scs.fisher_exact(table, alternative='two-sided')
        data.append(p_fisher)
        cols.append('fisher')

    if not 'z' in exclude:
        _, p_z = proportions_ztest(
            table.Success,
            table.Success+table.Fail,
            alternative='two-sided',
            prop_var=False
        )
        if np.isnan(p_z):
            p_z = 1.0
        data.append(p_z)
        cols.append('z')

    if not 'chi2' in exclude:
        try:
            _, p_chi2, _, _ = scs.chi2_contingency(table.values, correction=True)
        except Exception:
            p_chi2 = np.nan
        if np.isnan(p_chi2):
            p_chi2 = 1.0
        data.append(p_chi2)
        cols.append('chi2')

    return pd.DataFrame(
        data=[data], columns=cols
    )


def rejections(n, p1, p2, n_samples, alphas, *, exclude=None):
    samples = pd.concat([
        pvalues(
            sample_data.random_contingency_table_2x2(n=(n, n), p=(p1, p2)),
            exclude=exclude
        )
        for i in range(n_samples)
    ])
    out = pd.DataFrame()
    for alpha in alphas:
        r = (samples < alpha).sum() / n_samples
        r['alpha'] = alpha
        out = out.append(r, ignore_index=True)

    return out.melt(id_vars=['alpha'], var_name='test', value_name='rejections')