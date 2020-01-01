import requests
import io
from bs4 import BeautifulSoup
import json
import sys

words = set()

for page in range(1,32): # 32 pages
    url = f"https://vdict.com/a%5E,2,0,0,{page}.html"

    res = requests.get(url)
    res.raise_for_status()
    res.encoding = res.apparent_encoding # vdict Content-Header encoder isn't set to utf-8 for some reason
    soup = BeautifulSoup(res.text, "html.parser")
    result_list_node = soup.findAll("div", class_="result-list")[0]
    for node in result_list_node.findAll("a"):
    	print(node.contents[0].encode("utf8").decode("utf8"))
    	words.add(node.contents[0])


with io.open('words.txt', 'w', encoding="utf8") as outfile:
    outfile.write("\n".join(words))