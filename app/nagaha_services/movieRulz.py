import requests
from bs4 import BeautifulSoup
import urllib3

from app import nagaha_config

def get_telugu_titles():
    # Disable SSL warnings (site uses invalid certs)
    print('gettign movie titles')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = nagaha_config.get_config('MOVIERULZ', 'telugu_URL')
  
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
    }

    # Disable certificate verification
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("div", {"class": "cont_display"})
        titles =  [data.find_all('a')[0].get('title') for data in links]

        words_to_replace = ['Watch', 'Online', 'Free', 'Telugu']
        new_tiles = []
        for each_tiles in titles:
            updated = each_tiles
            for word in words_to_replace:
                updated = updated.replace(word, '')
            updated = updated.replace('  ', ' ')    
            new_tiles.append(updated)
        print(*new_tiles, sep="\n")
        return new_tiles
    return []