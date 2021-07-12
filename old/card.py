class Card:

    def __init__(self, message):
        self.message = message


    def auto_scaling(self):
        return {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0076D7",
            "summary": self.message['Service'],
            "sections": [{
                "activityTitle": self.message['Service'] + ' - ' + self.message['Description'],
                "activitySubtitle": self.message['Cause'],
                "activityImage": "https://sinovi.uk/images/articles/cw.png",
                "facts": [
                    {
                        "name": "Time:",
                        "value": self.message['Time']
                    },
                    {
                        "name": "AccountId:",
                        "value": self.message['AccountId']
                    },
                    {
                        "name": "Event:",
                        "value": self.message['Event']
                    },
                    {
                        "name": "StatusCode",
                        "value": self.message['StatusCode']
                    },
                    {
                        "name": "Subnet ID",
                        "value": self.message['Details']['Subnet ID']
                    },
                    {
                        "name": "Availability Zone",
                        "value": self.message['Details']['Availability Zone']
                    },
                    {
                        "name": "AutoScalingGroupName",
                        "value": self.message['AutoScalingGroupName']
                    }
                ],
                "markdown": True
            }]
        }

    def alarm(self):
        return {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0076D7",
            "summary": self.message['AlarmDescription'],
            "sections": [{
                "activityTitle": self.message['AlarmName'] + ' - ' + self.message['AlarmDescription'],
                "activitySubtitle": self.message['NewStateReason'],
                "activityImage": "https://sinovi.uk/images/articles/cw.png",
                "facts": [
                    {
                        "name": "StateChangeTime:",
                        "value": self.message['StateChangeTime']
                    },
                    {
                        "name": "AWSAccountId:",
                        "value": self.message['AWSAccountId']
                    },
                    {
                        "name": "Region",
                        "value": self.message['Region']
                    },
                    {
                        "name": "AlarmArn",
                        "value": self.message['AlarmArn']
                    },
                    {
                        "name": "OldStateValue",
                        "value": self.message['OldStateValue']
                    },
                    {
                        "name": "MetricName",
                        "value": self.message['Trigger']['MetricName']
                    },
                    {
                        "name": "Namespace",
                        "value": self.message['Trigger']['Namespace']
                    },
                    {
                        "name": "Period",
                        "value": self.message['Trigger']['Period']
                    },
                    {
                        "name": "EvaluationPeriods",
                        "value": self.message['Trigger']['EvaluationPeriods']
                    },
                    {
                        "name": "ComparisonOperator",
                        "value": self.message['Trigger']['ComparisonOperator']
                    },
                    {
                        "name": "Threshold",
                        "value": self.message['Trigger']['Threshold']
                    },
                ],
                "markdown": True
            }]
        }
