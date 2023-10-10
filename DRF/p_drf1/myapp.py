# create myapp.py for sending requesting and receiving response 

'''import requests
URL = "http://127.0.0.1:8000/stuinfo/2"

r = requests.get(url=URL)
data = r.json()
print(data)
'''
# deserialization function
import requests
URL = "http://127.0.0.1:8000/stuinfo1/"
import json
data = {
'name':'Vaidik',
'roll':101,
'city': 'jaipur'}

json_data = json.dumps(data)
r =requests.post(url=URL,data=json_data)

data = r.json()
print(data)