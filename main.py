import functions_framework
import json
import requests


@functions_framework.http
def slack_relay(request):
    request_json = request.get_json()
    print(request_json)
    message_components = request_json['message'].split('\n')
    webhook_url = message_components.pop(0)
    message = '\n'.join(message_components)
    body = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "A new alert has been received from Domo."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{request_json['name']}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": message,
                    "emoji": True
                },
                "accessory": {
                    "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "View Alert",
                                        "emoji": True
                            },
                    "value": "view_alert_btn",
                    "url": f"https://ninety-io.domo.com/alerts/{request_json['id']}",
                    "action_id": "button-action"
                }
            }
        ]
    }
    res = requests.post(webhook_url, json=body)
    slack_res = f'Response from Slack Webhook URL: {res.status_code}'
    print(slack_res)

    return res.reason, res.status_code
