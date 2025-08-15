import requests
import json

# The URL of your deployed application's predict endpoint
url = "https://sentiment-api-service-fzdu57t2fa-uc.a.run.app/predict"

# The data you want to send in JSON format
# payload = {"text": "India has decided that it will not tolerate nuclear threats anymore, we won't fall for any blackmail. Our military will decide the time and give fitting response to all acts of terror."}

payload = {"text": "Rented yestarday, what a waste of $20. More low quality badly done car scenes since films were invented."}


# The headers to specify that you're sending JSON
headers = {"Content-Type": "application/json"}

# Make the POST request
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Print the results
print(f"Status Code: {response.status_code}")
print(payload)
print("Response JSON:")
print(response.json())