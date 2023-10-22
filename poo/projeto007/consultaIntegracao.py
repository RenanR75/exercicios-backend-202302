import requests, json, pprint
api_key = "36a6bda3e04c35929851e175169874f8"
nome_da_cidade = "Rio de Janeiro"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + nome_da_cidade

response = requests.get(complete_url)
x = response.json()
pprint.pprint(x)
print(complete_url)


