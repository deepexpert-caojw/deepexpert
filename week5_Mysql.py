__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
import MySQLdb

range=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']

temps = []
result=[]


for t1 in range:
    for t2 in range:
        for t3 in range:
            for t4 in range:
                for t5 in range:
                    for t6 in range:
                      temps.append(t1+t2+t3+t4+t5+t6); temps.append(t1+t2+t3+t4+t5);


filename='result.txt'
file=file(filename,'w')
url = 'http://www.zgsj.com/domain_reg/domaintrans.asp'
for temp in temps:

        values = {'d_name':"%s.com" %temp,
              'dtype':"common",
              'drand':"1416053904465"}
        data = urllib.urlencode(values)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'
        headers = {'User-Agent' : user_agent }

        req = urllib2.Request(url,data,headers)
        response = urllib2.urlopen(req)
        the_page = response.read()

        reg = r"value='([a-zA-Z]+\.com)' checked"

        if re.findall(reg,the_page):
            file.write(str(re.findall(reg,the_page)))
            result.append(re.findall(reg,the_page))
            print str(re.findall(reg,the_page))
            file.write(' ')

        else:
            pass

#导入进数据库


try:
    conn=MySQLdb.connect(host='localhost',user='cjw',passwd='123456',port=3306)
    cur=conn.cursor()

    cur.execute('create database if not exists python')
    conn.select_db('python')
    cur.execute('create table test(URL varchar(20))')
    for t in  result:
        value=[t]
        cur.execute('insert into test values(%s)',value)

    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


file.close()

