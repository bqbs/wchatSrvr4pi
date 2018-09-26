#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import hashlib
import json
import urllib
import urllib.request

import WXMessage
from xml.etree import ElementTree

from flask import Flask
from flask import request as freq

from WChat import WChat
import tuling

app = Flask(__name__)
we = WChat(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/wchat', methods=['GET'])
def get_wechat():
    if not freq.args:
        return False
    signature = freq.args['signature']
    timestamp = freq.args['timestamp']
    nonce = freq.args['nonce']
    echostr = freq.args['echostr']
    # 自己的token
    token = "bqbs"  # 这里改写你在微信公众平台里输入的token
    # 字典序排序
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print(hashcode)
    # 如果是来自微信的请求，则回复echostr
    if hashcode == signature:
        print(hashcode)
        print(echostr)
    return echostr


@app.route('/wchat', methods=['POST'])
def post_wechat():
    if not freq.args:
        return False
    str_xml = freq.data
    print(str_xml)
    xml = ElementTree.fromstring(str_xml)  # 进行XML解析
    fromUserContent = xml.find("Content").text  # 获得用户所输入的内容
    msgType = xml.find("MsgType").text
    fromUser = xml.find("FromUserName").text
    toUser = xml.find("ToUserName").text
    content = fromUserContent
    we.cut(content)
    content = tuling_robot(fromUserContent)

    # 可以对content进行分析  做指令
    return 'test'


@we.route("help")
def menu():
    return "help"





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

