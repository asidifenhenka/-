from flask import *
from flask import request,Flask, jsonify
from toutiao1 import *
from flask_cors import CORS   #



from jrtt_api import *


app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/_add_numbers', methods=['GET', 'POST'])
def add_numbers():
    # url = request.args.get('a', 0, type=str)
    url = request.form.get('a', 0, type=str)

    db_tt = Data()   #今日头条
    db_yd = Datayidian() #一点资讯
    db_wy_dy = Datawangyidy() #网易订阅
    db_wy = Datawangyixw()  #网易新闻
    db_if = Dataifeng()  #凤凰资讯
    db_bj = Databj()  #百家号
    db_dy = Datady() #大鱼号
    db_qe = Dataqe() #企鹅号
    db_sh = Datash()#搜狐
    db_qtt = Dataqtt()#趣头条
    db_btime = Databtime() #时间号
    db_htt = Datahtt()  #惠头条


    link_tt  = re.match('http(s?)://www\.toutiao\.com/[a-z][0-9]+/', url)    #今日头条url验证
    link_yd = re.match(r'http(s?)://www\.yidianzixun\.com/article/[0-9A-Za-z]+', url) #一点资讯url验证
    link_wy_dy = re.match(r'http(s?)://dy\.163\.com/[0-9a-z]+/[0-9a-z]+/[0-9a-z]+/[A-Z0-9]*\.html',url)   #网易订阅url验证
    link_wy = re.match(r'http(s?)://[^dy]+\.163\.com/[0-9a-z]+/[0-9a-z]+/[0-9a-z]+/[A-Z0-9]*\.html',url)  #网易新闻url验证
    link_if = re.match(r'http(s?)://[a-z]+\.ifeng\.com/[a-z]/[0-9a-zA-Z]+',url)  #凤凰资讯url验证
    link_bj = re.match(r'https://mbd.baidu.com/[a-z]+/[a-z]+/landingshare\?context=%7B%22nid%22%3A%22news_[0-9]+%22%2C%22sourceFrom%22%3A%22bjh%22%7D',url) #百家号
    link_dy = re.match(r'http(s?)://[a-z]+\.[a-z]+\.uc\.cn/article\.html\?uc_param_str=frdnsnpfvecpntnwprdssskt',url)  #大鱼号
    link_qe = re.match(r'http(s)?://kuaibao.qq.com/[a-z]+/[0-9A-Za-z]+',url) #企鹅号
    link_sh = re.match(r'http(s)?://www.sohu.com/[a-z]+/\w+',url)  #搜狐
    link_qtt = re.match(r'http(s)?://html2.qktoutiao.com/[a-z]+/[0-9]+/[0-9]+/[0-9]+/[0-9]+.html',url)  #趣头条
    link_btime = re.match(r'http(s)?://item.btime.com/\w+',url)  #时间号
    link_htt = re.match(r'http(s)?://h5\.cp\.cashtoutiao\.com/[a-z]+/[a-z]+/detail\?id=[0-9]+',url)  #惠头条

    if link_tt != None:
            soup = db_tt.get_url(url)
            text = db_tt.get_text(soup)
            return jsonify(text)
    elif link_yd != None:
            soup = db_yd.get_url(url)
            text = db_yd.get_text(soup)
            return json.dumps(text)
    elif link_wy_dy != None:
            soup = db_wy_dy.get_url(url)
            text = db_wy_dy.get_text(soup)
            return json.dumps(text)
    elif link_wy != None:
        soup = db_wy.get_url(url)
        text = db_wy.get_text(soup)
        return json.dumps(text)
    elif link_if != None:
        soup = db_if.get_url(url)
        text = db_if.get_text(soup)
        return json.dumps(text)
    elif link_bj != None:
        soup = db_bj.get_url(url)
        text = db_bj.get_text(soup)
        return json.dumps(text)
    elif link_dy != None:
        link_a = re.search(r'wm_aid=[a-z0-9]+',url)
        s = str(link_a.group())
        j = re.sub('wm_aid=','',s)
        link_b = 'http://ff.dayu.com/contents/origin/'+ str(j) + '?biz_id=1002&_fetch_author=1&_incr_fields=click1,click2,click3,click_total,play,like'
        soup = db_dy.get_url(link_b)
        text = db_dy.get_text(soup)
        return json.dumps(text)

    elif link_qe != None:
        soup = db_qe.get_url(url)
        text = db_qe.get_text(soup)
        return json.dumps(text)
    elif link_sh != None:
        soup = db_sh.get_url(url)
        text = db_sh.get_text(soup)
        return json.dumps(text)

    elif link_qtt != None:
        soup = db_qtt.get_url(url)
        text = db_qtt.get_text(soup)
        return json.dumps(text)

    elif link_btime != None:
        soup = db_btime.get_url(url)
        text = db_btime.get_text(soup)
        return json.dumps(text)

    elif link_htt != None:
        link_a = re.search(r'id=[0-9]+',url)
        link_b = 'https://api.admin.cp.cashtoutiao.com/headLine/h5Api?'+link_a.group()+'&userId=&showPosition=&showSource=&relatedArticleID=&versionName=&platform=&serkey=&channelType='
        soup = db_htt.get_url(link_b)
        text = db_htt.get_text(soup)
        return json.dumps(text)

    else:
        a = {'code':500,'reason':'目前仅支持今日头条、一点资讯、网易新闻、网易订阅、凤凰资讯、大鱼号、百家号、搜狐、趣头条、时间号、惠头条'}
        return jsonify(a)


@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/s', methods=['GET', 'POST'])
def jrttApi():

    jrtt = Datajrtts()

    return jrtt.main()

if __name__ == '__main__':
    app.run(host='',debug=False,threaded=True,port=50050)   #threaded=True  启用多线程  但是debug 必须是false

    # WSGIServer(('', 50050), app).serve_forever()
    # http_server = WSGIServer(('', 50050), app)
    # http_server.serve_forever()