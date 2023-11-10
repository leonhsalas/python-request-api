import requests

url = "https://colegiomeze.com/"

response = requests.get(url)

print(response.content)
