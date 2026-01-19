'''
Two types of modules in python:
    - Built in modules
    - External modules
    
List th all Built in modules: http://docs.python.org /3/py-modindex.html
'''
import math
import os
import mymodule 
import requests

print (math.sqrt(16))
mymodule.hellow()
r = requests.get("https://www.google.com")
print(r.text)