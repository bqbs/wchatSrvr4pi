#!/usr/bin/env python
# coding=utf-8
__author__ = 'Lian'

import xml.dom.minidom


class WXMessage(object):
    """
    '<xml><ToUserName><![CDATA['+fromUser+']]></ToUserName>' \
           '<FromUserName><![CDATA['+toUser+']]></FromUserName>' \
           '<CreateTime>$createTime</CreateTime>' \
           '<MsgType><![CDATA['+msgType+']]></MsgType>' \
           '<Content><![CDATA['+content+']]></Content>' \
           '</xml>'
    """

    def __init__(self, toUserName, fromUserName, content):
        self.toUserName = toUserName
        self.fromUserName = fromUserName
        self.content = content

    def makeEasyTag(selft,dom, tagname, value, type='text'):

        tag = dom.createElement(tagname)

        if value.find(']]>') > -1:
            type = 'text'

        if type == 'text':
            value = value.replace('&', '&amp;')

            value = value.replace('<', '&lt;')

            text = dom.createTextNode(value)
        elif type == 'cdata':
            text = dom.createCDATASection(value)
        tag.appendChild(text)
        return tag

    def parse(self):
        impl = xml.dom.minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'xml', None)
        root = dom.documentElement
        fromUserElement = self.makeEasyTag(dom,'FromUserName',self.fromUserName)
        root.appendChild(fromUserElement)
        toUserElement = self.makeEasyTag(dom,'ToUserName',self.toUserName)
        root.appendChild(toUserElement)
        # createTime = self.makeEasyTag(dom,'CreateTime')
        # print root.toxml()
        return root.toxml()


if __name__ == '__main__':
    msg = WXMessage('test','testfrom', 'content')
    msg.parse()
