import requests

if __name__ == 'main':
    url = 'https://www.colegiomeze.com/'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        file = open('meze.html', 'wb')
        file.write(content)
        file.close()

#Nota este codigo solo se puede ejecutar en Mac