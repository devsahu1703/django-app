import requests
import json 
URL='http://127.0.0.1:8000/admin/Myapp/student/'
# get data
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    jdata = json.dumps(data)
    r = requests.get(url=URL, data=jdata)
    data = r.text
    print(data)
    

# post data 
def post_data():
    data = {'name': 'mayank', 'roll': 12, 'city': 'Lucknow'}
    jdata = json.dumps(data)
    r = requests.post(url=URL, data=jdata)
    data = r.json()
    print(data)

# update datadef update_data():
    data = {'id': 3, 'name': 'manshi', 'roll': 10}
    jdata = json.dumps(data)
    r = requests.put(url=URL, data=jdata)
    data = r.json()
    print(data)

# delete data
def delete_data():
    data = {'id': 3}
    jdata = json.dumps(data)
    r = requests.delete(url=URL, data=jdata)
    data = r.json()
    print(data)


#  Run
get_data()
