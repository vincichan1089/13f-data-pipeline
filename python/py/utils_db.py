from __future__ import annotations

import sqlite3
from pathlib import Path

from py.config import cfg


def sqlite_path(year_qtr: str | int) -> Path:
    return cfg.sqlite_dir / f"{year_qtr}.sqlite"


def connect_sqlite(year_qtr: str | int) -> sqlite3.Connection:
    return sqlite3.connect(sqlite_path(year_qtr))


def disconnect_sqlite(con: sqlite3.Connection | None) -> None:
    if con is not None:
        con.close()
