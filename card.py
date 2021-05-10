class Card:

    def __init__(self, message):
        self.message = message

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
                        "name": "NewStateValue",
                        "value": self.message['NewStateValue']
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
                        "name": "StatisticType",
                        "value": self.message['Trigger']['StatisticType']
                    },
                    {
                        "name": "Statistic",
                        "value": self.message['Trigger']['Statistic']
                    },
                    {
                        "name": "Unit",
                        "value": self.message['Trigger']['Unit']
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
