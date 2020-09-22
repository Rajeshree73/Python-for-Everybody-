import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#print(data.decode())

try:
  js = json.loads(data)
except:
  js = None

lst = list()

print(json.dumps(js, indent=4))

lst = list()
getcount = 0

getnum = js['comments']
for num in getnum:
    lst.append(num['count'])


print(lst)
print(sum(lst))
