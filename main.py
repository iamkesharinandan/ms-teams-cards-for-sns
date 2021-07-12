#!/usr/bin/python3.8
import json
import logging
import os

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

HOOK_URL = "https://taxbackinternational.webhook.office.com/webhookb2/33b61d5a-b198-4416-b076-f6c845c42477@5512b032" \
           "-e6b6-45ec-bf25-0d19c6304b0e/IncomingWebhook/e9256413dfe74aba88dbe43865251872/92b295e4-ccf6-4051-a9ad" \
           "-a79230429d1c "


def ec2_asg(message):
    return ec2(message['detail'])


def ec2(message):
    details = message['Details']
    theme_color = '808080'
    if 'Event' in message:
        theme_color = '00ff00' if message['Event'] == 'autoscaling:EC2_INSTANCE_LAUNCH' else 'ff0000'
    return {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": theme_color,
        "summary": message['Destination'] + ' - ' + message['Description'],
        "sections": [{
            "activityTitle": message['Destination'] + ' - ' + message['Description'],
            "activitySubtitle": message['Cause'],
            "activityImage": "https://sinovi.uk/images/articles/cw.png",
            "facts": [
                {
                    "name": "AutoScalingGroupName:",
                    "value": message['AutoScalingGroupName']
                },
                {
                    "name": "Availability Zone",
                    "value": details['Availability Zone']
                },
                {
                    "name": "Subnet ID",
                    "value": details['Subnet ID']
                },
                {
                    "name": "StartTime",
                    "value": message['StartTime']
                },
                {
                    "name": "Status",
                    "value": message['StatusCode']
                }
            ],
            "markdown": True
        }]
    }



def lambda_handler(event, context):
    # message = json.loads(event['Records'][0]['Sns']['Message'])
    f = open('terminate_ec2.json', "r")
    message = json.loads(f.read())
    f.close()

    if 'AlarmName' in message:
        alarm_name = message['AlarmName']
        old_state = message['OldStateValue']
        new_state = message['NewStateValue']
        reason = message['NewStateReason']
    elif 'source' in message and message['source'] == 'aws.autoscaling':
        message = ec2_asg(message)
    elif 'Destination' in message and message['Destination'] == 'AutoScalingGroup':
        message = ec2(message)
    elif 'Destination' in message and message['Destination'] == 'EC2':
        message = ec2(message)
    else:
        alarm_name = 'Unknown'
        old_state = 'Unknown'
        new_state = 'Unknown'
        reason = message

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
