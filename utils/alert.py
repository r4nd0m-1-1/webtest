import requests

def send_slack_alert(webhook_url, message):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

def create_jira_ticket(api_url, auth, summary, description):
    payload = {
        "fields": {
            "project": {"key": "SEC"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Bug"}
        }
    }
    requests.post(api_url, json=payload, auth=auth)
