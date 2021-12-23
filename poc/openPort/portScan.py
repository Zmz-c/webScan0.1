#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from socket import *
import threading

# 线程锁

lock = threading.Lock()
openNum = 0
threads = []
openport = []
endport = []


def portScanner(host, port):
    global openNum
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        openport.append(port)
        openNum += 1
        lock.release()
        s.close()

    except:
        pass


def web(url):
    setdefaulttimeout(1)
    for p in range(1, 5000):
        t = threading.Thread(target=portScanner, args=(url, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return openport


if __name__ == '__main__':
    web('www.foxconn.com.cn')
    print("开放的端口:")
    print(openport)
