# =================================================
# * IMPORTS * 
import time
import json
import traceback
from selenium import webdriver #You may have to type in a terminal "pip install selenium"
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# =================================================
# * Selenium Setup * 
caps = DesiredCapabilities.CHROME
caps["goog:loggingPrefs"] = {"performance": "ALL"}
options = webdriver.ChromeOptions()
options.add_argument(r"--log-level=3")
options.add_argument(r"--silent")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options,desired_capabilities=caps)    
a = ActionChains(driver)

# =================================================
# * Selenium Function * 
def Find_Text_by_xpath(xpath_var):
    time.sleep(.2)
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_var)))
        elem_text = driver.find_element("xpath", xpath_var).text
    except Exception as e:
        print(traceback.format_exc())
        print(xpath_var)
    return elem_text


#Remember to put commas at the ends of every line but the last
ListofURLS = [
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0x1d328a70404b88d4572ee6c06a568a205fecc44e442d836b96026a67fcfeaf57',
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0xa834df3d51f13f68d1e9b1fc2d4180e50db3c6d21ff52837703392dad925f982',
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0x93a2f573a439462f830346f09180cf7720677103854a2b43c7286152540d2369',
    'https://nft.gamestop.com/token/0x68505cc595a518e5a713224056df511751591fa7/0x20329c270e75f8b3a7685d16acac49027f2d5531b78f26ad9803eba358ef5c9f'
    ]

for url in ListofURLS: #Go through List of URLS
    driver.get(url)
    time.sleep(2) #Seconds the page waits to load, increase if page doesnt load in time
    
    Name = Find_Text_by_xpath('//*[@id="root"]/div/div[4]/div/article/section[2]/div[1]/h1')
    Available = Find_Text_by_xpath('//*[@id="root"]/div/div[4]/div/article/section[2]/div[2]/section/div[1]/div[2]/div/div[2]/span[2]')
    Price = Find_Text_by_xpath('//*[@id="root"]/div/div[4]/div/article/section[2]/div[2]/section/div[1]/div[2]/div/div[1]/div[1]/span[2]')
    
    print(f"Name: {Name}")
    print(f"Available: {Available}")
    print(f"Price: {Price}")
