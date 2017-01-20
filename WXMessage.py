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

    def __init__(self, toUserName, fromUserName, content, msgType='text'):
        self.toUserName = toUserName
        self.FromUUserName = fromUserName
        self.Content = content
        self.MsgType=msgType

    def makeEasyTag(selft, dom, tagname, value, type='text'):

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

    def format(self):
        impl = xml.dom.minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'xml', None)
        root = dom.documentElement
        fromUserElement = self.makeEasyTag(dom, 'FromUserName', self.fromUserName)
        root.appendChild(fromUserElement)
        toUserElement = self.makeEasyTag(dom, 'ToUserName', self.toUserName)
        root.appendChild(toUserElement)
        # createTime = self.makeEasyTag(dom,'CreateTime')
        # print root.toxml()
        return root.toxml()

    def parse(self, xml):
        pass

    @staticmethod
    def gen(self, fromUser, toUser, content, msgtype):
        '''

        :param self:
        :param fromUser:
        :param toUser:
        :param content:
        :param msgtype: 'text','video','shortvideo','location','voice','image','link'
        :return:
        '''
        pass


if __name__ == '__main__':
    msg = WXMessage('test', 'testfrom', 'content')
    msg.format()
