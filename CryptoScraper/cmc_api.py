import requests
import json

url = 'https://api.coinmarketcap.com/v1/ticker/'
user_agent_headers = {'user-agent':
                              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}


def get_allcoins():
    r = requests.get(url, headers=user_agent_headers)
    response = r.json()
    print(json.dumps(response, indent=4, sort_keys=True))
