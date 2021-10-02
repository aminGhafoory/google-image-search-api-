
import requests
import json
from tqdm import tqdm

api_key = "Your API Key(get it from provided link)"
cx = "Your CX (get it from provided link)"
query ='bear'#sample query

def google_image_search(api_key: str,cx: str ,query: str) -> None:

    for page in tqdm(range(1,10)):

        start = (page-1)*10 +1
        url = f'https://customsearch.googleapis.com/customsearch/v1?cx={cx}&safe=off&searchType=image&key={api_key}&q={query}&start={start}'
        response  = requests.get(url ,headers={"Accept":"application/json"})
        response_json =json.loads(response.text)
        links = [ response_json['items'][x]['link'] for x in range(len(response_json['items'])) ]
        with open('output.txt','a') as f:
            for i in links:
                f.write(f'{i}\n')


google_image_search(api_key,cx,query)
