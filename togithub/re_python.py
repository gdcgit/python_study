# -*- coding: utf-8 -*-
# import re
#
# m = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
#
# print(m.group())
#
# m = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>')
#
# print(m.group())
#
# str0 = "python 123";
# m = re.search(r'\d+', str0)
# print(m.group())
#
# str1 = "c++=100, java=90, python=80";
# m = re.findall(r'\d+', str1)
# print(sum([int(x) for x in m]))
#
# str2 = "imooc video = 1000"
# info = re.sub(r'\d+', '10001', str2)
# print(info)
#
#
# def add1(match):
#     val = match.group()
#     num = int(val) + 1
#     return str(num)
#
#
# str3 = "imooce video 1009"
# info = re.sub(r'\d+', add1, str3)
# print(info)
#
#
# str4 = "imooc: c c++ python"
# info = re.split(r':| ', str4)
# print(info)
#
# str5 = "imooc: c c++ java, python"
# info = re.split(r':|,', str5)
# print(info)
# info = re.split(r':| |,', str5)
# print(info)


#获取图片

import re
import urllib.request

resp = urllib.request.urlopen("https://www.imooc.com/course/list")

buf = resp.read()

html = buf.decode('utf-8')

list_url = re.findall(r'src=.+\.jpg', html)

# print(list_url)

j = 0
for i in list_url:
    r = re.sub(r'src="', 'http:', i)
    f = open(str(j) + '.jpg', 'wb')
    req = urllib.request.urlopen(r)
    buf = req.read()
    f.write(buf)
    j += 1

