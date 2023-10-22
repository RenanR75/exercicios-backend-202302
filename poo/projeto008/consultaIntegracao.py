#import required modules
import requests, json, sys, pprint
#Enter your APIkey here
api_key = "bdd4b856"
nome_do_filme = "Titanic"
# base_url variable to store url
base_url = "http://www.omdbapi.com/?"
complete_url = base_url + "apikey=" + api_key + "&t="+nome_do_filme
response = requests.get(complete_url)
x = response.json()
pprint.pprint(x)