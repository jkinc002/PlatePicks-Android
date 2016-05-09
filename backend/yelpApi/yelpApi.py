import io
import json
from pprint import pprint
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.config import SEARCH_PATH
from yelp.obj.search_response import SearchResponse
from crawl import Crawler
import datetime

# This class serves as Yelp API's wrapper
# param: python dictionary with
class Yelp_API(object):
    def __init__(self, data):
        #authorization
        with io.open('config_secret.json') as cred:
            creds = json.load(cred)
            auth = Oauth1Authenticator(**creds)
            self.client = Client(auth)
            self.data = data
        self.food_per_business = data['food_per_business']

    def call_API(self):
        #  return self.client.search('SF', self.data)
        #  return SearchResponse (
                #  self.client._make_request(SEARCH_PATH, self.data)
        #  )
        response = SearchResponse(
                self.client._make_request(SEARCH_PATH, self.data)
                )

        list_to_be_returned = []
        #  for bus in response.businesses:
            #  list_to_be_returned += Crawler.limit("http://www.yelp.com/biz_photos/" + bus.id + "?tab=food&start=0", self.food_per_business)
        dict_of_urls = {}
        for bus in response.businesses:
            #  pprint(vars(bus.location))
            url = "http://www.yelp.com/biz_photos/"+bus.id+"?tab=food&start=0"
            #  list_of_urls.append({url: [bus.location, bus.name]})
            #  list_of_urls.append({url: 
            dict_of_urls[url]= dict(address=bus.location.address, 
                    name=bus.name,
                    city=bus.location.city,
                    state=bus.location.state_code,
                    postal_code=bus.location.postal_code,
                    display_address=bus.location.display_address
                    )
            #  print dict_of_urls

            #  pprint(list_of_urls)
            #  print (list_of_urls)
        #  Crawler.limit(list_of_urls, 1)
        return Crawler(dict_of_urls).limit(self.food_per_business)

    #  return list_to_be_returned


#  print full object attribute of first object
#  print("----------------------------------------------------")
#  print("FIRST BUSINESS")
#  pprint(vars(response.businesses[0]))

#  print all business id's
#  print("----------------------------------------------------")
#  print("FIRST 5 BUS.ID")
#  for bus in response.businesses:
    #  print ("{0}".format( bus.id))

#  crawl url for pics
#  print("----------------------------------------------------")
#  print("CRAWL")
#  Crawler("https://www.yelp.com/biz/pho-vinam-riverside")


# Test time
#  for bus in response.businesses:
    #  a = datetime.datetime.now()
    #  Crawler.limit("http://www.yelp.com/biz_photos/" + bus.id +
            #  "?tab=food&start=0", 1)
    #  b = datetime.datetime.now()
    #  print ((b - a).microseconds)

    #  a = datetime.datetime.now()
    #  Crawler.limit("http://www.yelp.com/biz_photos/" + bus.id +
            #  "?tab=food&start=0", 100)
    #  b = datetime.datetime.now()
    #  print ((b - a).microseconds)
    #  print(Crawler.limit("http://www.yelp.com/biz_photos/" + bus.id +
            #  "?tab=food&start=0", 5))
