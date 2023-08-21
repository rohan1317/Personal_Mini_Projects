import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select(".storysitestrlink")
votes = soup.select(".score")


def ckh(link,votes):
    hn = []
    for inx, item in enumerate(link):
        title = link[inx].getText()
        hn.append(title)
    return hn


print(ckh(link, ))
