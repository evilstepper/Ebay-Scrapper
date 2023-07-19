import pandas as pd
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

pd.set_option('max_colwidth', 1000)
pd.set_option('max_rows', 1000)

APPLICATION_ID = 'Swagkick-Swagkick-PRD-1db16a83a-1c8aad98'


payload = {
        'keywords': 'belts', 
        'categoryId': ['3003'],
        'itemFilter': [
            {'name': 'LocatedIn', 'value': 'Germany'},{'name': 'SoldItemsOnly', 'value': 'true'}
        ],
        'sortOrder': 'StartTimeNewest',
}



def get_results(payload):
    try:
        api = Finding(siteid='EBAY-GB', appid=APPLICATION_ID, config_file=None)
        response = api.execute('findCompletedItems', payload)
        #response = api.execute('findItemsAdvanced', payload)
        
        return response.dict()
    except ConnectionError as e:
        print(e)
        print(e.response.dict())



# results = get_results(payload)

def get_total_pages(results):
    if results:
        return int(results.get('paginationOutput').get('totalPages'))
    else:
        return


def search_ebay(payload):
    
    results = get_results(payload)
    # total_pages = get_total_pages(results)
    total_pages=50
    print(total_pages)
    items_list = results['searchResult']['item']
        
    i = 2
    while(i <= total_pages):
        payload['paginationInput'] = {'entriesPerPage': 100, 'pageNumber': i}        
        results = get_results(payload)
        items_list.extend(results['searchResult']['item'])
        i += 1
        
    df_items = pd.DataFrame(columns=['itemId', 'title', 'viewItemURL', 'galleryURL', 'location', 'postalCode',
                                 'paymentMethod''listingType', 'bestOfferEnabled', 'buyItNowAvailable',
                                 'currentPrice', 'bidCount', 'sellingState'])

    for item in items_list:
        row = {
            'itemId': item.get('itemId'),
            'title': item.get('title'),
            'viewItemURL': item.get('viewItemURL'),
            'galleryURL': item.get('galleryURL'),
            'location': item.get('location'),
            'postalCode': item.get('postalCode'),
            'paymentMethod': item.get('paymentMethod'),        
            'listingType': item.get('listingInfo').get('listingType'),
            'bestOfferEnabled': item.get('listingInfo').get('bestOfferEnabled'),
            'buyItNowAvailable': item.get('listingInfo').get('buyItNowAvailable'),
            'currentPrice': item.get('sellingStatus').get('currentPrice').get('value'),
            'bidCount': item.get('bidCount'),
            'sellingState': item.get('sellingState'),
        }

        df_items = df_items.append(row, ignore_index=True)

    return df_items


# print(results)


df_items = search_ebay(payload)
df_items.head()
df_items.to_csv('ukbelts.csv',index=False) 
