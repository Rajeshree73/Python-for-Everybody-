
import urllib.request, urllib.parse, urllib.error 
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving', url)

xml = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xml), 'characters')

tcounts = 0
sum = 0

data = ET.fromstring(xml)
counts = data.findall('.//count')

for nums in counts:
    sum = sum +  int(nums.text)
    tcounts =  tcounts + 1

print('Count:', tcounts)
print('Sum:', sum)
