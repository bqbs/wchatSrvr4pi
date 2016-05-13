#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.etree import ElementTree
from flask import Flask
from flask import request
import hashlib
import time

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/wchat', methods=['GET'])
def get_wechat():
    if not request.args:
        return False
    signature = request.args['signature']
    timestamp = request.args['timestamp']
    nonce = request.args['nonce']
    echostr = request.args['echostr']
    # 自己的token
    token = "bqbs"  # 这里改写你在微信公众平台里输入的token
    # 字典序排序
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    # sha1加密算法

    #如果是来自微信的请求，则回复echostr
    if hashcode == signature:
        print hashcode
        print echostr
        return echostr


@app.route('/wchat', methods=['POST'])
def post_wechat():
    if not request.args:
        return False
    str_xml = request.data
    print str_xml
    xml = ElementTree.fromstring(str_xml)  # 进行XML解析
    content = xml.find("Content").text  # 获得用户所输入的内容
    msgType = xml.find("MsgType").text
    fromUser = xml.find("FromUserName").text
    toUser = xml.find("ToUserName").text

    return '<xml><ToUserName><![CDATA['+fromUser+']]></ToUserName>' \
           '<FromUserName><![CDATA['+toUser+']]></FromUserName>' \
           '<CreateTime>$createTime</CreateTime>' \
           '<MsgType><![CDATA['+msgType+']]></MsgType>' \
           '<Content><![CDATA['+content+']]></Content>' \
           '</xml>'


if __name__ == "__main__":
    app.run(host="localhost", port=80, debug=True)