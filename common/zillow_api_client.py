import requests

from json import dumps
from json import loads
from xmljson import badgerfish as bf

from xml.etree.ElementTree import fromstring

ZILLOW_ENDPOINT = 'http://www.zillow.com/webservice'
GET_SEARCH_RESULTS_API_NAME = 'GetSearchResults.htm'

ZWS_ID = '''X1-ZWz1fjzhaag64r _6ed93'''

def build_url(api_name):
    return '%s/%s' %(ZILLOW_ENDPOINT.strip('/'),api_name.strip('/'))

"""Zillow API: GetSearchResult"""
def getSearchResults(address, citystatezip, rentzestimate=False):
    payload = {
    'zws-id': ZWS_ID,
    'address': address,
    'citystatezip':citystatezip,
    'rentzestimate':rentzestimate
    }

    response = requests.get(build_url(GET_SEARCH_RESULTS_API_NAME))
    #thransform XML to JSON
    #dumps thransform JSON to String
    #loads thransform String to JSON
    res_json = loads(dumps(bf.data(fromstring(response.text))))
    print res_json
    #Extract info from response
    for key in res_json:
        print key
        if(res_json[key] is not None and res_json[key]['response'] is not None and res_json[key]['response']['results'] is not None):
            return res_json[key]['response']['results']['result']
        else:
            return {}
