#!/usr/bin/env python
# -*- coding: utf_8 -*-
import urllib2
import cStringIO
import time

__author__ = 'Lian'

try:
    import pytesseract
    from PIL import Image
except ImportError:

    print '模块导入错误,请使用pip安装,pytesseract依赖以下库：'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit


def vcode1():
    url = 'http://dota2.vpgame.com/roll/default-captcha.html?v=573c18e1c4eb5'
    while True:
        code = vcode_from_url(url)
        if len(code) >= 4:
            print code
        time.sleep(1)


def vcode_from_url(url):
    file = cStringIO.StringIO(urllib2.urlopen(url).read())
    image = Image.open(file)
    code = pytesseract.image_to_string(image)
    return code


def main():
    vcode1()


if __name__ == '__main__':
    main()