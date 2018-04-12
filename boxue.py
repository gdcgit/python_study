# -*- coding: utf-8 -*-
# number = 1
# sum = 0
# ji = 1
# while number <= 10:
#     # print("当前是{}".format(number))
#     if number % 2 == 0:
#         sum += number
#     elif number % 2 == 1:
#         ji *= number
#     number += 1
#
# print("偶数的和为{}".format(sum))
# print("奇数的积为{}".format(ji))
# print("程序结束")

# import func
# func.say()

# from func import say
# say()


# def add(x, y):
#     try:
#         sum = x + y
#         print(sum)
    # except Exception as e:
    #     print(e)
    # except:
    #     print(" 输入有误")


# if __name__ == '__main__':
#     add("123", 2)
#     add(1, 3)

#############################
# 获取网页内容
# import requests
# response = requests.get('http://www.baidu.com')
# response.encoding = "utf-8"  # 指定response.text的编解码方式
# print(response.text)  # response.text来获取网页的html字符串
#
# # response.content是一个bytes类型的字符串
# print(response.content.decode())

#############################
# 获取百度首页的logo图片，保存到本地
# import requests
# r = requests.get('https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png?where=super')
# f = open("baidu.png", "wb")
# f.write(r.content)
# f.close()

#############################
# import requests
# headers = {"User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
# r = requests.get('http://www.baidu.com', headers=headers)
# print(r.content.decode())

#############################
# import requests
# import json
# import sys
# # 实现在终端输入内容，
# trans_str = sys.argv[1]
#
# # trans_str = input("输入要翻译的内容：")
#
# # 找到post的url地址，和post的数据
# # post_url = "http://fanyi.baidu.com/v2transapi"  #网页版，现在爬不了了
# post_url = "http://fanyi.baidu.com/basetrans"
#
# post_data = {
#     "from": "zh",
#     "to": "en",
#     "query": trans_str,
#     "transtype": "translang",
#     "simple_means_flag": "3",
#     "sign":"548627.834594",
#     "token":"b7d56934f4182f06fc13be30dbba6067"
# }
# # headers = {"User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
# headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
# # 发送请求，获取响应
# r = requests.post(post_url, data=post_data, headers=headers)
# # 提取数据，展示出来
# dict_response = json.loads(r.content.decode())
# re = dict_response["trans"][0]["dst"]
# print("翻译的结果是：{}".format(re))

#############################
# 登录人人网
# import requests
#
# session = requests.session()
#
# # post_url = "http://www.renren.com/PLogin.do"
# post_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201830145333"
# post_data = {"email": "gaoloveyoufover@163.com", "password": "gao6245462"}
# headers = {"User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
#
# session.post(post_url, data=post_data, headers=headers)
#
# r = session.get("http://zhibo.renren.com/top")
# f = open("renren1.html", "w", encoding="utf-8")
# f.write(r.content.decode())
# f.close()

#############################
# 一次请求失败，可以使用retry再次发送请求
# import requests
# from retrying import retry
#
# headers = {"User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
#
#
# @retry(stop_max_attempt_number=3)
# def _parse_url(url):
#     print("*"*100)
#     r = requests.get(url, headers=headers, timeout=5)
#     assert r.status_code == 200
#     return r.content.decode()
#
#
# def parse_url(url):
#     try:
#         html = _parse_url(url)
#     except Exception as e:
#         print("报错了：", e)
#         html = None
#     return html
#
#
# if __name__ == '__main__':
#     html = parse_url("www.baidu.com")  # 使用错误的url查看retry的效果
#     if html is None:
#         print("请求不成功")
#     else:
#         print("请求成功了")

#############################
import json
import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36",
    "Referer": "https://m.douban.com/tv/american"
}


@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print(url)
    print("*"*100)
    r = requests.get(url, headers=headers, timeout=5)
    print(r)
    assert r.status_code == 200
    return r.content.decode()


def parse_url(url):
    try:
        html = _parse_url(url)
    except Exception as e:
        print("报错了：", e)
        html = None
    return html


def get_url_list():
    # url_list = [
    #     "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_classic_hot/items?os=android&for_mobile=1&start={}&count=18",
    #     "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_occident_hot/items?os=android&for_mobile=1&start={}&count=18"
    # ]
    url_list = [
        {
            "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_classic_hot/items?os=android&for_mobile=1&start={}&count=18",
            "classify": "JD"
        },
        {
            "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_occident_hot/items?os=android&for_mobile=1&start={}&count=18",
            "classify": "OM"
        }
    ]
    return url_list


def get_content_list(json_response):
    dict_response = json.loads(json_response)
    content_list = dict_response["subject_collection_items"]
    total_num = dict_response["total"]
    return content_list, total_num


def save_content_list(content_list):
    for content in content_list:
        print(content)
        print("*"*100)


def run():
    # 1. url_list 待请求的临时的url地址
    url_list_temp = get_url_list()
    for temp in url_list_temp:
        number = 0
        total_num = 100
        while number <= total_num+18:
            url = temp["url_temp"].format(str(number))
            # 2. 发送请求，获取响应
            json_response = parse_url(url)
            # 3. 提取数据
            content_list, total_num = get_content_list(json_response)
            # 4. 保存
            for content in content_list:
                content["classify"] = temp["classify"]
            save_content_list(content_list)
            number += 18


if __name__ == '__main__':
    run()
