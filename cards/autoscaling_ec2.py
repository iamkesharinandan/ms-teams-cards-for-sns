

def launch_new_ec2(message):
    return {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": message['detail']['Destination'] + ' - ' + message['detail']['Description'],
        "sections": [{
            "activityTitle": message['detail']['Destination'] + ' - ' + message['detail']['Description'],
            "activitySubtitle": message['detail']['Cause'],
            "activityImage": "https://sinovi.uk/images/articles/cw.png",
            "facts": [
                {
                    "name": "AutoScalingGroupName:",
                    "value": message['detail']['AutoScalingGroupName']
                },
                {
                    "name": "Availability Zone",
                    "value": message['detail']['Details']['Availability Zone']
                },
                {
                    "name": "Subnet ID",
                    "value": message['detail']['Details']['Subnet ID']
                }
            ],
            "markdown": True
        }]
    }
