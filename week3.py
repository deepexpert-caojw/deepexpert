__author__ = 'Administrator'
import urllib
import urllib2
import re

range=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']

temps = []


for t1 in range:
    for t2 in range:
        for t3 in range:
            for t4 in range:
                for t5 in range:
                    temps.append(t1+t2+t3+t4+t5); temps.append(t1+t2+t3+t4); temps.append(t1+t2+t3); temps.append(t1+t2); temps.append(t1)


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
            print str(re.findall(reg,the_page))
            file.write(' ')

        else:
            pass







file.close()

