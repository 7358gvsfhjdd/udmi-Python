import requests
#https://docs.python-requests.org/en/latest/index.html

r =  requests.get('https://api.github.com/users/codewithharry')
#jason data contains some data

print(r.text)

with open("codewithharry.txt", "w") as f:
    f.write(r.text)
