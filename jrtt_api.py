import execjs
import urllib.parse
import ast
import time
import json
import requests
import pymysql
import re
from apscheduler.schedulers.background import BackgroundScheduler

class Datajrtts():
    '''获取关键参数as cp _signature'''
    def get_js(self):
        f = open(r"E:\env\新建文件夹\toutiao.js", 'r', encoding='UTF-8')  ##打开JS文件
        line = f.readline()
        htmlstr = ''
        while line:
            htmlstr = htmlstr + line
            line = f.readline()
        ctx = execjs.compile(htmlstr)
        ctx_dict = ast.literal_eval(ctx.call('get_as_cp_signature'))
        return ctx_dict
    def get_url(self,ctx_dict):
        link = 'https://m.toutiao.com/list/'
        data = {
            'tag': '__all__',
            'ac': 'wap',
            'count': 20,
            'format': 'json_raw',
            'as': ctx_dict['as'],
            'cp': ctx_dict['cp'],
            'max_behot_time': int(time.time()),
            '_signature':ctx_dict['_signature'],
            'i': int(time.time())
        }
        url = link + '?' + urllib.parse.urlencode(data)
        return url
    def main(self):
        '''数据解析  必须加cookie'''
        headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
            'Host': 'm.toutiao.com',
            'Cookie': 'UM_distinctid=1692f0f1e9b3ec-0aca14f41e04d3-57b143a-100200-1692f0f1e9c6f1; tt_webid=6662665576944551437; csrftoken=eeb2e2ed3a37146509e4b5a64a94be8b; _ga=GA1.2.1927407303.1553858466; _ba=BA0.2-20190329-51225-lXjfdx88Q2hnV4e1Raa8'
        }
        f = Datajrtts()
        data = {}
        urls = []
        i = 0
        datas = []
        while i != 1:   #获取url  每个一秒获取一次
            s = f.get_js()
            time.sleep(1)
            j = f.get_url(s)
            # print(j)
            urls.append(j)
            i = i+1
        print(urls)
        for j in urls:
            response = requests.get(j,headers=headers)
            text = response.text
            bodys= json.loads(text)
            for a in bodys['data']:
                s = str(a)
                media_name_re = re.search(r'media_name', s)  #防止广告信息报错终止运行
                if media_name_re != None:
                    data = {
                        'title': a['title'],
                        'release_time': a['datetime'],
                        'keyword': a['keywords'],
                        'article_id': a['item_id'],
                        'url': 'https://www.toutiao.com/a' + a['item_id'] + '/'
                    }
                    # print(data)
                    datas.append(data)
        return json.dumps(datas)

# s = Datajrtts()
# print(s.main())