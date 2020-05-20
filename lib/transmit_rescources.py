# -*- encoding: utf-8 -*-
# File    : transmit_rescources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 20:22

#转交资源
import time

from selenium.webdriver.common.by import By
from tools.service import Service
class TransmitRescources:

    def __init__(self,driver):
        self.driver=driver
        self.driver.find_element_by_partial_link_text('培训资源').click()
        self.driver.find_element_by_partial_link_text('转交资源').click()

    # 选择区域
    def select_area(self,area_value):
        area_ele=self.driver.find_element_by_xpath('//*[@id="regionSelect1"]')
        Service.select_text(area_ele,area_value)
    # 选择部门
    def select_dpt(self, dpt_value):
        dpt_ele = self.driver.find_element_by_css_selector('#content > div:nth-child(2) > div:nth-child(1) > select:nth-child(3)')
        Service.select_text(dpt_ele,dpt_value)
    # 选择咨询师
    def select_empname(self, empname_value):
        empname_ele = self.driver.find_element_by_id('empNameSelect1')
        Service.select_text(empname_ele, empname_value)
    # 选择在状态
    def select_transmit_status(self, transmit_status_value):
        transmit_status_ele = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/select[4]')
        Service.select_text(transmit_status_ele, transmit_status_value)
    # 选择来源
    def select_transmit_source(self, transmit_source_value):
        transmit_source_ele = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/select[5]')
        Service.select_text(transmit_source_ele, transmit_source_value)
    # 输入姓名或者电话
    def input_transmit_name(self, transmit_name_value):
        transmit_name_ele = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/input')
        Service.send_input(transmit_name_ele,transmit_name_value)
    # 点击搜索
    def click_transmit_query(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/button').click()


    # 随机选择资源
    def get_random_rescources(self,old_num):
        if old_num > 10:
            old_num = 10
        self.driver.find_element_by_xpath(f'//*[@id="transmit-table"]/tbody/tr[{old_num}]/td[1]/input').click()
    # 选择转交区域
    def select_transmit_area(self, transmit_area_value):
        transmit_area_ele = self.driver.find_element_by_xpath('//*[@id="regionSelect2"]')
        Service.select_text(transmit_area_ele, transmit_area_value)
    # 选择转交部门
    def select_transmit_dpt(self, transmit_dpt_value):
        transmit_dpt_ele = self.driver.find_element_by_xpath('//*[@id="deptSelect2"]')
        Service.select_text(transmit_dpt_ele, transmit_dpt_value)
     
    # 选择转交咨询师
    def select_transmit_empname(self, transmit_empname_value):
        transmit_empname_ele = self.driver.find_element_by_xpath('//*[@id="empNameSelect2"]')
        Service.select_text(transmit_empname_ele, transmit_empname_value)

    #点击提交
    def click_transmit_commit(self):
        self.driver.find_element_by_xpath('//*[@id="Submit"]').click()

    #点击提交
    def click_submit(self):
        self.driver.find_element_by_xpath('//*[@id="Submit"]').click()

    #执行资源搜索
    def do_query_rescources(self,transmit_rescources_info):
        self.select_area(transmit_rescources_info['area_text_value'])
        # time.sleep(2)
        self.select_dpt(transmit_rescources_info['dpt_text_value'])
        self.select_empname(transmit_rescources_info['empname_text_value'])
        self.select_transmit_status(transmit_rescources_info['status_text_value'])
        self.select_transmit_source(transmit_rescources_info['source_text_value'])
        self.input_transmit_name(transmit_rescources_info['name_text_value'])
        self.click_transmit_query()
        time.sleep(3)
        #获取此时数量
        return Service.get_num(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')


    #执行分配
    def do_transmit_rescources(self,old_num,transmit_rescources_info):
        #随机勾选
        self.get_random_rescources(old_num)
        self.select_transmit_area(transmit_rescources_info['transmit_area_value'])
        self.select_transmit_dpt(transmit_rescources_info['transmit_dpt_value'])
        self.select_transmit_empname(transmit_rescources_info['transmit_empname_value'])
        self.click_submit()


