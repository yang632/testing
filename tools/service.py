# -*- encoding: utf-8 -*-
# File    : service
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 16:54
class Service:
    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)