import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'sneakers'


def get_data(searchterm, i):
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=sneakers&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={}'.format(
        i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup, productslist):
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        product = {
            'title': item.find('div', {'class': 's-item__title'}).find('span').text,
            'soldprice': item.find('span', {'class': 's-item__price'}).text,
            'solddate': item.find('div', {'class': 's-item__title--tag'}).find('span', {'class': 'POSITIVE'}).text if item.find('div', {'class': 's-item__title--tag'}) else '',
        }
        productslist.append(product)
    return productslist


def output(productslist, searchterm):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv(searchterm + 'output9.csv', index=False)
    print('Saved to CSV')
    return


# range is determined by number of pages you want to scroll
productslist = []
for i in range(1, 1):
    print(i)
    soup = get_data(searchterm, i)
    productslist = parse(soup, productslist)
output(productslist, searchterm)
