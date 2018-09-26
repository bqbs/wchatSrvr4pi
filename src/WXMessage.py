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
        self.MsgType = msgType

    def make_easy_tag(self, dom, tag_name, value, type='text'):

        tag = dom.createElement(tag_name)

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
        from_user = self.make_easy_tag(dom, 'FromUserName', self.fromUserName)
        root.appendChild(from_user)
        to_user = self.make_easy_tag(dom, 'ToUserName', self.toUserName)
        root.appendChild(to_user)
        # createTime = self.makeEasyTag(dom,'CreateTime')
        # print root.toxml()
        return root.toxml()

    def parse(self, xml):
        pass

    @staticmethod
    def gen(self, fromUser, toUser, content, msgtype):
        """
        :param self:
        :param fromUser:
        :param toUser:
        :param content:
        :param msgtype: 'text','video','shortvideo','location','voice','image','link'
        :return:
        """
        return content


if __name__ == '__main__':
    msg = WXMessage('test', 'testfrom', 'content')
    msg.format()
