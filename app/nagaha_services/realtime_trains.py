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

    next_trains = []
    if response.status_code == 200:
        reply = response.json()
        services = reply.get('services')
        
        for each_service in services:
            next_trains.append({'STN' : each_service['locationDetail']['description'],
                'Real Time': each_service['locationDetail']['gbttBookedArrival'],
                'Exp Time': each_service['locationDetail']['realtimeArrival']})
        
        print("Success:", next_trains)
    else:
        print("Failed:", response.status_code, response.text)
    
    return next_trains

