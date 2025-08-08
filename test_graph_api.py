# Simple script to test an API endpoint
import requests

# Using a public sample endpoint from Microsoft Graph documentation
url = "https://graph.microsoft.com/v1.0/users?$top=5"

try:
    response = requests.get(url)
    print("Request successful!")
    print("Status Code:", response.status_code)
    print("====="
    # print(response.json()) # You can uncomment this to see the data
except Exception as e:
    print("An error occurred:", e)
    
