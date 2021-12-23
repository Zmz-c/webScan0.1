# -*- coding:utf-8 -*-
""""
此文件为sql注入检测测试文件
"""
import tkinter

from poc.SI.spider import Spider, urlv
from poc.SI.sqls import urlV


def sqlScan(url):
    SI = Spider(url, 5)
    SI.sqlvOut()
    return urlv


if __name__ == '__main__':
    new_url=sqlScan("http://www.baidu.com/")
    form = tkinter.Tk()
    form.title("sql检测结果")
    form.geometry('800x600')
    w = tkinter.Label(form, text="SQL注入检测")
    w.pack()
    list1 = tkinter.Listbox(form,width=100)
    for i in urlV:
        list1.insert(0, i)
    h = tkinter.Label(form, text="可能SQL注入")
    list2 = tkinter.Listbox(form,width=100)
    for i in new_url:
        list2.insert(0, i)
    list2.pack()
    h.pack()
    list1.pack()
    form.mainloop()
