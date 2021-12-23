import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now
from poc.MG import HR
from poc.MG.HR import urls
from poc.SI import Vtest
from poc.SI.spider import urlv
from poc.SI.sqls import urlV
from poc.openPort.portScan import web, openport
from webScan import models
from webScan.models import urlManager, uV

countUrl = []
Vd = []


@login_required(login_url='/login/')
def index(request):
    insterurl(countUrl)
    test_urlNum = urlManager.objects.filter(urlTime__day=now().day).count()
    sql_num = uV.objects.filter(~Q(open_sql='')).count()
    url_num = uV.objects.filter(~Q(open_url='')).count()
    port_num = uV.objects.filter(~Q(open_port='')).count()

    # 这里是返回给前端index.html的数据的数据
    v1_numz = urlManager.objects.filter(urlTime__month=6).count()
    v2_numz = urlManager.objects.filter(urlTime__month=7).count()
    v3_numz = urlManager.objects.filter(urlTime__month=8).count()
    v4_numz = urlManager.objects.filter(urlTime__month=9).count()
    v5_numz = urlManager.objects.filter(urlTime__month=10).count()
    v6_numz = urlManager.objects.filter(urlTime__month=11).count()
    v7_numz = urlManager.objects.filter(urlTime__month=12).count()

    url_numT = url_num
    last5_urlNum = urlManager.objects.filter(urlTime__day=now().day - 5).count()
    last3_urlNum = urlManager.objects.filter(urlTime__day=now().day - 7).count()
    lastm_urlNum = urlManager.objects.filter(urlTime__day=now().month - 3).count()
    qs = urlManager.objects.all()
    url_fz = uV.objects.all()
    return render(request, 'index.html',
                  {'username': request.user, 'test_urlNum': test_urlNum, 'qs': qs, 'sql_num': sql_num,
                   'url_num': url_num, 'last5_num': last5_urlNum, 'last3_urlNum': last3_urlNum,
                   'lastm_urlNum': lastm_urlNum, "port_num": port_num, 'port_numT': json.dumps(port_num),
                   'url_numT': json.dumps(url_numT), 'sql_numT': json.dumps(sql_num),
                   'v1_numz': json.dumps(v1_numz), 'v2_numz': json.dumps(v2_numz), 'v3_numz': json.dumps(v3_numz),
                   'v4_numz': json.dumps(v4_numz), 'v5_numz': json.dumps(v5_numz), 'v6_numz': json.dumps(v6_numz),
                   'v7_numz': json.dumps(v7_numz), 'url_fz': url_fz
                   })


# 敏感目录扫描
def hr(request):
    global webs
    if request.is_ajax():
        data = request.POST
        web = data.get("url")
        countUrl.append(web)
        mgCount(urls, web)
        urls.clear()
        webs = JsonResponse({"data": HR.hul(web)})
    return webs


# 登录功能

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("账号或密码错误,请重试")


# 注销
def outlogin(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


# 插入url数据
def insterurl(list):
    for lis in list:
        obj = models.urlManager.objects.create(url=lis, urlTime=now())
        obj.save()
    return


# 漏洞统计

# sql注入漏洞统计
def VDCount(sql, url):
    for sql in sql:
        obj = models.uV.objects.create(url=url, open_url='', open_sql=sql, open_port='')
        obj.save()
    return


# 敏感目录注入漏洞统计
def mgCount(vurl, url):
    for i in vurl:
        obj = models.uV.objects.create(url=url, open_url=i, open_sql='', open_port='')
        obj.save()
    return


# 端口扫描统计
def portCount(port, url):
    for i in port:
        obj = models.uV.objects.create(url=url, open_url='', open_sql='', open_port=i)
        obj.save()
    return


# 端口扫描
def portscan(request):
    if request.is_ajax():
        data = request.POST
        url = data.get("url")
        countUrl.append(url)
        portCount(openport, url)
        openport.clear()
        return JsonResponse({"data": web(url)})


# sql注入检测
def sqlT(request):
    if request.is_ajax():
        data = request.POST
        url = data.get("url")
        if url is not None:
            countUrl.append(url)
        urlv.clear()
        new_url = Vtest.sqlScan(url)
        VDCount(urlV, url)
        return JsonResponse({"data": new_url, "V": urlV})
