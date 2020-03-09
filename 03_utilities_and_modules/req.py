import requests

req = requests.get('https://www.dr.dk')

print(req.text)

#change link to pointing somewhere on your own computer