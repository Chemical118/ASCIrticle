from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import keyboard as k
import pandas as pd


ua = UserAgent()
userAgent = ua.random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={userAgent}')
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

df = pd.read_excel('data.xls', header=None)
df_list = map(lambda t: t[0], df.values.tolist())
for i in df_list:
    driver.get("https://www.ncbi.nlm.nih.gov/protein/?term=" + (i + ' citrate synthase').replace(' ', '+'))
    k.wait('esc')
