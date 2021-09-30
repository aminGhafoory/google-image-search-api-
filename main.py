
import os
import requests
import json
from tqdm import tqdm

api_key = os.environ['api_key']
cx = os.environ['cx']
query ='bear'

def google_image_search(api_key: str,cx: str ,query: str)->None:

    for page in tqdm(range(1,2)):

        start = (page-1)*10 +1
        url = f'https://customsearch.googleapis.com/customsearch/v1?cx={cx}&safe=off&searchType=image&key={api_key}&q={query}&start={start}'
        response  = requests.get(url ,headers={"Accept":"application/json"})
        response_json =json.loads(response.text)
        links = [ response_json['items'][x]['link'] for x in range(len(response_json['items'])) ]
        with open('output.txt','a') as f:
            for i in links:
                f.write(f'{i}\n')

def save_image_from_url(url):
    img_name = url.split('/')[-1]
    r = requests.get(url, allow_redirects = True)
    with open(img_name,'wb') as f:
        f.write(r.content)



google_image_search(api_key,cx,query)
url_list  = [line.rstrip('\n') for line in open("output.txt",'r')]
