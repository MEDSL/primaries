#adapted from https://hydroecology.net/downloading-extracting-and-reading-files-in-r/
library("downloader")
library("filesstrings")

url <-  "http://www.enr-scvotes.org/SC/75708/203926/reports/detailxls.zip"

# create a temporary directory
td = tempdir()
# create the placeholder file
tf = tempfile(tmpdir=td, fileext=".zip")
# download into the placeholder file
download.file(url, tf, mode="wb")
# get the name of the first file in the zip archive
fname = unzip(tf, list=TRUE)$Name[1]

# unzip the file to the temporary directory
unzip(tf, files=fname, exdir=td, overwrite=TRUE)
# fpath is the full path to the extracted file

fpath <-file.path(td, fname)
topath <-  "~/../../Desktop"

#move and rename
file.move(fpath, topath)
setwd(topath)
file.rename('detail.xls', 'SC_primary_by_county.xls')

