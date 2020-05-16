'''觀光最新消息寫入文件'''
from bs4 import BeautifulSoup
import requests
import codecs

r1 = requests.get(
    "https://www.taiwan.net.tw/m1.aspx",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    },
    params={
        "sNo":"0001001"
      }
)

b1=BeautifulSoup(r1.text,"html.parser")
# a1=b1.find_all("a",{"class":"columnBlock-title"})
# for a2 in a1:
#     print(a2.text)
# a1=b1.find_all("span",{"class":"date"})
# for a2 in a1:
#     print(a2.text)
# a1=b1.find_all("div",{"class":"columnBlock-info"})
# for a2 in a1:
#     print(a2.find("span",{"class":"date"}).text,end="\t")
#     print(a2.find("a",{"class":"columnBlock-title"}).text)
fn=1
a1=b1.find_all("div",{"class":"columnBlock-info"})
for a2 in a1:
    title=a2.find("a",{"class":"columnBlock-title"})
    date=a2.find("span",{"class":"date"})
    if title.attrs["href"].find("m1.aspx")!=-1:
        r2=requests.get(
            "https://www.taiwan.net.tw/"+title.attrs["href"],
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
                "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            }
        )
        b2=BeautifulSoup(r2.text,"html.parser")
        with codecs.open("html/"+str(fn)+".txt","w","utf-8") as f:
            f.write(title.text+"\r\n")
            f.write(date.text+"\r\n\r\n")
            f.write(b2.find("div",{"class":"content"}).find("p").text)
            fn+=1
