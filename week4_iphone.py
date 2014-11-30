__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
import time
import poplib
import smtplib
import email
import mimetypes
from email.mime.text import MIMEText
from email.header import Header


url = 'http://store.apple.com/hk-zh/buy-iphone/iphone6'

sender='a18012784161@139.com'
receiver='a18012784161@139.com'
subject = 'iphone get'
username = 'a18012784161@139.com'
password = 'asdcjw110'


while True:
    req=urllib2.Request(url)
    res=urllib2.urlopen(req)
    i_page=res.read()
    reg='{"dimensionScreensize":"(.*?)","dimensionColor":"(.*?)","dimensionCapacity":"(.*?)","partNumber":".*?","price":"(.*?)","displayShippingQuote":"(.*?)".*?}'
    match=re.compile(reg).findall(i_page)
    for i in match:
        i=i[4].decode('utf-8')
        text=i[0]+i[1]+i[2]+i[3]
        if i[4]!='有货的信息~':


            msg = MIMEText(text,'text','utf-8')
            msg['Subject'] = Header(subject,'utf-8')

            smtp = smtplib.SMTP()
            smtp.connect('smtp.139.com')
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
        else:
            pass;

        time.sleep(5)





