import requests
import json

URL = "http://127.0.0.1:8000/stuinfo/"
r = requests.get(url = URL)
data = r.json()
print(data)

# URL1 = "http://127.0.0.1:8000/stucreate/"
# data1 = { "name": "sayali", "roll": 3, "city": "mumbai"}
# json_data = json.dumps(data1)
# r = requests.post(url =  URL1,data = json_data)
# data1 = r.json
# print(data1)