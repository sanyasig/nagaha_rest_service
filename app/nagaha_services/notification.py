import requests

from app import nagaha_config

def send_ntfy_message(msg, title='NAGAHA SERVICES'):
   topic = nagaha_config.get_config('NTFY','topic_name')
   print(f"sending message to topic {topic}")
   response = requests.post("https://ntfy.sh/{}".format(topic),
                  data=msg.encode(encoding='utf-8'),
                   headers={"Title": title})
   print(response)

