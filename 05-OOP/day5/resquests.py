import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")

# print(response.status_code)
# print(response.headers)
# print(response.json())

# parameters = {"lat": 31.771959, "lon": 35.217018}
# response = requests.get(f"http://api.open-notify.org/iss-pass.json?lat=31.771959&lon=35.217018")
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# print(response.text)

# response = requests.get("http://api.open-notify.org/astros.json")

# Print the content of the response (the data the server returned)
# data = response.json()

# print(data)

parameters = {"category": "music"}
response = requests.get("https://api.chucknorris.io/jokes/random", params=parameters)

res = response.json()

print(res["value"])
