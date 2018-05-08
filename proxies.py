import requests
import random
from bs4 import BeautifulSoup



def get_proxies():
    get_ip_url = 'http://www.xicidaili.com/nn/'
    #Created a hearders
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    #Created a cookies
    cookies = {
    '_free_proxy_session': 'BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTJkZTMzMzIxZDI4MzU0MzI3OTQ5ZjQ5ZDI0YjhiODdkBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWFZN1A5S1VBK3ZGSzdPc29qWm5FUDRtS1RaaWRlM0hWb0RrdjVGcEV5UTA9BjsARg%3D%3D--e39755b2c2a86a28c7385ef55ef0217642514887',
    'Hm_lvt_0cf76c77469e965d2957f0553e6ecf59':'1525508494',
    'Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59':'1525512685'
    }
    html = requests.get(url=get_ip_url,headers=headers,cookies=cookies)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'html.parser')
    #创建一个list以储存代理ip池
    Ip_type_pool = []
    Ip_pool = []
    Port_pool = []
    for get_ip_type in soup.select('tr > td')[5::10]:
        IPType = get_ip_type.text
        Ip_type_pool.append(IPType)
    for get_proxy_IP in soup.select('tr > td')[1::10]:
        proxyIP = get_proxy_IP.string
        Ip_pool.append(proxyIP)
    for get_proxy_Port in soup.select("tr > td")[2::10]:
        proxyPort = get_proxy_Port.string
        Port_pool.append(proxyPort)

#输出到txt文本
# f = open("ProxiePool.txt",'a')
# for x in range(0,len(Ip_type_pool)):
#     k = "\"" + Ip_type_pool[x] + "\"" + ":" + Ip_pool[x] + ":" + Port_pool[x]
#     f.write(k+"\n")
# f.close()

    #将http代理的地址输出到一个list中利用random随机抽取一个到代理中
    proxy_list = []
    for x in range(0,len(Ip_pool)):
        if str(Ip_type_pool[x])=='HTTP':
            k = Ip_pool[x] + ":" + Port_pool[x]
            proxy_list.append(k)

    proxy_ip = random.choice(proxy_list)
    proxies = {"http" : 'http://' + proxy_ip}
    return proxies

def Proxy_accept(headers): #测试获取的代理ip可用性
    headers = headers
    while True : #循环抽取代理，直到抽到可用为止
        proxies = get_proxies()
        test = requests.get("https://www.baidu.com", proxies=proxies, headers=headers)
        if test.status_code == 200: #链接百度，响应码为200时该代理可用
            print('200')
            return True
        else:return False

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

Proxy_accept(headers)
