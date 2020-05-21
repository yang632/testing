# -*- encoding: utf-8 -*-
# File    : public_rescources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 11:43
from selenium.webdriver.common.by import By

from tools.service import Service


class PublicRescources:

    def __init__(self,driver):

        self.driver=driver
        self.driver.find_element_by_partial_link_text('资源管理').click()
        self.driver.find_element_by_partial_link_text('公共资源').click()

    #选择下拉框,需传入xpath与值
    def select_ele(self,xpath,select_ele_value):

        ele_select=self.driver.find_element(By.xpath,xpath)
        Service.select_text(ele_select,select_ele_value)

    #输入姓名电话或者qq
    def input_public_name(self,public_name_value):
        public_name_ele= self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/input')
        Service.send_input(public_name_ele,public_name_value)

    #点击查询
    def click_public_query(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/button').click()
    #执行查询
    def do_query_public_resource(self):
        #选择区域
        self.select_ele(area_xpath,area_value)
        #选择部门
        #选择最后废弃人
        #选择状态
        #选择来源
        #选择学历
        #