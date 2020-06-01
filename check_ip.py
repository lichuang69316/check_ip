# -*- coding: utf-8 -*-
import dns.resolver,requests

# 解析域名
def get_iplist():
    domain = input('请输入域名地址：')
    A = dns.resolver.query(domain, 'A')
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j)

# 对获取的ip，进行请求，检查是否正常，返回状态码
def checkip():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    # 遍历iplist
    for i in range(len(iplist)):
        res = requests.get('http://' + str(iplist[i]),headers=headers)
        print('http://' + str(iplist[i]) + '    ' + str(res))

if __name__ == '__main__':
    # 存放域名解析的ip
    iplist = []
    try:
        get_iplist()
    except:
        print('-----无法解析域名-----')
    checkip()
