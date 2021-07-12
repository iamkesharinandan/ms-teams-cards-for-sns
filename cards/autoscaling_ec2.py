

def launch_new_ec2_asg(message):
    return launch_new_ec2(message['detail'])


def launch_new_ec2(message):
    details = message['Details']
    return {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
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
