import json

import urllib3

from card import Card

http = urllib3.PoolManager()


def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    msg = message
    card = Card(message)
    if 'AlarmName' in message:
        msg = card.alarm()
    elif 'Service' in message:
        msg = card.auto_scaling()

    url = "incoming webhook url"
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)

    encoded_msg = json.dumps(msg)
    print(encoded_msg)


if __name__ == '__main__':
    lambda_handler('', '')
