import requests
from bs4 import BeautifulSoup

url = 'https://haken.ca-ss.jp/'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)
