import requests

response = requests.get("https://explorer.lichess.ovh/masters/")
print(response.text)