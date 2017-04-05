import requests
import json
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = 'https://api.github.com/emojis'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'}

s = requests.Session()
content = s.get(url,headers=headers).content
j_c = json.loads(content)
for key,value in j_c.items():
    with open('%s.png' %key, 'wb') as f:
        try:
            png = s.get(value,headers=headers,timeout=10).content
        except:
            time.sleep(1)
            png = s.get(value,headers=headers,timeout=10).content
        f.write(png)
