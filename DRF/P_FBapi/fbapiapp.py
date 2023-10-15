import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
data = {
'name':'Vaidik',
'roll':101,
'city': 'jaipur'}
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# get_data()

def post_data():
    data = {
'name':'Vaidik',
'roll':101,
'city': 'jaipur'}
    headers = {'content-type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,headers = headers, data=json_data)
    if r.status_code == 201:  # Assuming HTTP 201 Created is returned for a successful POST
        print("Data successfully posted.")
    else:
        print("Failed to post data. Status code:", r.status_code)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id':2,
        'name' :' Jack',
        'city' : 'Ranchi'
    }
    json_data = json.dumps(data)

    headers = {'content-type':'application/json'}
    r = requests.put(url = URL, headers = headers, data =json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {'id':2}
    json_data = json.dumps(data)

    headers = {'content-type':'application/json'}
    r = requests.put(url = URL, headers = headers, data =json_data)
    data = r.json()
    print(data)

delete_data()