# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:08:11 2018

@author: zhang_yu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.request
def getdata():
#    resultword=[]
#    resultexplain=[]
    result=[]
    for i in range(1,229):
        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        url = 'https://www.hujiang.com/ciku/zuixinyingyusijicihui_'+str(i)+"/"
        print(url)
        # 发起请求
        req = urllib.request.Request(url=url,headers=headers)
        #解析 应答 utf-8解码
        res = urllib.request.urlopen(req)
    #    html = res.read().decode('utf-8')
    #    print(html)
        soup=BeautifulSoup(res,"lxml")
        lilist=soup.find_all('li',class_="clearfix")
#        ul=soup.find("ul")
    #    ul=soup.find(class="sp-rank-content")
        for li in lilist:  
            word = re.findall('[a-zA-Z]+',li.a.get_text())[0]
            pos=re.split('\\.| ',li.span.get_text())[0]
            result.append(word+' '+pos)
            print(word+' '+pos)
            
    file=open('hujiang.txt','w')
    for i in range(len(result)):
#        print(result[i])
        file.write(result[i])
        file.write('\n')
    file.close()
        
getdata()
#import re
