import json

with open('./skeleton.json', 'r') as f:
    json_data= json.load(f)

skeleton_hashtable={}
for k,v in json_data.items():
    skeleton_hashtable[v] = k
