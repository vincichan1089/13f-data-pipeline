from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # makes the object immutable after creation: once Config is created, you cannot assign new values to its attributes
class Config:
    root: Path
    data_dir: Path
    sqlite_dir: Path
    master_index_dir: Path
    derived_dir: Path
    qa_dir: Path
    staging_dir: Path
    start_year: int
    parse_start_year: int
    end_year: int
    workers: int
    timeout_sec: int
    sec_user_agent: str


def build_config(root: Path | None = None) -> Config: # Given an optional root folder, construct and return a ready-to-use configuration
    root_path = (root or Path(".")).resolve() # gives the absolute path of the root folder
    cfg = Config(
        root=root_path,
        data_dir=root_path / "data",
        sqlite_dir=root_path / "data" / "sqlites",
        master_index_dir=root_path / "data" / "master_index",
        derived_dir=root_path / "data" / "derived",
        qa_dir=root_path / "data" / "qa",
        staging_dir=root_path / "data" / "staging",
        start_year=1993,
        parse_start_year=1996,
        end_year=2026,
        workers=5,
        timeout_sec=300,
        sec_user_agent="wcchanvinci@gmail.com",
    )

    for p in [
        cfg.data_dir,
        cfg.sqlite_dir,
        cfg.master_index_dir,
        cfg.derived_dir,
        cfg.qa_dir,
        cfg.staging_dir,
    ]:
        p.mkdir(parents=True, exist_ok=True)

    return cfg


cfg = build_config()
