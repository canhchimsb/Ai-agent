import requests
from config import NODES

def send_task(node_name, payload):
    url = NODES[node_name] + "/task"
    resp = requests.post(url, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()
