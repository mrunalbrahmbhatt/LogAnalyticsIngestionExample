# This script sends log data to Azure Log Analytics workspace.
# It constructs a JSON payload, creates an HMAC SHA256 signature for authentication,
# and sends the data via an HTTP POST request.

import hashlib
import hmac
import base64
import json
import time
import os
from datetime import datetime
import requests


# Get the current directory (the folder where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the config file
config_file_path = os.path.join(current_directory, 'config.json')
# Read credentials from config file
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

workspace_id = config['workspace_id']
shared_key = config['shared_key']
log_type = config['log_type']

# Current time in UTC
current_time = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
#print(current_time)
utc_time = datetime.utcnow().isoformat()

# Log data to send (example JSON format)
logs_data = [
    {
        "eventId": "12345",
        "eventType": "UserLogin",
        "userId": "user1@example.com",
        "sourceIp": "192.168.1.1",
        "location": "New York, USA",
        "device": "Windows 10",
        "browser": "Chrome"
    },
    {
        "eventId": "12346",
        "eventType": "FileDownload",
        "userId": "user2@example.com",
        "sourceIp": "192.168.1.2",
        "location": "San Francisco, USA",
        "device": "MacOS",
        "browser": "Safari"
    },
    {
        "eventId": "12347",
        "eventType": "UserLogout",
        "userId": "user3@example.com",
        "sourceIp": "192.168.1.3",
        "location": "Chicago, USA",
        "device": "Linux",
        "browser": "Firefox"
    }
]

for entry in logs_data:
    entry["TimeGenerated"] = current_time  # utc_time

# Convert log data to JSON
json_data = json.dumps(logs_data)

# Construct the message for HMAC
request_uri = "/api/logs"
content_length = str(len(json_data))
signature_string = f"POST\n{content_length}\napplication/json\nx-ms-date:{current_time}\n{request_uri}"

# Create the HMAC SHA256 hash signature
encoded_signature = base64.b64encode(hmac.new(
    base64.b64decode(shared_key),
    signature_string.encode('utf-8'),
    hashlib.sha256
).digest()).decode('utf-8')

# Prepare the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f"SharedKey {workspace_id}:{encoded_signature}",
    'x-ms-date': current_time,
    'Log-Type': log_type,
    'Content-Length': content_length
}

# Log Analytics URL
url = f"https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01"
#print(json_data)

# Send the HTTP POST request
response = requests.post(url, headers=headers, data=json_data)

# Check the response
print(response.status_code)
print(response.text)
