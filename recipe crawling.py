import requests
from bs4 import BeautifulSoup
from urllib.request import quote
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
movie_name=input('which movie do you want to watch?')
name=movie_name.encode('gbk')
urll=quote(name)
url='http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+urll
res=requests.get(url, headers=headers)
res.encoding ='gbk'
soup=BeautifulSoup(res.text,'html.parser')
link=soup.find(class_="co_content8").find_all('table')
if link:
    lu = link[0].find('a')['href']
    urlmovie = 'https://www.ygdy8.com/' + lu
    res1 = requests.get(urlmovie)
    res1.encoding = 'gbk'
    soup_movie1 = BeautifulSoup(res1.text,'html.parser')
    urldownload = soup_movie1.find('div',id="Zoom").find('span').find('table').find('a')['href']
    print(urldownload)
else:
    print('没有' + movie_name)