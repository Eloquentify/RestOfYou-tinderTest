import requests
from pprint import pprint
import json
import time


data = []
def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return  local_filename

    if not url.startswith('http'):
        url = 'http:'+url

    r = requests.get(url,stream=True)
    with open(local_filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename

def randompics(page):
    i = str(page*20+1)
    headers = {
        'authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'viewport-width': '1329',
        'accept': '*/*',
        'referer': 'https://unsplash.com/search/photos/random',
        'authority': 'unsplash.com',
        'accept-version': 'v1',
        'dpr': '2',
    }

    params = (
        ('query', 'random'),
        ('xp', 'search-improved-v2:control'),
        ('per_page', '20'),
        ('page', i),#21
    )
    # print "'"+str(page*20+1)+"'"

    response = requests.get('https://unsplash.com/napi/search/photos', headers=headers, params=params).json()
    photos = response['results']
    #pprint(photos)
    for i,photo in enumerate(photos):
        downloadlink = photo['links']['download']
        url = i+100*page : downloadlink
        pprint(url)
        data.append(url)

# randompics(2)
for i in range(5):
    randompics(i)

outfile = open('picUrls.json', 'w')
json.dump(data, outfile, indent=4)
outfile.close()

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://unsplash.com/napi/search/photos?query=random&xp=search-improved-v2:control&per_page=20&page=21', headers=headers)
