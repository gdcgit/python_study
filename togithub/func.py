# -*- coding: utf-8 -*-
def say():
    print("hello world")


class Cat:

    def __init__(self, name="miao", color="black"):
        self.cat_name = name
        self.cat_color = color

    def eat(self):
        print("{}在吃肉。。。".format(self.cat_name))

    def drink(self, drinks):
        print("妙哉喝{},颜色{}".format(drinks, self.cat_color))
        return True


if __name__ == "__main__":
    # print("这是func.py中的一个打印语句")
    my_cat = Cat("小猫", "倦色")  # 实例化
    my_cat.eat()
    is_alive = my_cat.drink("可口")
    if is_alive:
        print("我的喵还活着")
    else:
        print("我的喵死了")
    print(my_cat.cat_name)
    print(my_cat.cat_color)
