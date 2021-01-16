import telegram
import telepot
from bs4 import BeautifulSoup # html 분석
import requests # html 가져오는 라이브러리

req = requests.get("http://ncov.mohw.go.kr/")
# print(req.text)
req.raise_for_status()

soup = BeautifulSoup(req.text, "html.parser") # 분석하는 방법 명시 parsing
# print(soup)

국내, 해외 = soup.find("div", class_="liveNum_today_new").find_all("span", class_="data")
print(국내.text, 해외.text)

a = 국내.text 
a = a.replace(',','')

합계 = int(a) + int(해외.text)
# print(합계)

코로나 = "[코로나 발생 현황]" + "\n-국내 발생 : " + 국내.text + "\n-해외 발생 : " + 해외.text + "\n-합계 : " + str(합계)
print(코로나)

# 텔레그램 봇 구동

token = "1409195797:AAFv2WmJOm3zjJUuDYKeKkdSLgTiwvV6Fg8" 
mc = "454953244"
bot = telepot.Bot(token)
bot.sendMessage(chat_id = '@covid_19_now', text = 코로나)    



 
