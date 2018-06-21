from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import re


driver = webdriver.Chrome()

#get all county names and hrefs
driver.get("http://silverstateelection.com/county-results/")
counties = [(button.text, button.get_attribute("href")) for button in driver.find_elements_by_class_name("btn")]


#make a list of dataframes (for efficiency) 
race_dfs =[]

#iterate through each county page
for county_name, county_url in counties:
    driver.get(county_url)

    #each race is marked with a race_id 
    race_ids = [race.get_attribute("id") for race in driver.find_elements_by_xpath(xpath="//div[contains(@id, 'race')]")]

    #iterate through each race
    for race_id in race_ids:

        #create a new dataframe for each race
        race_df = pd.DataFrame(columns = ['county', 'race', 'candidate', 'votes'])

        #get the name of the race (ie United States Senate (Democratic)
        race_name = driver.find_element_by_xpath(xpath= "//*[@id='{}']//h3".format(race_id)).text

        #expand the results to see table (need this to see dynamic results)
        race_el = driver.find_element_by_xpath(xpath= "//*[@id='{}']".format(race_id))
        race_el.find_element_by_class_name("race-details").click()

        #table id for results table is the same number as the race id 
        table_id = "table" + re.sub("\D", "", race_id)

        #get candidate names and votes from table
        candidate_names = [cand.text.replace("\n", " ") 
                           for cand in driver.find_elements_by_xpath(xpath="//*[@id='{}']//span[contains(@class, 'name')]".format(table_id))]
        votes = [vote.text for vote in driver.find_elements_by_xpath("//*[@id='{}']//td[contains(@class, 'Votes')]".format(table_id))]

        #populate df for that race
        race_df['candidate']= candidate_names
        race_df['votes'] = votes
        race_df['race']= race_name
        race_df['county'] = county_name
        
        race_dfs.append(race_df)

#create one df for all races
pd.concat(race_dfs).to_csv('NV_primary_results.csv', index = False)

