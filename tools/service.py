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
        # print(content)
        return getattr(webdriver,content["BROWSER"])()

    #打开首页yang
    @classmethod
    def open_startpage(cls,driver):
        content=Utility.get_json('../conf/yang/base.conf')
        # print(content)
        url=f"{content['PROTOCOL']}://{content['HOSTNAME']}:{content['PORT']}/{content['PROGRAM']}/"
        # url='http://47.96.74.65:8080/WoniuBoss4.0/login'
        driver.get(url)

    # 打开首页huang
    @classmethod
    def open_startpage_huang(cls, driver):
        content = Utility.get_json('../conf/huang/base.conf')
        # print(content)
        url = f"{content['PROTOCOL']}://{content['HOSTNAME']}:{content['PORT']}/{content['PROGRAM']}/"
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


    #登录执行,进行解密
    @classmethod
    def ignor_login_decrypt(cls,driver):
        cls.open_startpage(driver)
        contents = Utility.get_json('../conf/yang/base.conf')
        #执行登录

        from lib.login import Login
        Login(driver).do_login(contents['USERNAME'],contents['USERPASS'],contents['CKECKCODE'])
        time.sleep(2)
        #点击解密按钮
        driver.find_element_by_id('btn-decrypt').click()
        # 输入密码
        two_pass = driver.find_element_by_css_selector('div.modal-body:nth-child(2) > input:nth-child(1)')
        cls.send_input(two_pass, contents['TWOPASS'])
        # 点击确定
        driver.find_element_by_css_selector('#secondPass-modal > div:nth-child(1) > \
                div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()


    #下拉框选择通过value
    @classmethod
    def select_value(cls,ele,value):
        from selenium.webdriver.support.select import Select
        Select(ele).select_by_value(value)
    # 下拉框选择通过text
    @classmethod
    def select_text(cls,ele,text):
        from selenium.webdriver.support.select import Select
        Select(ele).select_by_visible_text(text)

    #接受alert弹窗
    @classmethod
    def accept_alert(cls,driver):
        alert = driver.switch_to.alert
        alert.accept()








if __name__ == '__main__':
    pass
    # driver =Service.get_driver('../conf/yang/base.conf')
    # Service.open_startpage(driver)
    # # Service.ignor_login(driver)
