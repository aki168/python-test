import requests
from bs4 import BeautifulSoup
# https://www.google.com/search?q="keyword"&tbm=isch # image search

# 使用者裝置 biw =寬 , bih =高

url = "https://www.google.com/"
keyword = "国士無双 高砂酒造"
web = requests.get("https://www.google.com/search?q={}&tbm=isch&gl=jp&hl=ja".format(keyword))
soup = BeautifulSoup(web.text, "html.parser")
pics = soup.find_all("img")
title = soup.find_all("span")
for i in title:
    print(i.get_text())
for i in pics:
    if "images?" in i['src'] :
        print(i['src'])
#         print(url + i.find('a')['href'], end="\n\n")