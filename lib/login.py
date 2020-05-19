# -*- encoding: utf-8 -*-
# File    : login
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 17:21
from tools.service import Service


class Login:
    def __init__(self,driver):
        self.driver=driver
    #输入用户名
    def input_uasername(self,uname):
        username=self.driver.find_element_by_css_selector('div.row:nth-child(1) > input:nth-child(1)')
        Service.send_input(username,uname)

    #输入密码
    def input_password(self,psword):
        password=self.driver.find_element_by_css_selector('div.row:nth-child(2) > input:nth-child(1)')
        Service.send_input(password,psword)

    #输入验证码
    def input_vcode(self,code):
        vcode=self.driver.find_element_by_css_selector('input.col-md-6')
        Service.send_input(vcode,code)
    #取消勾选记住密码
    def click_remember(self):
        self.driver.find_element_by_css_selector('div.row:nth-child(4) > input:nth-child(1)').click()
    #点击登录
    def click_login(self):
        self.driver.find_element_by_css_selector('.btn').click()


    #登录成功点击注销
    def click_logout(self):
        self.driver.find_element_by_partial_link_text('注销').click()
    #执行登录动作
    def do_login(self,uname,psword,code):
        Service.open_startpage(self.driver,'../conf/yun/base.conf')
        self.input_uasername(uname)
        self.input_password(psword)
        self.input_vcode(code)
        self.click_remember()
        self.click_login()


if __name__ == '__main__':
    pass
    # from selenium import webdriver
    # driver=webdriver.Edge()
    # driver.implicitly_wait(10)
    # lo=Login(driver)
    # lo.do_login("WNCD000","woniu123","0000")