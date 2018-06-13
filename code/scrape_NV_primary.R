library(urltools)
library(XML)
library(httr)
library(rvest)
library(magrittr)
library(dplyr)
library(magrittr)
library(glue)

BASE_URL = "http://silverstateelection.com/county-results/"

county_list_url <- "http://silverstateelection.com/county-results"
pg <- read_html(county_list_url)
county_urls <- paste(BASE_URL, urls[which(grepl("shtml", html_attr(html_nodes(pg, "a"), "href")))], sep='')

county_pg <- read_html(county_urls[1])

race_divs <-html_nodes(county_pg, xpath="//div[contains(@id,'race')]") 

#race names
race_names <- html_nodes(race_divs, xpath="//h3/text()") %>% tail(-1)

candidate_names <- html_nodes(race_divs, xpath= "//[contains(@class, 'name')]/text()")
votes <- html_nodes(race_divs, xpath= "//td[contains(@class, 'Votes')]/text()")

