__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
import urllib2
import re
import time
import MySQLdb


def oil():
    conn=MySQLdb.connect(host='localhost',user='cjw',passwd='123456',port=3306)
    cur=conn.cursor()
    conn.select_db('python1')


    url="http://www.bitauto.com/youjia/suzhou/?WT.srch=1"
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    page=response.read()

    req1=re.compile('class="todayPrice"><strong>(.*?)</strong>(.*?)</span>',re.X)
    req2=re.compile('class="oilNum">(.*?)</span>',re.X)
    match=req1.findall(page)
    match2=req2.findall(page)
    cur.execute('insert into week6oil values(%s)',match[0][0])
    conn.commit()
    cur.close()
    conn.close()
    a=0
    for j in match2:
        j=j.decode("utf-8")
        print j
        c= match[a][1].decode('utf-8')
        print match[a][0]+c
        a=a+1



def money():
    conn=MySQLdb.connect(host='localhost',user='cjw',passwd='123456',port=3306)
    cur=conn.cursor()
    conn.select_db('python1')
    cur.execute('create table week6money4(huilv varchar(20)) ')
    url='http://huilv.911cha.com/USDCNY.html'
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    page=response.read()
    req1=re.compile('<p>(.*?)</p>')
    req1=re.compile('<p>美元对人民币汇率：(.*?)</p>')
    match=req1.findall(page)
    match2=req1.findall(page)

    cur.execute('insert into week6money4 values(%s)',match2)
    conn.commit()
    cur.close()
    conn.close()
    for i in match:
        i=i.decode("utf-8")
        print i


try:
 while(True):
     oil()
     money()

     time.sleep(3600)
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])