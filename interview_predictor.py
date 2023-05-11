import requests # lib used for making HTTP requests
import json # lib used for working with JSON objects

url = 'http://127.0.0.1:5000/predict?level=Junior&lang=Java&tweets=yes&phd=no'

response = requests.get(url)

# check the response's status code

print('status code:', response.status_code)

if response.status_code == 200:
    json_object = json.loads(response.text)
    print(json_object)
    
