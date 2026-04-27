library(DBI)
library(RSQLite)
library(dplyr)
library(tibble)

pull_cusip_col <- function(tbl_obj) {
    cols <- colnames(tbl_obj)
    col_name <- case_when(
      "cusip" %in% cols ~ "cusip",
      "cusipno" %in% cols ~ "cusipno",
      TRUE ~ NA_character_
    )
    if (is.na(col_name)) return(character(0))
    tbl_obj %>% as_tibble() %>% pull(col_name)
  }

get.cusip.vec <- function(con, year_qtr) {
  # try current quarter
  if (dbExistsTable(con, "cusip_list")) {
    tbl_now <- tbl(con, "cusip_list")
    cusip_vec <- pull_cusip_col(tbl_now)
    return(cusip_vec)
  }

  # if missing (e.g. 1997Q4), try previous quarter
  prev_yq <- prev_year_qtr(year_qtr)
  prev_sqlite_path <- sqlite_path(prev_yq)

  if (!file.exists(prev_sqlite_path)) {
    return(character(0))
  }

  con_prev <- dbConnect(SQLite(), prev_sqlite_path)
  on.exit(dbDisconnect(con_prev), add = TRUE)

  if (!dbExistsTable(con_prev, "cusip_list")) {
    return(character(0))
  }

  tbl_prev <- tbl(con_prev, "cusip_list")
  pull_cusip_col(tbl_prev)
}
