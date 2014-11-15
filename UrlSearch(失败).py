__author__ = 'Administrator'
import urllib
import urllib2
import thread
# searchedDomainName

test_data = {'searchedDomainName':'qq'}
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://www.zgsj.com/domain_reg/com.asp"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res.decode("gbk")
#未能打开传送数据后的网页（打开了源码也找不到反馈的地方，，，，）
