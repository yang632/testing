# -*- encoding: utf-8 -*-
# File    : public_rescources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 11:43
import time

from selenium.webdriver.common.by import By

from tools.service import Service


class PublicRescources:

    def __init__(self,driver):
        self.driver=driver
        self.driver.find_element_by_partial_link_text('资源管理').click()
        self.driver.find_element_by_partial_link_text('公共资源').click()

    #选择区域
    def select_public_area(self,area_value):
        area_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[1]')
        Service.select_text(area_ele,area_value)

    #选择部门
    def select_public_dpt(self,dpt_value):
        dpt_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[2]')
        Service.select_text(dpt_ele,dpt_value)

    #选择最后废弃人
    def select_public_last_abandoned(self,last_abandoned_value):
        last_abandoned_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[3]')
        Service.select_text(last_abandoned_ele,last_abandoned_value)
    #选择状态
    def select_public_last_status(self,last_status_value):
        last_status_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[4]')
        Service.select_text(last_status_ele,last_status_value)
    #选择来源
    def select_public_source(self,public_source_value):
        public_source_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[5]')
        Service.select_text(public_source_ele,public_source_value)
    #选择学历
    def select_public_education(self,public_education_value):
        public_education_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[6]')
        Service.select_text(public_education_ele,public_education_value)

    #输入姓名电话或者qq
    def input_public_name(self,public_name_value):
        public_name_ele= self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/input')
        Service.send_input(public_name_ele,public_name_value)

    #点击查询
    def click_public_query(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/button').click()

    #点击认领
    def select_public_claim(self):
        self.driver.find_element_by_xpath('//*[@id="ownCusBtn"]').click()

    #确认认领
    def claim_enter(self):
        self.driver.find_element_by_css_selector('body > div.bootbox.modal.fade.mydialog.in > \
        div > div > div.modal-footer > button.btn.btn-primary').click()
    #执行废弃资源全条件搜索
    def do_query_public(self,query_public_info):
        self.select_public_area(query_public_info['area_value'])
        time.sleep(1)
        self.select_public_dpt(query_public_info['dpt_value'])
        self.select_public_last_abandoned(query_public_info['abandoned_value'])
        self.select_public_last_status(query_public_info['status_value'])
        self.select_public_source(query_public_info['source_value'])
        self.select_public_education(query_public_info['education_value'])
        self.input_public_name(query_public_info['name_value'])
        self.click_public_query()

    #随机认领资源
    def do_claim_rescources(self,old_num):
        if old_num > 10:
            old_num=10
        self.driver.find_element_by_xpath(f'//*[@id="public-pool-table"]/tbody/tr[{old_num}]/td[1]/input').click()
        self.select_public_claim()
        import time
        time.sleep(2)
        self.claim_enter()



