"""Lightweight CLI runner for core factor-analysis functions.

Usage example:
    python run.py --input data.csv --n-factors 3
"""
import argparse
import sys
import pandas as pd
from .io_helpers import ensure_dataframe
from .processing import (
    convert_responses,
    compute_bartlett,
    run_pca,
    run_fa,
    communalities,
    loadings_df,
)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="e_learning_fa_core")
    parser.add_argument("--input", required=True, help="CSV file with questionnaire columns")
    parser.add_argument("--n-factors", type=int, default=3, help="Number of factors for FA")
    parser.add_argument("--pca-components", type=int, default=4, help="Number of PCA components")
    args = parser.parse_args(argv)

    df = ensure_dataframe(args.input)
    df_num = convert_responses(df)

    chi2, p = compute_bartlett(df_num)
    print(f"Bartlett test: chi2={chi2:.3f}, p={p:.3e}")

    pca, vals = run_pca(df_num, n_components=args.pca_components)
    print(f"PCA explained variance ratios: {pca.explained_variance_ratio_}")

    fa = run_fa(df_num, n_factors=args.n_factors)
    comm = communalities(fa)
    print("Communalities (head):")
    print(comm.head())

    loadings = loadings_df(fa, df_num.columns)
    print("Factor loadings (head):")
    print(loadings.head())


if __name__ == "__main__":
    main()
