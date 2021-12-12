import requests, json

url = "https://stellarflyff.com/server-status"

req = requests.get(url)
if req.status_code == 200:
	data = json.loads(req.content)

	for section in ["data"]:
		for sub_section in ["serverStatus", "serverTime"]:
			print("Server Status: " + data[section][sub_section])