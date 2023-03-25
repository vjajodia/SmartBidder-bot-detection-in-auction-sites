import requests
import random
import time
import ipdb
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/bid/1"

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'en-US,en',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'csrftoken=EBxNXlfu9MyCaF3kP7eCD6YQQNDEgNPj; sessionid=98hbu1a687nnupfc5vdi2z0ebgctupa6; csrftoken=vLihJxU9qQwI3DuKCMIqqRKLcReEAR87',
  'Origin': 'http://127.0.0.1:8000',
  'Referer': 'http://127.0.0.1:8000/details/1',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Sec-GPC': '1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

print("***************")

url2 = "http://127.0.0.1:8000/details/1"

payload2={}

response2 = requests.request("GET", url2, data=payload2)
# ipdb.set_trace()
soup = BeautifulSoup(response2.text, 'html.parser') 
all_values = soup.find_all("div", {"class": "text-center"})
last_bid = all_values.pop()
last_bid_value = float(last_bid.text.split(" ")[2])
print(f"====================\n{last_bid_value = }\n====================")


for i in range(10):
  last_bid_value += round(random.uniform(0.1, 5.0),2)
  print(last_bid_value)
  payload=f"csrfmiddlewaretoken=8LKJIfg0XpuyR8WP7sgFVK3W6pCHvjeNCc7mvqlkW1S0RDPZMpk7oGRCM25bBWTW&bid={last_bid_value}&record=62399%2C0.133801%2C0.777108%2C0.691033%2C0.043191"
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  time.sleep(1)
  i+=1
print("***************")



