# requests is not in the standard library and must be install
# pip install requests
import requests 

response = requests.get('https://api.chucknorris.io/jokes/random')

data = response.json()

print("CHUCK NORRIS JOKE")
print(data['value'])