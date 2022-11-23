import requests
apiUrl = "https://jsonblob.com/api/jsonBlob/1044977445962530816"
r = requests.get(apiUrl)
print(r.text)