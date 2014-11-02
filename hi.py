# coding=utf-8
__author__ = 'Administrator'
import cPickle as p
class person:

    def __init__(self,name,eaddress,telnum):
        self.name=name
        self.eaddress=eaddress
        self.telnum=telnum
    def printall(self):
        print '姓名:',self.name, '电子邮件地址:',self.eaddress,'电话:',self.telnum
    def readdress(self,address):
        self.eaddress=address
    def ren(self,num):
        self.telnum=num

aa={'cjw':person('cjw','52@qq.com','180')}
def addone(a):
    name=raw_input('增加一个用户，请输入名字')
    eaddress=raw_input('请输入地址')
    telname=raw_input('请输入电话')
    a[name]=person(name,eaddress,telname)
def delone(a):
    name=raw_input('删除一个用户，请输入名字')
    if a.has_key(name)==False:
        print'无法找到改用户'
    else:
        del a[name]
def findone(a):
    name=raw_input('查询一个用户，请输入名字')
    if a.has_key(name)==False:
        print'无法找到该用户'
    else:
        a[name].printall()
def fixone(a):
    print'修改一个用户信息，请输入名字'
    name=raw_input()
    if a.has_key(name)==False:
        print'no body'
    else:
        num=raw_input('请输入新的电话号码')
        a[name].ren(num)
        eaddress=raw_input('请输入新的地址')
        a[name].readdress(eaddress)
def choosetodo(x):
    print'你需要干什么，请选择前面的数字:1增加一个用户 2删除一个用户 3.查询一个用户 4修改一个用户资料,按其它键退出'
    a=raw_input()
    if a=='1':
        addone(x)
        choosetodo(x)
    elif a=='2':
        delone(x)
        choosetodo(x)
    elif a=='3':
        findone(x)
        choosetodo(x)
    elif a=='4':
        fixone(x)
        choosetodo(x)
    else:
        print' 结束'




filename='name.data'
f=file(filename)
ab=p.load(f)
choosetodo(ab)
f.close()
f=file(filename,'w')
p.dump(ab,f)
f.close()
