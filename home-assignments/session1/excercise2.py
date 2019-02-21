import urllib.request
import re

# get external IP

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

# get city file
def getCity():
    city = urllib.request.urlopen('https://iplocation.com/').read().decode('utf8')
    lines = city.split('\n')
    for line in lines:
        if re.search("class=\"city\"", line):
            output=line.split('>')[1].split('<')[0]
            return output


print(getExtIp())
print(getKey())
print(getCity())

