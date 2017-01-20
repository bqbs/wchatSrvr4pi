#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.etree import ElementTree
from flask import Flask
from flask import request
import hashlib
import time
import sys, urllib, json
from WChat import WChat

app = Flask(__name__)
wx = WChat(__name__)


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

    # 如果是来自微信的请求，则回复echostr
    if hashcode == signature:
        print(hashcode)
        print(echostr)
        return echostr


@app.route('/wchat', methods=['POST'])
def post_wechat():
    if not request.args:
        return False
    str_xml = request.data
    print(str_xml)
    xml = ElementTree.fromstring(str_xml)  # 进行XML解析
    fromUserContent = xml.find("Content").text  # 获得用户所输入的内容
    msgType = xml.find("MsgType").text
    fromUser = xml.find("FromUserName").text
    toUser = xml.find("ToUserName").text
    content = fromUserContent
    wx.cut(content)
    content = tuling_robot(fromUserContent)

    # 可以对content进行分析  做指令
    return WXMessage.gen(content=content,fromUser=toUser,toUser=fromUser)

@wx.route("help")
def menu():
    return "help"


# tuling robot
def tuling_robot(content):
    url = 'http://apis.baidu.com/turing/turing/turing?key=879a6cb3afb84dbf4fc84a1df2ab7319&info=%s&userid=eb2edb736'
    req = urllib.reqeust.Request(url % content.encode("utf-8"))
    req.add_header("apikey", "d0c1245201bc618440af7c0bf4fa187c")
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        contentinJson = json.loads(content)
        if contentinJson["text"]:
            content = contentinJson["text"]
    return content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
