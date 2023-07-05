import requests
from bs4 import BeautifulSoup

# url = 'https://www.ptt.cc/'
# web = requests.get('https://www.ptt.cc/bbs/Japan_Travel/index.html', cookies={'over18':'1'})
# soup = BeautifulSoup(web.text, "html.parser")
# titles = soup.find_all('div', class_='title')     # 取得 class 為 title 的 div 內容
# for i in titles:
#     if i.find('a') != None:                         # 判斷如果不為 None
#         print(i.find('a').get_text())                 # 取得 div 裡 a 的內容，使用 get_text() 取得文字
#         print(url + i.find('a')['href'], end='\n\n')  # 使用 ['href'] 取得 href 的屬性

url = "https://udn.com/"
web = requests.get("https://udn.com/news/index")
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all("div", class_="story-list__text")
for i in titles:
    if i.find("a").get_text() != "" or i.find("a").get_text() != None:
        print(i.find("a").get_text())
        print(url + i.find('a')['href'], end="\n\n")