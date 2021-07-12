#!/usr/bin/python3.8
import json
import logging
import os
import cards.autoscaling_ec2 as ec2

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

HOOK_URL = "https://taxbackinternational.webhook.office.com/webhookb2/33b61d5a-b198-4416-b076-f6c845c42477@5512b032" \
           "-e6b6-45ec-bf25-0d19c6304b0e/IncomingWebhook/e9256413dfe74aba88dbe43865251872/92b295e4-ccf6-4051-a9ad" \
           "-a79230429d1c "


def lambda_handler(event, context):
    # message = json.loads(event['Records'][0]['Sns']['Message'])
    f = open('launch_ec2.json', "r")
    message = json.loads(f.read())
    f.close()
    original_message = message

    if 'AlarmName' in message:
        alarm_name = message['AlarmName']
        old_state = message['OldStateValue']
        new_state = message['NewStateValue']
        reason = message['NewStateReason']
    elif 'source' in message and message['source'] == 'aws.autoscaling':
        alarm_name = message['detail']['AutoScalingGroupName']
        old_state = 'N/A'
        new_state = message['detail']['Description']
        reason = message['detail']['Cause']
    else:
        alarm_name = 'Unknown'
        old_state = 'Unknown'
        new_state = 'Unknown'
        reason = message

    data = {
        "colour": "64a837",
        "title": "**%s** is resolved" % alarm_name,
        "text": "**%s** has changed from %s to %s - %s" % (alarm_name, old_state, new_state, reason)
    }

    if new_state.lower() == 'alarm':
        data = {
            "colour": "d63333",
            "title": "Red Alert - There is an issue %s" % alarm_name,
            "text": "**%s** has changed from %s to %s - %s" % (alarm_name, old_state, new_state, reason)
        }

    message = {
        "@context": "https://schema.org/extensions",
        "@type": "MessageCard",
        "themeColor": data["colour"],
        "title": data["title"],
        "text": data["text"]
    }

    f = open('ex.json', "r")
    message = json.loads(f.read())
    f.close()
    message = ec2.launch_new_ec2(original_message)
    req = Request(HOOK_URL, json.dumps(message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        return {"status": "200 OK"}
    except HTTPError as e:
        print("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        print("Server connection failed: %s", e.reason)


if __name__ == '__main__':
    e = ''
    c = ''
    lambda_handler(e, c)
