# SEC 13F Institutional Holdings Data Pipeline

An end-to-end R and Quarto pipeline for downloading, extracting, parsing, cleaning, and analyzing SEC 13F institutional holdings filings.

This project builds a historical 13F holdings dataset from raw SEC EDGAR filings. It automates the workflow from quarterly filing download through table extraction and parsing to cleaned manager-quarter holdings panels for downstream research and analysis.

## Overview

The pipeline is designed to turn raw 13F filings into structured, analysis-ready holdings data. It handles multiple filing and table formats across time, stores intermediate outputs in SQLite and Parquet, and includes quality-assurance checks at each major stage.

## Pipeline Stages

1. **Download filings**
   - Pull quarterly SEC master index files
   - Filter for 13F-related submissions
   - Download raw filing text files from EDGAR

2. **Recover missing filings**
   - Compare downloaded filings against the master index
   - Redownload and append missing files to the quarter database

3. **Build CUSIP universe**
   - Download and parse SEC 13F CUSIP reference lists
   - Handle pre-2004 PDF/OCR quirks and post-2004 table formats
   - Store quarter-level CUSIP lists for downstream matching

4. **Extract holdings tables**
   - Extract information tables from raw filings
   - Support XML sections, `TABLE` blocks, and fallback text extraction logic
   - Save raw extracted holdings text for each filing

5. **Parse holdings**
   - Parse XML, tab-delimited, comma-delimited, and fixed-width style tables
   - Identify CUSIPs, values, share counts, discretion flags, and related fields
   - Write structured holdings rows back to quarterly SQLite files

6. **Combine quarterly outputs**
   - Read parsed holdings across quarter-level databases
   - Append into a unified historical holdings dataset
   - Export consolidated data to Parquet

7. **Clean and standardize**
   - Standardize reporting and filing dates
   - Select canonical filings for each manager-quarter
   - Clean and validate CUSIPs
   - Filter extreme outliers
   - Detect likely post-2023 value unit switches
   - Fill missing quarters to build a more complete panel

8. **Analyze**
   - Construct manager-quarter portfolio summaries
   - Compute simple return and holdings-based metrics
   - Explore cross-sectional fund characteristics

## Repository Structure

```text
01_download.qmd                  # Download quarterly 13F filings from SEC EDGAR
01a_redownload_missing_files.qmd # Identify and recover missing filings
01b_cusip_universe.qmd           # Build quarterly 13F CUSIP universe
02_extract.qmd                   # Extract raw holdings tables from filings
03_parse.qmd                     # Parse extracted tables into structured holdings
04_combine.qmd                   # Combine parsed quarterly outputs
05_clean.qmd                     # Clean, standardize, and panelize holdings data
06_analysis.qmd                  # Exploratory analysis on cleaned holdings data

config.R                         # Project configuration and directory settings
utils_db.R                       # Database path / connection helpers
utils_cusip.R                    # Quarter-aware CUSIP lookup helpers
utils_dates.R                    # Quarter table and date utilities
```

## Tech Stack

- **R**
- **Quarto**
- **SQLite**
- **Arrow / Parquet**
- **tidyverse**
- **future / furrr** for parallel processing

## Key Features

- End-to-end historical 13F data pipeline
- Support for multiple filing and table formats across filing eras
- Quarter-specific CUSIP reference matching
- SQLite-backed intermediate storage
- Parquet outputs for efficient downstream analysis
- Built-in QA summaries and validation plots
- Modular workflow split into reproducible Quarto scripts

## Data Workflow

Raw SEC filings are downloaded and stored quarter by quarter. Holdings tables are then extracted and parsed into structured rows, combined into a full historical dataset, and cleaned into a manager-quarter panel for research use.

Intermediate processing relies on SQLite databases, while downstream combined and cleaned datasets are written in Parquet format for efficient analysis.

## Example Use Cases

This repository can support work such as:
- Institutional holdings research
- Manager-level portfolio analysis
- Historical 13F panel construction
- Data engineering practice with messy regulatory filings
- Reproducible finance and market microdata workflows

## Notes

- The pipeline includes special handling for historical filing inconsistencies and missing quarters.
- Some stages include quarter-level QA outputs and manual exception handling where SEC source files are irregular.
- The repository is an active research/data engineering project and may continue to evolve.

## Author

**Vinci Chan**

If you work in finance, data analytics, or regulatory filings research, feel free to connect via LinkedIn or explore the repository.
