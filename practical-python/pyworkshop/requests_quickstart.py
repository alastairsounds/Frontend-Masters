# requests_quickstart.py

import requests

r = requests.get("https://api.github.com/events")

print("status code:", r.status_code)

github_data = r.json()

for item in r:
    print(item)
