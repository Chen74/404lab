import requests
version = requests.__version__
print(version)

print(requests.get("http://google.com/").text)

print(requests.get("https://raw.githubusercontent.com/Chen74/404lab/main/lab1.py").text)
