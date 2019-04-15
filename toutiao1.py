#coding=utf8
import requests
import json
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup
import html
class Data():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
        'Refer':'https://www.toutiao.com/'
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url,headers=Data.headers)
            # print(response.status_code)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                # self.get_text(soup)
                return soup

        except RequestException:
            print('请求错误',url)

    def get_text(self,soup):
        # global data
        titles = soup.find_all('title')
        for a in  titles:
            title = a.get_text()
        contents = soup.find_all('script')
        content = list(contents[6].stripped_strings)

        for j in content:

            content_data = re.search('&lt;.*/p&gt;', j, re.DOTALL)
            content_data_str = str(content_data.group())
            a = html.unescape(content_data_str)
            data ={
                'b_text':a,
                'a_title': title
            }
            return data
'''一点咨询模块'''
class Datayidian():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url,headers=Datayidian.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                # self.get_text(soup)
                return soup

        except RequestException:
            print('请求错误', url)

    def get_text(self,soup):
        titles = soup.find_all('h2')
        for a in titles:
            title = a.get_text()

        bodys = soup.find_all('div',class_='content-bd')
        for j in bodys:
            s = str(j)
            body = s
            data = {
                'code':200,  #识别码
                'b_text': body,
                'a_title': title
            }
            return data
'''网易订阅模块'''
class Datawangyidy():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data = {}
    def get_url(self,url):
        try :
            response = requests.get(url,headers=Datawangyidy.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text,'lxml')
                return soup
        except RequestException:
            print('请求错误', url)

    def get_text(self,soup):
        titles = soup.find_all('h2')
        for a in titles:
            title_s = list(a.stripped_strings)
            for j in title_s:
                title = j
        bodys = soup.find_all('div', class_='content')
        for s in bodys:
            bodyx = str(s)
            body = re.sub('src=', 'width=700px height=500px src=', bodyx)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data
'''网易新闻模块'''
class Datawangyixw():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url,headers=Datawangyixw.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                return soup
        except RequestException:
             print('请求错误', url)
    def get_text(self,soup):
        titles = soup.find_all('h1')
        for a in titles:
            title = a.get_text()
        bodys = soup.find_all('div', class_='post_text')
        for s in bodys:
            body = str(s)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data
'''凤凰资讯模块'''
class Dataifeng():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data ={}
    def get_url(self,url):
        try:
            response = requests.get(url,headers=Dataifeng.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                return soup
        except RequestException:
            print('请求错误', url)

    def get_text(self,soup):
        titles = soup.find_all('title')
        for i in titles:
            title = i.get_text()
        src = soup.select('head script')[5]  #定位文章位置
        str_src = str(src)
        bodys = re.search(r'<p>.*?</p>.*。</p>', str_src)
        body_s = str(bodys.group())
        body =  re.sub('\\\\','',body_s)
        data = {
            'code': 200,  # 识别码
            'b_text': body,
            'a_title': title
        }
        return data
'''百家号模块'''
class Databj():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url,headers=Databj.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text,'lxml')
                return soup
        except RequestException:
            print('请求错误', url)
    def get_text(self,soup):
        titles = soup.find_all('h1')
        for i in titles:
            title = i.get_text()
        bodys = soup.find_all('div',class_='mainContent')
        for a in bodys:
            bodyx = str(a)
            body = re.sub('<div style="padding-top:[0-9]+\.[0-9]+%">','<div style="padding-top:0%">',bodyx)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data

'''大鱼号模块'''
class Datady():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url,headers=Datady.headers)
            if response.status_code == 200:
                soup = response.text
                return soup
        except RequestException:
            print('请求错误', url)
    def get_text(self,soup):
        src = json.loads(soup)
        s = src['data']
        title = s['title']
        s = src['data']
        bodys = s['body']
        body_s = bodys['text']
        imgs = bodys['inner_imgs']
        img_urls = []
        for i in imgs:
            img_url = i['url']
            img_urls.append(img_url)
        for j in range(0, len(img_urls)):
            body = re.sub('<!--{img:%d}-->' % j, '<img width=700px height=500px src= "%s" >' % img_urls[j], body_s)
            body_s = body

        data = {
            'code': 200,  # 识别码
            'b_text': body,
            'a_title': title
        }
        return data

'''企鹅号模块'''

class Dataqe():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url, headers=Dataifeng.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                return soup
        except RequestException:
            print('请求错误', url)
    def get_text(self,soup):
        titles = soup.find_all('p',class_='title')
        for i in titles:
            title_s = i.stripped_strings
            for j in list(title_s):
                title = j

        bodys = soup.find_all('div', class_='content-box')
        for a in bodys:
            bodyx = str(a)
            body = re.sub('width="100%"', 'width=700px height=500px', bodyx)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data
'''搜狐模块'''

class Datash():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url, headers=Dataifeng.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                return soup
        except RequestException:
            print('请求错误', url)

    def get_text(self,soup):
        titles = soup.find_all('h1')
        for i in titles:
            title_s = i.stripped_strings
            for j in list(title_s):
                title = j
        bodys = soup.find_all('article', class_='article')
        for a in bodys:
            body = str(a)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data
'''趣头条'''
class Dataqtt():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url, headers=Dataifeng.headers)
            response.encoding = 'gbk2312'  # 乱码处理
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')

                return soup
        except RequestException:
            print('请求错误', url)
    def get_text(self,soup):
        titles = soup.find_all('title')
        for i in titles:
            title = i.get_text()
        bodys = soup.find_all('div', class_='content')
        for a in bodys:
            body_s = re.sub('data-src','src',str(a))
            body =  re.sub('data-size="[0-9]+,[0-9]+"', 'width=700px height=500px', body_s)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data


'''时间号'''
class Databtime():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data = {}
    def get_url(self,url):
        try:
            response = requests.get(url, headers=Dataifeng.headers)
            response.encoding = 'gbk2312'  # 乱码处理
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                return soup
        except RequestException:
            print('请求错误', url)
    def get_text(self,soup):
        titles = soup.find_all('h1')
        for i in titles:
            title = i.get_text()
        bodys = soup.find_all('div', class_='content-text')
        for a in bodys:
            body = str(a)
            data = {
                'code': 200,  # 识别码
                'b_text': body,
                'a_title': title
            }
            return data

'''惠头条'''
class Datahtt():


    def get_url(self,url):
        try:
            response = requests.get(url, headers=Datady.headers)
            if response.status_code == 200:
                soup = response.text
                return soup
        except RequestException:
            print('请求错误', url)
    def get_text(self,soup):
        src = json.loads(soup)
        s = src['data']
        title = s['title']

        body = s['content']
        data = {
            'code': 200,  # 识别码
            'b_text': body,
            'a_title': title
        }
        return data



