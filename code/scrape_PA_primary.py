

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()


# ## Get Counties
driver.get("https://www.electionreturns.pa.gov/Home/SummaryResults")
counties = [el.get_attribute("alt") for el in driver.find_elements(By.CLASS_NAME, "countydata")]

# ## Election ID 
# By visiting one of the county sites from https://www.electionreturns.pa.gov/Home/SummaryResults you can see the election ID in the url

ELECTION_ID = "63"

def getElectedOfficeElements(driver):
    '''the id "items" is used to identify the body of the page not including the "filter options" div; 
    the class name is not unique to the larger divs, so I used the background color to isolate the divs 
    that contain race information'''
    return driver.find_elements(By.XPATH, "//div[@id = 'items']//div[@style='background-color:#D1E7FE;']")


def createRaceDataFrame(raceElement, county_name, office_name, district): 
    '''for each party's primary race for each seat, create a dataframe'''
    party = raceElement.find_element(By.CLASS_NAME, "panel-title").text
    cand_names = [name.text for name in raceElement.find_elements(By.XPATH, ".//*[@ng-bind='item.CandidateName']")]
    votes = [votes.text.replace(" Votes", "") for votes in raceElement.find_elements(By.CLASS_NAME, "progress-spantext")]
    return pd.DataFrame(columns = ['county', 'office', 'district', 'primary', 'candidate name', 'votes'], 
                     data= {'county': county_name, 'office': office_name, 'district': district,
                            'primary':party, 'candidate name': cand_names, 'votes': votes})


# ## Collect data for each county and create a dataframe

race_dfs = []
for county_name in counties: 
    url = "https://www.electionreturns.pa.gov/Home/CountyResults?countyName={}&ElectionID={}&ElectionType=P&IsActive=1".format(county_name, ELECTION_ID)
    driver.get(url)
    time.sleep(5)
    office_elements = getElectedOfficeElements(driver)
    
    #offices are races for both parties (ie U.S. Senate)
    for office in office_elements: 
        office_name = office.find_element(By.CLASS_NAME, "panel-heading-level1").text
        
        #some races are broken into districts (ie general assembly)
        districts = office.find_elements(By.CLASS_NAME, "col-xs-12")

        for district in districts: 
            #get text, if district race than district will be in title 
            district_name = [el.text for el in district.find_elements(By.CLASS_NAME, "panel-title")][0]
            party_races = district.find_elements(By.CLASS_NAME, "col-xs-6")
            if 'District' not in district_name:
                
                #if not a district race, it is a statewide race
                district_name = 'Statewide'
            for party_race in party_races: 
                #create df
                race_dfs.append(createRaceDataFrame(party_race, county_name, office_name, district_name))
    #print county_name,



df = pd.concat(race_dfs, ignore_index= True)

df.to_csv('PA_primary_by_county.csv', index=False)

