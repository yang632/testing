# -*- encoding: utf-8 -*-
# File    : service
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 16:54
import time
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
        # url='http://47.96.74.65:8080/WoniuBoss4.0/login'
        driver.get(url)
        time.sleep(3)

    #输入内容
    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    # 判断某个元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True



if __name__ == '__main__':
    driver =Service.get_driver()
    Service.open_startpage(driver)