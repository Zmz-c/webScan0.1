# -*- coding:utf-8 -*-
import sys

from poc.SI import down, urlmanager, sqls
import threading
from urllib.parse import urljoin
from bs4 import BeautifulSoup

"""
#此文件为爬虫文件
#非必要请不要修改
"""

urlv = []


class Spider(object):
    def __init__(self, root, threadNum):  # 初始化文件
        self.urls = urlmanager.UM()  # url管理
        self.download = down.Downloader()  # 文件下载模块
        self.root = root
        self.threadNum = threadNum  # 多线程

    def _judge(self, domain, url): # 域名判断是否存在
        if url.find(domain) != -1:
            return True
        return False

    def _parse(self, page_url, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser')
        _news = self._get_new_urls(page_url, soup)
        return _news

    def _get_new_urls(self, page_url, soup): # 获取注入后的返回链接
        new_urls = set()
        links = soup.find_all('a')  # 从页面中寻找a标签
        for link in links:
            new_url = link.get('href') # a标签的href属性
            new_full_url = urljoin(page_url, new_url)
            if self._judge(self.root, new_full_url):
                new_urls.add(new_full_url)
        return new_urls

    def sqlvOut(self):

        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):  # 启用多线程
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()

                ## sql注入测试
                try:
                    if sqls.sqlCk(new_url): # sql检测脚本
                        print("url:%s 这是可能存在漏洞的" % new_url)
                except:
                    pass

                print("获取到的链接:" + new_url)
                t1 = "链接:" + new_url
                urlv.append(t1)
                t = threading.Thread(target=self.download.download, args=(new_url, _content))
                t.start()
                th.append(t)
            for t in th:
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url, _str["html"])
                self.urls.add_new_urls(new_urls)
