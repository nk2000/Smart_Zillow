import requests

from lxml import html

URL = '''http://www.zillow.com'''
GET_PROPERTY_BY_ZPID_PATH = '''homes'''

""""connect the URL"""
def build_url(url,path):
    if url[-1] == '/':
        url = url[:-1]
    return '%s/%s' %(url,path)

SEARCH_XPATH_FOR_ZPID = '''//div[@id='list-results']/div[@id='search-results']/ul[@class='photo-cards']/li/article/@id'''
GET_INFO_XPATH_FOR_STREET_ADDR = '''//header[@class='zsg-content-header addr']/h1[@class='notranslate']/text()'''
GET_INFO_XPATH_FOR_CITY_STATE_ZIP = '''//header[@class='zsg-content-header addr']/h1[@class='notranslate']/span/text()'''
"""Get property information by Zillow Property ID"""
def get_property_by_zpid(zpid):
    request_url = '%s/%s_zpid' %(build_url(URL,GET_PROPERTY_BY_ZPID_PATH),str(zpid))
    session_requests = requests.session()
    print request_url
    response = session_requests.get(request_url)

    try:
        tree = html.fromstring(response.content)
    except Exception:
        return {}

    #Street address
    street_address = tree.xpath(GET_INFO_XPATH_FOR_STREET_ADDR)
    if len(street_address) == 0:
        street_address = ''
    else:
        street_address = street_address[0]
        street_address = street_address.strip(', ')

    #City, state and zipcode:need reg

    city_state_zipcode = tree.xpath(GET_INFO_XPATH_FOR_CITY_STATE_ZIP)
    if len(city_state_zipcode) == 0:
        city_state_zipcode = ''
    else:
        city_state_zipcode = city_state_zipcode[0]
    city = city_state_zipcode.split(',')[0].strip(', ')
    state = city_state_zipcode.split(',')[1].split()[0].strip(' ,')
    zipcode = city_state_zipcode.split(',')[1].split()[1].strip(' ,')



    return {
        'zpid':zpid,
        'street_adress':street_address,
        'city':city,
        'state':city,
        'zipcode':zipcode
    }

"""Get similar homes for sale"""
def get_similar_homes_for_sale_by_id(zpid):
    pass
