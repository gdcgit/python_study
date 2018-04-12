# -*- coding: utf-8 -*-
# 利用configparser解析ini文件
import configparser


class cfg(object):

    def __init__(self, orgfile):
        self.orgfile = orgfile
        self.cfg = configparser.ConfigParser()

    def load(self):
        self.cfg.read(self.orgfile)

    def read(self):
        self.load()
        print("=================")
        for section in self.cfg.sections():
            print(section)
            print(self.cfg.items(section))
        print("=================")

    def add_section(self, section):
        self.cfg.add_section(section)

    def add_item(self, section, key, value):
        self.cfg.set(section, key, value)

    def delete_item(self, section, key):
        self.cfg.remove_option(section, key)

    def delete_section(self, section):
        self.cfg.remove_section(section)

    def save(self):
        f = open('imooc.ini','w')
        self.cfg.write(f)
        f.close()


if __name__ == '__main__':
    cfg = cfg('imooc.ini')
    cfg.read()
    cfg.add_section('login')
    cfg.add_item('login', 'time', '2018-04-06')
    cfg.read()
    cfg.add_section('ceshi')
    cfg.add_item('ceshi', 'sss', '2018-06-08')
    cfg.add_item('ceshi', 'sss1', '2018-06-09')
    cfg.read()
    cfg.delete_item('ceshi','sss')
    cfg.read()
    cfg.delete_section('ceshi')
    cfg.read()
    cfg.save()

