import requests
version = requests.__version__
print(version)

print(requests.get("http://google.com/").text)