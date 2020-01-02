import requests
import io
from bs4 import BeautifulSoup
import json
import sys

words = set()

with io.open('words.txt', 'r', encoding="utf8") as outfile:
  for word in outfile.read().split("\n"):
    words.add(word)


# Tu Dien Viet - Viet
for page in range(1, 379):  # 294 pages
    url = f"https://vdict.com/%5E,3,0,0,{page}.html"

    res = requests.get(url)
    res.raise_for_status()
    # vdict Content-Header encoder isn't set to utf-8 for some reason
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    result_list_node = soup.findAll("div", class_="result-list")[0]
    for node in result_list_node.findAll("a"):
        print(node.contents[0])
        words.add(node.contents[0])

# Tu Dien Viet - Anh
for page in range(1, 294):  # 294 pages
    url = f"https://vdict.com/%5E,2,0,0,{page}.html"
    res = requests.get(url)
    res.raise_for_status()
    # vdict Content-Header encoder isn't set to utf-8 for some reason
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    result_list_node = soup.findAll("div", class_="result-list")[0]
    for node in result_list_node.findAll("a"):
        print(node.contents[0])
        words.add(node.contents[0])


with io.open('words.txt', 'w', encoding="utf8") as outfile:
    outfile.write("\n".join(words))
