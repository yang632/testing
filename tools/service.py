# -*- encoding: utf-8 -*-
# File    : service
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 16:54
from tools.utility import Utility
class Service:
    #获取driver
    @classmethod
    def get_driver(cls):
        from selenium import webdriver
        content=Utility.get_json('../conf/yang/base.conf')
        return getattr(webdriver,content["BROWSER"])()

    #打开首页
    @classmethod
    def open_startpage(cls,driver):
        content=Utility.get_json('../conf/yang/base.conf')
        # print(content)
        url=f"{content['PROTOCOL']}://{content['HOSTNAME']}:{content['PORT']}/{content['PROGRAM']}/"
        driver.get(url)
    #输入内容
    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)


if __name__ == '__main__':
    driver =Service.get_driver()
    Service.open_startpage(driver)