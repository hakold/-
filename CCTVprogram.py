import requests
import random
from bs4 import BeautifulSoup


def get_proxies():#获得一个代理ip池
    get_ip_url = 'http://www.xicidaili.com/nn/'
    ## Created a headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    # Created a cookies
    cookies = {
        ##Cookies内容
    }
    html = requests.get(url=get_ip_url, headers=headers, cookies=cookies)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    # 创建一个list以储存代理ip池
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

        # 输出到txt文本
        # f = open("ProxiePool.txt",'a')
        # for x in range(0,len(Ip_type_pool)):
        #     k = "\"" + Ip_type_pool[x] + "\"" + ":" + Ip_pool[x] + ":" + Port_pool[x]
        #     f.write(k+"\n")
        # f.close()

    # 将http代理的地址输出到一个list中利用random随机抽取一个到代理中
    proxy_list = []
    for x in range(0, len(Ip_pool)):
        if str(Ip_type_pool[x]) == 'HTTP':
            k = Ip_pool[x] + ":" + Port_pool[x]
            proxy_list.append(k)
    return proxy_list

def proxy_choice():#在代理ip池中抽取一个代理ip
    proxy_list = get_proxies()
    proxy_ip = random.choice(proxy_list)
    proxies = {"http": 'http://' + proxy_ip}
    return proxies

def Proxy_accept(headers): #测试获取的代理ip可用性
    headers = headers
    while True : #循环抽取代理，直到抽到可用为止
        proxy = proxy_choice()
        test = requests.get("http://tv.cctv.com/lm/bjjt/", proxies=proxy, headers=headers)
        if test.status_code == 200: #链接百度，响应码为200时该代理可用
            print('200')
            return proxy
        else:False


def Realspider(headers):
    headers = headers
    proxy = Proxy_accept(headers)
    cookies = {
        'vjuids' : '4b1473cb.15efc14fce0.0.5e0ad432781ac',
        'wdcid' : '43389ba5a51794c9',
        'wdlast' : '1509550450',
        'vjlast' : '1507467787.1525788713.21',
        'cuid' : 'f84e7146 - 3567 - 6ad5 - 594c - 2a3c2ec467f2 - -1525788717984'
    }
    html = requests.get("http://tv.cctv.com/lm/bjjt/", proxies=proxy, headers=headers, cookies=cookies)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    Program_name = soup.select('li > span > a')
    Program_name = []
    for name in soup.select('li > span > a'):
        changename = name.text
        Program_name.append(changename)
    return Program_name

headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36'
    }
print(Realspider(headers))
