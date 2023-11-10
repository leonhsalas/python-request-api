import requests

url = "https://colegiomeze.com/"
response = requests.get(url)
    
if response.status_code == 200:


    content = response.content

    file = open("colegiomeze.html", "wb")

    file.write(content)

    file.close()
else:
    print(response.status_code)

#Nota este codigo solo se puede ejecutar en Mac