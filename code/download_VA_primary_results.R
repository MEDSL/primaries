library(data.table)

#result site has downloadable csv file that contains precinct level results for all races

dem_results <- fread("https://results.elections.virginia.gov/vaelections/2018%20June%20Democratic%20Primary/Site/results.csv")
write.csv(dem_results, file = "~/../../Desktop/VA_dem_primary_by_precinct.csv")

rep_results <- fread("https://results.elections.virginia.gov/vaelections/2018%20June%20Republican%20Primary/Site/results.csv")
write.csv(rep_results, file = "~/../../Desktop/VA_rep_primary_by_precinct.csv")
