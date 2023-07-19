import profile
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests
import pandas as pd
import re
import urllib.request as urllib2
import time

f = open("D:/Selenium/users.csv","w")
f.write("profile link,Instagram,Items Sold")
f.write("\n")



url=[]
users=[]

DRIVER_PATH = 'D:/Selenium/chromedriver'

link="https://www.depop.com/search/?q=sneaker"
options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")

options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(link)

for i in range(2000): 
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(1)
    

soup = BeautifulSoup(driver.page_source, 'html.parser')
for post in soup.findAll("ul", {'class': 'styles__ProductListContainer-sc-__sc-13q41bc-1 kayaIL'}):
      for li in post.find_all("li"):
          href = li.a.get("href")
          #print(href)
          url_to_go = "https://www.depop.com" + href
          #driver1 = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
          #driver1.get(url_to_go)
          #soup1 = BeautifulSoup(driver1.page_source, 'html.parser')
          html_document2 = urllib2.urlopen(url_to_go).read()
          soup2 = BeautifulSoup(html_document2, 'html.parser')
          username = soup2.find('a', class_ =  "sc-jrsJWt styles__Username-sc-__imzomr-3 isfTFw gdptiX").text

          if username is not None:
            # user=username.text
            print(username)
            if username not in users:
                users.append(username)
                
                profil = "https://www.depop.com/" + username + "/"
                f.write(profil)
                response = urllib2.urlopen(profil).read()
                soup4= BeautifulSoup(response, 'html.parser')
                insta = soup4.find('a', class_ = "sc-jrsJWt dfXtnW")
                itemsSold = soup4.find('p', class_ = "sc-jrsJWt Signalstyle__StyledText-sc-__sc-1xn3qq3-2 dfXtnW efkBL")
                if itemsSold is not None:
                    itemsSold = itemsSold.text[:-5]
                    f.write("," + itemsSold)
                    if insta is not None:
                        instaLink = insta.get("href")
                        print(instaLink)
                        f.write("," + instaLink)
                    f.write("\n")
                    
                    
f.close()


# import profile
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
# import requests
# import pandas as pd
# import re
# import urllib.request as urllib2
# import time
# # #file open
# productslist = []
# DRIVER_PATH = 'D:/Selenium/chromedriver'

# options = Options()
# options.headless = True
# # options.add_argument("--window-size=1920,1200")

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")

# options.add_experimental_option('excludeSwitches', ['enable-logging'])


# file = open("D:/Selenium/users.csv","r")
# line = file.readline()

# while(line):
#     line = file.readline()
#     if(line is not ''):
#         index=line.index(",")
#         a=line[0:index]
#         ue= a + "sold"
#         print(ue)
#         driver1 = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#         driver1.get(ue)
#         for i in range(100): 
#             driver1.execute_script("window.scrollTo(0, window.scrollY + 200)")
#             time.sleep(1)
#         soup21 = BeautifulSoup(driver1.page_source, 'html.parser')
#         for post1 in soup21.findAll("ul", {'class': 'styles__ProductListContainer-sc-__sc-13q41bc-1 fzvLUT'}):
#             for li1 in post1.find_all("li"):
#                 href1 = li1.a.get("href")
#                 print(href1)
#                 productslist.append("https://www.depop.com" + href1)


# file.close()
# df = pd.DataFrame(productslist) 
# df.to_csv('productlist.csv',index=False) 


    




