import requests

response = requests.get('http://qin.resgain.net/name_list_3.html')

print(response.text)
