import urllib.request
import re
import requests

# writing data to file
def writeData(str, filename):
    try:
        with open(filename, 'w') as file:
            file.write(str)
    except IOError:
        print("Can't create file")
        exit(0)

## get ext_ip // depricated
def getExtIp():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip

# get API from file
def getKey():
    try:
        with open('Weather_API_Key.txt', 'r') as file:
            key = file.read()
        return key
    except IOError:
        print("Can't open file")
        exit(0)

# get city
def getCity():
    url = urllib.request.urlopen('https://iplocation.com/').read().decode('utf8')
    lines = url.split('\n')
    for line in lines:
        if re.search("class=\"city\"", line):
            r=line.split('>')[1].split('<')[0]
     #   if re.search("class=\"country_name\"", line):
      #      r['country']=line.split('>')[2].split('<')[0]

    return r

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid={1}".format(location,api_key)
    r = requests.get(url)
    return r.json()

def getCountry(city, lon, lat):
    url="http://photon.komoot.de/api/?q={}&lat={}&lon={}".format(city,lat,lon)
    r = requests.get(url)
    return r.json()['features'][0]['properties']['country']


# 1st task -> write into file
city=getCity()
str="The weather in {} is {} degrees".format(city,get_weather(getKey(),city)['main']['temp'])
writeData(str,"excercise2_1.txt")

# second task, create list with 10 cities and write to new file
cities=['Madrid', 'Berlin', 'London', 'Paris', 'Moscow', 'Kiev', 'Lisbon', 'Stockholm', 'Budapest', 'Burgas']
str=""
for cityname in cities:
    report=get_weather(getKey(),cityname)
    temp=report['main']['temp']
    lon=report['coord']['lon']
    lat = report['coord']['lat']
    getCountry(cityname,lon,lat)
    str+="The weather in {}, {} is {} degrees.\n".format(cityname,getCountry(cityname,lon,lat),temp)

writeData(str,"excercise2_2.txt")