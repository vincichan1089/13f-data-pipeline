# SEC 13F Institutional Holdings — Data Pipeline

An end-to-end data pipeline for downloading, parsing, and analyzing SEC Form 13F institutional holdings filings using R and Quarto.

The SEC Form 13F requires institutional investment managers with over $100 million in qualifying assets to report their quarterly equity holdings. This project builds a reproducible pipeline to collect, clean, and analyze the full universe of 13F filings from 1993 to present.

---

## Overview

This pipeline automates the full 13F data workflow:

1. **Download** — Fetches raw XML filings from the SEC EDGAR database
2. **Extract** — Parses holdings data from individual filing XMLs
3. **Parse** — Standardizes and structures holdings into tidy formats
4. **Combine** — Merges quarterly data into a unified panel
5. **Clean** — Performs data quality checks and corrections
6. **Analyze** — Generates summary statistics and visualizations

The pipeline covers approximately **30+ years** of 13F filings (1993–2026), processed through a parallelized, modular architecture.

---

## Pipeline Structure

```
workspace/
├── R/                          # Shared utility functions
│   ├── config.R                # Project configuration (years, paths, settings)
│   ├── utils_cusip.R           # CUSIP lookup and mapping utilities
│   ├── utils_dates.R           # Date parsing and quarter handling
│   └── utils_db.R              # SQLite database read/write utilities
│
├── qmd/                        # Quarto documents (pipeline stages)
│   ├── 01_download.qmd         # Download filings from SEC EDGAR
│   ├── 01a_redownload_missing_files.qmd  # Retry failed downloads
│   ├── 01b_cusip_universe.qmd  # Build CUSIP-to-ticker mapping universe
│   ├── 02_extract.qmd          # Extract holdings from raw XML
│   ├── 03_parse.qmd            # Parse and standardize data
│   ├── 04_combine.qmd          # Combine quarterly datasets
│   ├── 05_clean.qmd            # Data cleaning and QA
│   └── 06_analysis.qmd         # Exploratory analysis and outputs
│
└── .gitignore
```

---

## Tech Stack

| Category      | Tools |
|--------------|-------|
| Language     | R |
| Reporting    | Quarto (HTML output) |
| Data         | `data.table`, `dplyr`, `lubridate` |
| Database     | `DBI`, `RSQLite` |
| Parallel     | `future`, `furrr` |
| Project Mgmt | `here` |

---

## Key Features

- **Parallelized downloads** using `future`/`furrr` with configurable worker count
- **CUSIP-to-ticker mapping** for cross-referencing holdings with market data
- **SQLite-backed storage** for efficient querying of large panel datasets
- **Modular pipeline design** — each stage is a self-contained Quarto document
- **SEC-compliant** — respects EDGAR rate limits via user agent identification
- **Reproducible** — fully scripted workflow from raw data to analysis outputs

---

## Usage

### Clone the repository

```bash
git clone https://github.com/VinciChan2233/workspace.git
cd workspace
```

### Install required R packages

```r
install.packages(c("here", "data.table", "dplyr", "lubridate",
                   "DBI", "RSQLite", "future", "furrr"))
```

### Run the pipeline

Open the Quarto documents in RStudio and knit each file in sequence (01 → 06), or source the R scripts individually.

1. Configure parameters in `R/config.R` (year range, parallel workers, etc.)
2. Run `01_download.qmd` to fetch filings from SEC EDGAR
3. Proceed through stages 02–06 in order

> **Note:** The download stage makes HTTP requests to the SEC EDGAR API. Please be respectful of their rate limits.

---

## Data Source

- **SEC EDGAR**: U.S. Securities and Exchange Commission Electronic Data Gathering, Analysis, and Retrieval system
- **Form 13F**: Institutional Investment Manager Holdings Report
- **Coverage**: 1993–2026 (full historical archive)

---

## Potential Use Cases

- Track institutional ownership trends across sectors and market caps
- Identify "smart money" flows and manager concentration
- Analyze portfolio construction patterns of top asset managers
- Build factor or style exposure datasets from institutional holdings
- Research market structure and the evolution of institutional investing

---

## Author

**Vinci Chan**

- GitHub: [VinciChan2233](https://github.com/VinciChan2233)
- Location: Hong Kong

---

*This project is for educational and analytical purposes. Data is sourced from publicly available SEC filings.*
