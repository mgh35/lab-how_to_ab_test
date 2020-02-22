import numpy as np
import pandas as pd

import scipy.stats as scs
from statsmodels.stats.proportion import proportions_ztest

import how_to_ab_test.sample_data as sample_data


def pvalues(table):
    # _, p_fisher = scs.fisher_exact(table, alternative='two-sided')
    p_fisher = 1.0
    _, p_z = proportions_ztest(
        table.Success,
        table.Success+table.Fail,
        alternative='two-sided',
        prop_var=False
    )
    try:
        _, p_chi2, _, _ = scs.chi2_contingency(table.values, correction=False)
    except Exception:
        p_chi2 = np.nan
    try:
        _, p_chi2_corrected, _, _ = scs.chi2_contingency(table.values, correction=True)
    except Exception:
        p_chi2_corrected = np.nan

    if np.isnan(p_z):
        p_z = 1.0
    if np.isnan(p_chi2):
        p_chi2 = 1.0
    if np.isnan(p_chi2_corrected):
        p_chi2_corrected = 1.0

    return pd.DataFrame(
        data=[
            [p_fisher, p_z, p_chi2, p_chi2_corrected],
        ], columns=['fisher', 'z', 'chi2', 'chi2_corrected']
    )


def rejections(n, p1, p2, n_samples, alphas):
    samples = pd.concat([
        pvalues(
            sample_data.random_contingency_table_2x2(n=(n, n), p=(p1, p2))
        )
        for i in range(n_samples)
    ])
    out = pd.DataFrame()
    for alpha in alphas:
        r = (samples < alpha).sum() / n_samples
        r['alpha'] = alpha
        out = out.append(r, ignore_index=True)

    return out