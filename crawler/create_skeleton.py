import json
import os
from utils import loggings

file_path = '/Users/alegro/MusicTub/data/melonDB'
file_name = 'song_meta.json'

mylog = loggings.get_logger('Progress')
skeleton = {}

mylog.info('read melon data')
with open(os.path.join(file_path, file_name)) as f:
    json_data = json.load(f)

mylog.info('create skeleton data')
for data in json_data:
    skeleton[data['id']] = data['song_name']

mylog.info('save skeleton data')
with open('skeleton.json', 'w') as f:
    json.dump(skeleton, f)

