
import pandas as pd



def createRaceDf(race, party, district_list):
    final_dfs = []
    if not district_list:
        district_list.append('')  #if a statewide race pass no district information to url
        jurisdiction = 'statewide'
    for district in district_list: 
        race_name = "%20".join(race.split()) #urlify
        if district: 
            jurisdiction = district
            district = '%20District%20' + str(district) #format district
        url = "https://elections.tn.gov/county-results.php?OfficeByCounty={}{}&Party={}".format(race_name, district, party)
        dfs= pd.read_html(url) #pandas function that reads html tables
        for df in dfs:  #each county has its own df
            columns = df.columns
            if "Totals" not in columns[0]:  #don't include totals in our results for formatting reasons
                county = columns[0].strip() #county name
                df = df.rename(index=str, columns={columns[0]: 'candidate', columns[1]: "votes"}) #change header names
                df = df.drop(columns[2], axis=1) #drop percentages 
                df['county'] = county
                df['race'] = race #race name
                df['jurisdiction'] = jurisdiction #district or statewide
                df['party'] = party
                final_dfs.append(df) 
            else: 
                pass
                #print race_name, party_name, columns[0]
    return final_dfs




parties = ['Democratic', 'Republican']
for party in parties: 
    dfs = createRaceDf('Governor', party, [])
    dfs.extend(createRaceDf('United States Senate', party, []))
    dfs.extend(createRaceDf('United States House of Representatives', party , range(1,10)))
    dfs.extend(createRaceDf('Tennessee Senate', party, range(1,34, 2) + [2]))
    dfs.extend(createRaceDf('Tennessee House of Representatives', party, range(1,100)))
    dfs.extend(createRaceDf('Tennessee House of Representatives', party, range(1,100)))

#write file 
pd.concat(dfs, ignore_index = True).to_csv('TN_unofficial_by_county.csv', index=False)

