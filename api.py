import requests
import json

# API endpoint URL
url = "https://api.example.com/data"  # Replace with your API URL

# Optional: Add parameters (query string)
params = {"key1": "value1", "key2": "value2"}

# Optional: Add headers (e.g., for authentication or content type)
headers = {"Content-Type": "application/json"}


try:
    response=requests.get(url,params=params,headers=headers)
    response.raise_for_status()
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
