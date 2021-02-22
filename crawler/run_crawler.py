from youtube_crawler import search_crawling
import json

with open('./skeleton.json', 'r') as f:
    json_data = json.load(f)

print(json_data.values)
'''
for k,v in json_data.items():
    res = search_crawling(query=json_data[k], max_results=10)
    break
print(res)
'''