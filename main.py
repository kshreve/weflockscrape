import os
import json
import urllib.request

with open('tileurls.json') as f:
    data = json.load(f)

for url in data:
    splitUrl = url.split('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile')[1]
    filename = splitUrl.split('/')[3]
    folder = 'images' + splitUrl.rsplit('/', 1)[0]
    os.makedirs(folder, exist_ok=True)
    urllib.request.urlretrieve(url, folder+'/'+filename)
    print('got ', url)
