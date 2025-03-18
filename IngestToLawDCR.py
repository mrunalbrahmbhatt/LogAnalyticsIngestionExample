# This script authenticates with Azure using client credentials, retrieves a bearer token,
# and sends log data to an Azure Data Collection Rule (DCR) endpoint.
# It includes constants for app ID, app secret, tenant ID, DCR URI, DCR Immutable ID, and table name.
# The script prepares the request body for token retrieval, makes the request to get the bearer token,
# prepares log data with the current time, and sends the log data to the specified DCR endpoint.

import requests
import json
import time
import os
from urllib.parse import quote_plus
from datetime import datetime
import random

# Get the current directory (the folder where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the config file
config_file_path = os.path.join(current_directory, 'dcr.json')
# Read configuration from config.json
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)
#print(config)
app_id = config['app_id']
app_secret = config['app_secret']
tenant_id = config['tenant_id']
DceURI = config['DceURI']
DcrImmutableId = config['DcrImmutableId']
Table = config['Table']
scope = config['scope']

# Prepare the request body for token request
body = {
    "client_id": app_id,
    "scope": "https://monitor.azure.com//.default",
    "client_secret": app_secret,
    "grant_type": "client_credentials",
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# Token request URL
uri = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
# Make the request to get the bearer token
response = requests.post(uri, data=body, headers=headers)
bearer_token = response.json().get("access_token")
#print(bearer_token)
current_time = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
# Log data to send (example JSON format)
# Function to generate random log data
def generate_random_log(event_id):
    event_types = ["UserLogin", "FileDownload", "UserLogout", "PasswordChange", "AccountLockout"]
    locations = ["New York, USA", "San Francisco, USA", "Chicago, USA", "Los Angeles, USA", "Houston, USA", "Seattle, USA"]
    devices = ["Windows 10", "MacOS", "Linux", "iOS", "Android", "Windows 11"]
    browsers = ["Chrome", "Safari", "Firefox", "Edge"]

    return {
        "eventId": str(event_id),
        "eventType": random.choice(event_types),
        "userId": f"user{event_id}@example.com",
        "sourceIp": f"192.168.1.{event_id}",
        "location": random.choice(locations),
        "device": random.choice(devices),
        "browser": random.choice(browsers),
        "TimeGenerated": current_time
    }

# Generate 6 random log entries
logs_data = [generate_random_log(i) for i in range(1, 7)]


# for entry in logs_data:
#     entry["TimeGenerated"] = current_time


# Now send the log entries
# Prepare body and headers for data upload
body = json.dumps(logs_data)

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# URI for sending data
upload_uri = f"{DceURI}/dataCollectionRules/{DcrImmutableId}/streams/Custom-{Table}?api-version=2023-01-01"
#print(upload_uri)
# Upload the log entry
upload_response = requests.post(upload_uri, data=body, headers=headers)

# Output the response and a separator
print(upload_response.status_code)
print(upload_response.text)
