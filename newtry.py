import requests
from lxml import html
import csv
import time


pages = range(500)
i=6
for i in pages:
# URL of the site to scrape
    url = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=sneakercycle&store_name=sneakercycle&_oac=1&LH_Sold=1&_ipg=240&_pgn={}'.format(i)
    response = requests.get(url)
    tree = html.fromstring(response.content)
    titlepath = "//*/div/div[2]/a/div/span/text()"
    pricepath = "//*/div/div[2]/div[3]/div[1]/span/span/text()"
    datepath = "//*/div/div[2]/div[1]/div/span[1]/text()"
    # brandpath="//*/div/div[2]/div[2]/text()"
    
    text_elements1 = tree.xpath(titlepath)
    text_elements2 = tree.xpath(pricepath)
    text_elements3 = tree.xpath(datepath)
    # text_elements4 = tree.xpath(brandpath)

    with open('com_shows_data.csv', 'a', newline='',encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)

        for element_role, element_class, element_class1 in zip(text_elements1, text_elements2, text_elements3):
           
           
            
            # text_class2 = element_class2.strip()
            # name
            if element_role.strip():
                text_role = element_role.strip()
           
            # price
            if element_class.strip():
                text_class = element_class.strip()
    
            # sold
            if element_class1.strip():
                text_class1 = element_class1.strip().replace('Sold', '')
    
            
            csv_writer.writerow([text_role, text_class,text_class1])
            print(text_role, text_class,text_class1)

    time.sleep(5)