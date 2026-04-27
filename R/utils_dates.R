library(tidyverse)
library(lubridate)

make_quarter_tbl <- function(
  start_year,
  end_year,
  start_month_day = "0101",
  end_month_day   = "0331"
) {
  start_date <- ymd(paste0(start_year, start_month_day)) %>% floor_date("quarter")
  end_date   <- ymd(paste0(end_year,   end_month_day))

  tibble(date = seq(start_date, end_date, by = "quarters")) %>%
    mutate(
      year = year(date),
      qtr = quarter(date),
      year_qtr = paste0(year, qtr)
    )
}

prev_year_qtr <- function(year_qtr) {
  yr <- as.integer(substr(year_qtr, 1, 4))
  qtr <- as.integer(substr(year_qtr, 5, 5))
  if (qtr == 1) paste0(yr - 1L, 4L) else paste0(yr, qtr - 1L)
}