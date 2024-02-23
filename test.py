import requests

url = "https://api.fullmetal.ai/prompt"

payload = "{\r\n    \"prompt\": \"Hi\",\r\n    \"model\": \"7B\"\r\n}"
headers = {
  'apikey': 'fk-sk-MC4yTYOaqLzdQWOWhpAd'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)