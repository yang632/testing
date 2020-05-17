# -*- encoding: utf-8 -*-
# File    : training_resources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/17 10:18   培训资源操作

from tools.service import Service


class TrainingResources:
    def __init__(self,driver):
        self.driver=driver
        #点击资源管理,点击培训资源
        self.driver.find_element_by_partial_link_text("资源管理").click()
        self.driver.find_element_by_partial_link_text("培训资源").click()
    #点击资源新增按钮
    def click_add_button(self):
        self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()
    #输入电话号码
    def input_tel(self,tel_value):
        tel=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[1]/div[1]/input')
        Service.send_input(tel,tel_value)
    #输入姓名
    def input_name(self,name_value):
        name=self.driver.find_element_by_css_selector('div.has-feedback:nth-child(2) > input:nth-child(2)')
        Service.send_input(name,name_value)
    #选择性别
    def select_sex(self,sex_value):
        sex_ele=self.driver.find_element_by_xpath('//*[ @ id = "addCus"]/div[1]/div[1]/div[3]/select')
        Service.select_value(sex_ele,sex_value)

    #选择状态
    def select_status(self,status_text_value):
        status_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[2]/div[1]/select')
        Service.select_text(status_ele,status_text_value)
    #输入微信
    def input_wechat(self,wechat_value):
        wechat_ele=self.driver.find_element_by_css_selector('//*[@id="addCus"]/div[1]/div[2]/div[2]/input')
        Service.send_input(wechat_ele,wechat_value)
    #





    # #新增资源
    # def add_resources(self):










if __name__ == '__main__':
    driver=Service.get_driver()
    Service.ignor_login_decrypt(driver)
    ts=TrainingResources(driver)