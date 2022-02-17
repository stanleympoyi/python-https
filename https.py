import requests


url = "https://news.ycombinator.com/"
response = requests.get(url)

print(
    f"your request to {url} came back with status code {response.status_code}")
