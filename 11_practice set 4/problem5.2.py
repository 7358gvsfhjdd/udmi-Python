import requests #pip install requests

a = requests.get("https://api.gethub.com/")
print(a.json())