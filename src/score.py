"""Scoring utilities for the CVS-Q survey.

Functions:
 - compute_severity(frequency, intensity)
 - score_responses(df): returns DataFrame with item-level severities and total score

Small CLI is provided to run scoring on an input Excel file and write CSV output.
"""
from typing import Iterable
import pandas as pd


def compute_severity(frequency: int, intensity: int) -> int:
    """Compute severity = frequency * intensity with the README edge rule.

    Inputs are expected to be integers in {0,1,2}.
    If frequency == 0 the intensity is forced to 0.
    Returns one of {0,1,2,4}.
    """
    if frequency == 0:
        return 0
    return int(frequency) * int(intensity)


def score_responses(df: pd.DataFrame, freq_cols: Iterable[str], int_cols: Iterable[str]) -> pd.DataFrame:
    """Given a DataFrame with frequency and intensity columns, compute item severities and total score.

    - freq_cols and int_cols should be the same length and paired by item order.
    - Returns a copy of the DataFrame with new columns named `sev_<item>` and `total_severity`.
    """
    df_out = df.copy()
    freq_cols = list(freq_cols)
    int_cols = list(int_cols)
    if len(freq_cols) != len(int_cols):
        raise ValueError("freq_cols and int_cols must be the same length")

    severities = []
    for fcol, icol in zip(freq_cols, int_cols):
        sev_col = f"sev_{fcol}"
        # coerce to numeric, fill missing with 0
        f = pd.to_numeric(df_out[fcol], errors="coerce").fillna(0).astype(int)
        i = pd.to_numeric(df_out[icol], errors="coerce").fillna(0).astype(int)
        # apply edge rule: where frequency == 0, intensity -> 0
        i = i.where(f != 0, 0)
        sev = (f * i).astype(int)
        df_out[sev_col] = sev
        severities.append(sev_col)

    df_out["total_severity"] = df_out[severities].sum(axis=1).astype(int)
    return df_out


def _example_columns_from_readme() -> (list, list):
    """Return example column name lists used by tests and CLI.

    The real datasets may use other column names; tests use a synthetic DataFrame.
    """
    # Example placeholder names: freq_1..freq_16 and int_1..int_16
    freq_cols = [f"freq_{i+1}" for i in range(16)]
    int_cols = [f"int_{i+1}" for i in range(16)]
    return freq_cols, int_cols


def main(input_path: str, output_path: str):
    """Simple CLI: read Excel (first sheet) and write scored CSV to output_path."""
    df = pd.read_excel(input_path)
    freq_cols, int_cols = _example_columns_from_readme()
    # Try to detect columns present; fall back to first 16 pairs if names missing
    present_freq = [c for c in freq_cols if c in df.columns]
    present_int = [c for c in int_cols if c in df.columns]
    if len(present_freq) != len(present_int) or len(present_freq) == 0:
        # attempt to pick alternating columns if the file uses a compact layout
        # fallback: use first 32 numeric columns (16 pairs)
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        if len(numeric_cols) >= 32:
            present_freq = numeric_cols[0:16]
            present_int = numeric_cols[16:32]
        else:
            raise RuntimeError("Could not auto-detect frequency/intensity columns. Please supply columns or rename source file to freq_1..int_16 pattern.")

    scored = score_responses(df, present_freq, present_int)
    scored.to_csv(output_path, index=False)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Score CVS-Q responses from an Excel file")
    parser.add_argument("--input", required=True, help="Input Excel file path")
    parser.add_argument("--output", required=True, help="Output CSV path")
    args = parser.parse_args()
    main(args.input, args.output)
