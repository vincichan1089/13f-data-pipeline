library(here)

cfg <- list(
  root             = here::here(),
  data_dir         = here::here("data"),
  sqlite_dir       = here::here("data", "sqlites"),
  master_index_dir = here::here("data", "master_index"),
  derived_dir      = here::here("data", "derived"),
  qa_dir           = here::here("data", "qa"),
  staging_dir      = here::here("data", "staging"),
  start_year       = 1993,
  parse_start_year = 1996,
  end_year         = 2026,
  workers          = 5,
  timeout_sec      = 300,
  sec_user_agent   = "wcchanvinci@gmail.com"
)

dir.create(cfg$data_dir,         recursive = TRUE, showWarnings = FALSE)
dir.create(cfg$sqlite_dir,       recursive = TRUE, showWarnings = FALSE)
dir.create(cfg$master_index_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(cfg$derived_dir,      recursive = TRUE, showWarnings = FALSE)
dir.create(cfg$qa_dir,           recursive = TRUE, showWarnings = FALSE)
dir.create(cfg$staging_dir,      recursive = TRUE, showWarnings = FALSE)

options(timeout = max(cfg$timeout_sec, getOption("timeout")))