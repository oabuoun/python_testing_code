import requests

request_bbc = requests.get("https://www.bbc.co.uk")

print("----------- The status_code -----------")
print(request_bbc.status_code)
input()

print("----------- The content ---------------")
print(request_bbc.content)
