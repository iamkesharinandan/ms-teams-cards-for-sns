import urllib3
import json
from card import Card

http = urllib3.PoolManager()


def lambda_handler(event, context):
    message = {"AlarmName": "CPU-UTILIZATION_GREATER_THAN_90_FOR_ALL_EC2",
               "AlarmDescription": "This alarms triggers when cpu utilization is greater than 90% for any of the instance",
               "AWSAccountId": "464661424927", "NewStateValue": "ALARM",
               "NewStateReason": "Threshold Crossed: 2 out of the last 2 datapoints [99.90999849997499 (10/05/21 05:54:00), 99.24001266645556 (10/05/21 05:49:00)] were greater than the threshold (90.0) (minimum 2 datapoints for OK -> ALARM transition).",
               "StateChangeTime": "2021-05-10T05:59:23.984+0000", "Region": "EU (Ireland)",
               "AlarmArn": "arn:aws:cloudwatch:eu-west-1:464661424927:alarm:CPU-UTILIZATION_GREATER_THAN_90_FOR_ALL_EC2",
               "OldStateValue": "OK",
               "Trigger": {"MetricName": "CPUUtilization", "Namespace": "AWS/EC2", "StatisticType": "Statistic",
                           "Statistic": "MAXIMUM", "Unit": None, "Dimensions": [], "Period": 300,
                           "EvaluationPeriods": 2, "ComparisonOperator": "GreaterThanThreshold", "Threshold": 90.0,
                           "TreatMissingData": "- TreatMissingData:                    missing",
                           "EvaluateLowSampleCountPercentile": ""}}

    msg = message
    card = Card(message)
    if 'AlarmName' in message:
        msg = card.alarm()

    encoded_msg = json.dumps(msg)
    print(encoded_msg)


if __name__ == '__main__':
    lambda_handler('', '')
