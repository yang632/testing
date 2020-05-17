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


    #打开菜单界面
    @classmethod
    def open_menu(cls,driver,menu_name):
        driver.find_element_by_partial_link_text(menu_name).click()


    #登录执行
    @classmethod
    def ignor_login(cls,driver):
        cls.open_startpage(driver)
        from lib.login import Login
        Login(driver).do_login("WNCD000","woniu123","0000")
    # def ignor_login(cls,driver):
    #     cls.open_startpage(driver)
    #     contents=Utility.get_json("../conf/yang/base.conf")
    #     print(contents)
    #     #添加cookie
    #     driver.add_cookie({'name':'userName','value':contents['USERNAME']})
    #     driver.add_cookie({'name': 'userPass', 'value': contents['USERPASS']})
    #     driver.add_cookie({'name': 'checkcode', 'value': contents['CKECKCODE']})
    #     # driver.add_cookie({'name': 'remember', 'value': contents['REMEMBER']})
    #     cls.open_startpage(driver)




if __name__ == '__main__':
    driver =Service.get_driver()
    Service.ignor_login(driver)