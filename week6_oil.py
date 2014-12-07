__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
import urllib2
import re
import time



def oil():
    url="http://www.bitauto.com/youjia/suzhou/?WT.srch=1"
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    page=response.read()

    req1=re.compile('class="todayPrice"><strong>(.*?)</strong>(.*?)</span>',re.X)
    req2=re.compile('class="oilNum">(.*?)</span>',re.X)
    match=req1.findall(page)
    match2=req2.findall(page)
    a=0
    for j in match2:
        j=j.decode("utf-8")
        print j
        c= match[a][1].decode('utf-8')
        print match[a][0]+c
        a=a+1



def money():
    url='http://huilv.911cha.com/USDCNY.html'
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    page=response.read()
    req1=re.compile('<p>(.*?)</p>')
    match=req1.findall(page)
    for i in match:
        i=i.decode("utf-8")
        print i


while(True):
    oil()
    money()
    time.sleep(3600)