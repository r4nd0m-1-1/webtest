import requests

def lookup_cve(keyword):
    url = f"https://cve.circl.lu/api/search/{keyword}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json().get("results", [])[:3]
    return []
