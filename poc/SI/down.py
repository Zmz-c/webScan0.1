# -*- coding:utf-8 -*-
import requests


class Downloader(object):
    # 获取链接
    def get(self, url):
        r = requests.get(url, timeout=10)  # timeout超时放弃
        if r.status_code != 200: # 返回值不是200放弃
            return None
        _str = r.text
        return _str

    # post方式提交数据
    def post(self, url, data): # 提交构造的数据
        r = requests.post(url, data)
        _str = r.text
        return _str

    # 获取数据
    def download(self, url, html): # 下载构造的数据
        if url is None:
            return None
        _str = {"url": url}
        try:
            r = requests.get(url, timeout=10)
            if r.status_code != 200:
                return None
            _str["html"] = r.text
        except Exception as e:
            return None
        html.append(_str)
