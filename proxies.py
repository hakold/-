import requests
from bs4 import BeautifulSoup

url = 'http://www.xicidaili.com/nn/'
for page in range(1,5):
    go_url = url + str(page)
    print(go_url)
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
html = requests.get(url=url,headers=headers,cookies=cookies)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text,'html.parser')

ProxiesIP = []
ProxiesPort = []

for IP in soup.select('tr > td')[1::10]:
    proxyIP = IP.string
    ProxiesIP.append(proxyIP)

for Port in soup.select("tr > td")[2::10]:
    proxyPort = Port.string
    ProxiesPort.append(proxyPort)

f = open("news.txt",'a')
for x in range(0,len(ProxiesIP)):
    k = ProxiesIP[x] + ":" + ProxiesPort[x]
    f.write(k+"\n")
f.close()
