from __future__ import annotations

import sqlite3
from typing import Sequence

import pandas as pd

from py.utils_dates import prev_year_qtr
from py.utils_db import sqlite_path


def pull_cusip_col(tbl_obj: pd.DataFrame) -> Sequence[str]:
    cols = list(tbl_obj.columns)

    if "cusip" in cols:
        col_name = "cusip"
    elif "cusipno" in cols:
        col_name = "cusipno"
    else:
        return []

    return tbl_obj[col_name].dropna().astype(str).tolist()


def _read_table(con: sqlite3.Connection, table_name: str) -> pd.DataFrame:
    return pd.read_sql_query(f"SELECT * FROM {table_name}", con)


def _has_table(con: sqlite3.Connection, table_name: str) -> bool:
    q = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
    return con.execute(q, (table_name,)).fetchone() is not None


def get_cusip_vec(con: sqlite3.Connection, year_qtr: str | int) -> list[str]:
    if _has_table(con, "cusip_list"):
        tbl_now = _read_table(con, "cusip_list")
        return list(pull_cusip_col(tbl_now))

    prev_yq = prev_year_qtr(year_qtr)
    prev_sqlite_file = sqlite_path(prev_yq)

    if not prev_sqlite_file.exists():
        return []

    con_prev = sqlite3.connect(prev_sqlite_file)
    try:
        if not _has_table(con_prev, "cusip_list"):
            return []

        tbl_prev = _read_table(con_prev, "cusip_list")
        return list(pull_cusip_col(tbl_prev))
    finally:
        con_prev.close()
