from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome(executable_path='chromedriver')

def setCountyRaceURL(countyNo,countyName):
    url = "resultsSW.aspx?text=Race&type=CTYSPEC&map=CTY&cty=" + countyNo + "&name=" + countyName
    return url
    
urlDict = {}

for i in range(1,54):
    if i<10:
        url = 'http://results.sos.nd.gov/ResultsExport.aspx?cat=SWALL&type=CTYSPEC&text=Race&cty=0'+str(i)#06
    else:
        url= 'http://results.sos.nd.gov/ResultsExport.aspx?cat=SWALL&type=CTYSPEC&text=Race&cty='+str(i)
        
    urlDict[i] = url

    browser.get(url)
