import requests
from requests.auth import HTTPBasicAuth

from app import nagaha_config

def get_next_train_status(src, dest):
    
    url = nagaha_config.get_config('RTT','train_status_endpoint')
    url = url.format(src, dest)
    print ("sending api requets tp {}".format(url))

    # Send GET request with basic auth
    response = requests.get(url, auth=HTTPBasicAuth(nagaha_config.get_sercret('RTT', 'username'),
                                                    nagaha_config.get_sercret('RTT', 'password')))

    if response.status_code == 200:
        reply = response.json()
        services = reply.get('services')
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)

