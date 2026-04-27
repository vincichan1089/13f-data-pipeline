library(DBI)
library(RSQLite)

sqlite_path <- function(year_qtr) {
  file.path(cfg$sqlite_dir, paste0(year_qtr, ".sqlite"))
}

connect_sqlite <- function(year_qtr) {
  dbConnect(SQLite(), sqlite_path(year_qtr))
}

disconnect_sqlite <- function(con) {
  if (!is.null(con)) dbDisconnect(con)
}