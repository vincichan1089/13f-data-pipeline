from __future__ import annotations

from datetime import date

import pandas as pd


def make_quarter_tbl(
    start_year: int,
    end_year: int,
    start_month_day: str = "0101",
    end_month_day: str = "0331",
) -> pd.DataFrame:
    start_date = pd.Timestamp(f"{start_year}{start_month_day}").to_period("Q").start_time
    end_date = pd.Timestamp(f"{end_year}{end_month_day}")

    dates = pd.date_range(start=start_date, end=end_date, freq="QS")
    out = pd.DataFrame({"date": dates})
    out["year"] = out["date"].dt.year
    out["qtr"] = out["date"].dt.quarter
    out["year_qtr"] = out["year"].astype(str) + out["qtr"].astype(str)
    return out


def prev_year_qtr(year_qtr: str | int) -> str:
    yq = str(year_qtr)
    if len(yq) != 5:
        raise ValueError("year_qtr must be in YYYYQ format")

    yr = int(yq[:4])
    qtr = int(yq[4])

    if qtr == 1:
        return f"{yr - 1}4"
    return f"{yr}{qtr - 1}"


def quarter_end(dt: pd.Timestamp | date) -> pd.Timestamp:
    t = pd.Timestamp(dt)
    return t.to_period("Q").end_time.normalize()


def quarter_diff(date1: pd.Timestamp | date, date2: pd.Timestamp | date) -> int:
    d1 = pd.Timestamp(date1)
    d2 = pd.Timestamp(date2)

    q_index_1 = d1.year * 4 + ((d1.month - 1) // 3)
    q_index_2 = d2.year * 4 + ((d2.month - 1) // 3)

    return abs(q_index_2 - q_index_1)
