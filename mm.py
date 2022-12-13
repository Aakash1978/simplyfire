import requests
import webbrowser as Web 
r = requests.get('https://get.geojs.io/')
ip_request=requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()
import json 
from urllib.request import urlopen
url = 'https://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
url ='https://get.geojs.io/v1/ip/geo/'+data['ip']+'.json'
geo_request=requests.get(url)
geo_data = geo_request.json()
print(geo_data)
print(geo_data['longitude'])
print(geo_data['latitude'])

print("https://www.google.com/maps/@"+geo_data['latitude']+","+geo_data['longitude']+",17z")