library(urltools)
library(XML)
library(httr)
library(rvest)
library(magrittr)




url <- "http://results.sos.nd.gov/resultsSW.aspx?text=Race&type=SW&map=CTY"
statewide_html <- read_html(url)
#statewide_html %>% html_nodes(xpath="//")







tabl#url<- "http://results.sos.nd.gov/ResultsExport.aspx?rid=11244&osn=110&pty=REP&name=United%20Staractes%20Senator&cat=CTYALL"

# create a temporary directory
# td = tempdir()
# # create the placeholder file
# tf = tempfile(tmpdir=td, fileext=".xls")
# # download into the placeholder file
# download.file(url, tf, mode="wb")
# 
# fpath <-file.path(td)
# topath <-  "~/../../Desktop"
# #move and rename
# file.move(tf, getwd())
# file.rename(basename(tf), 'ND_Senate_by_precint.xls')
# 
# #look more into rid
