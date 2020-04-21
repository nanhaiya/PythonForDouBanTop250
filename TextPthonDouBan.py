import requests
import re
import urllib
from bs4 import BeautifulSoup

#爬虫豆瓣TOP250,并保存为本地文件

num = 0
while(num<=250):
    string = ""
    url="https://movie.douban.com/top250"
    headers={"User-Agent":"Mozilla/5.0"}
    data={
        "start":num,
        "filter":""
    }
    r=requests.request(method="get",url=url,headers=headers,params=data)
    r=r.text
    soup=BeautifulSoup(r,"html.parser")
    index=r"[\u4e00-\u9fa5]+"
    #仅采集电影名
    # for tag in soup.find_all(attrs={"class":"title"}):
    # for i in soup.find_all(attrs={"class":"title"}):
    #     if re.match(index,i.string) is not None:
    #         print("第", num + 1, "名", end=": ")
    #         print(i.string)
    #         num+=1
    # if num>250:
    #     break

    #采集电影名、原名、描述
    for tag in soup.find_all(attrs={"class": "item"}):
        print("第", num + 1, "名", end=": ")
        number=num+1
        string+="第"+str(number)+"名："
        name=tag.find_all(attrs={"class": "title"})
        for j in name:
            print(j.string,end="/\t")
            string+=j.string+"/\t"
        sc=tag.find_all(attrs={"class": "inq"})
        if len(sc)>0:
            print(sc[0].string)
            string+=sc[0].string+"\r\n"
        else:
            print()
            string+="\r\n"
        num+=1
    #保存为本地文件
    #ab+：文件不存在则创建文件用于读写，文件写入位置于文件最后
    with open(r"F:\laen\lean\python\text\豆瓣TOP250.txt",'ab+') as file:
        file.write(string.encode("utf-8"))
