# -*- encoding: utf-8 -*-
# File    : transmit_rescources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
<<<<<<< HEAD
<<<<<<< HEAD
# Time    : 2020/5/19 20:22

#转交资源
from selenium.webdriver.common.by import By

from tools.service import Service


class TransmitRescources:

    def __init__(self,driver):
        self.driver=driver
        self.driver.find_element_by_partial_link_text('培训资源').click()
        self.driver.find_element_by_partial_link_text('转交资源').click()


    #选择options
    def select_option(self,xpath_value,select_value):
        select_ele=self.driver.find_element(By.XPATH,xpath_value)
        Service.select_text(select_ele,select_value)


    #输入文本内容
    def input_text(self,xpath_value,text_value):
        text_ele=self.driver.find_element(By.XPATH,xpath_value)
        Service.send_input(text_ele,text_value)

    #点击搜索
    def click_transmit_query(self,xpath_value):
        self.driver.find_element_by_xpath(xpath_value).click()

    #点击提交
    def click_submit(self):
        self.driver.find_element_by__xpath('//*[@id="Submit"]').click()

    def do_transmit_rescources(self,old_num,transmit_rescources_info):
        transmit_rescources_info={
            "area_xpath_value":xpath,"area_text_value":value,
            "dpt_xpath_value": xpath, "dpt_text_value": value,
            "empname_xpath_value": xpath, "empname_text_value": value,
            "status_xpath_value": xpath, "status_text_value": value,
            "source_xpath_value": xpath, "source_text_value": value,
            "name_xpath_value": xpath, "name_text_value": value,"query_xpath_value":vaklue,
            "transmit_area_xpath_value": xpath, "transmit_area_value": value,
            "transmit_dpt_xpath_value": xpath, "transmit_dpt_value": value,
            "transmit_empname_xpath_value": xpath, "transmit_empname_value": value
        }
        #选择区域
        self.select_option(transmit_rescources_info['area_xpath_value'],transmit_rescources_info['area_text_value'])
        #选择部门
        self.select_option(transmit_rescources_info['dpt_xpath_value'],transmit_rescources_info['dpt_text_value'])
        #选择咨询师
        self.select_option(transmit_rescources_info['empname_xpath_value'], transmit_rescources_info['empname_text_value'])
        #选择在状态
        self.select_option(transmit_rescources_info['status_xpath_value'],transmit_rescources_info['status_text_value'])
        #选择来源
        self.select_option(transmit_rescources_info['source_xpath_value'], transmit_rescources_info['source_text_value'])
        #输入姓名或者电话
        self.input_text(transmit_rescources_info['name_xpath_value'],transmit_rescources_info['name_text_value'])
        #点击搜索
        self.click_transmit_query(transmit_rescources_info['query_xpath_value'])

        #随机选择资源
        if old_num >10:
            old_num=10
        self.driver.find_element_by__xpath(f'//*[@id="transmit-table"]/tbody/tr[{old_num}]/td[1]/input').click()


        #选择转交区域
        self.select_option(transmit_rescources_info['transmit_area_xpath_value'],\
                           transmit_rescources_info['transmit_area_value'])
        #选择转交部门
        self.select_option(transmit_rescources_info['transmit_dpt_xpath_value'],\
                           transmit_rescources_info['transmit_dpt_value'])
        #选择转交咨询师
        self.select_option(transmit_rescources_info['transmit_empname_xpath_value'],\
                           transmit_rescources_info['transmit_empname_value'])


        #点击提交
        self.click_submit()
=======
# Time    : 2020/5/19 20:22
>>>>>>> eb6c6fe576a75db31ffad982cc353d6f1b9efb50
=======
# Time    : 2020/5/19 20:22
>>>>>>> eb6c6fe576a75db31ffad982cc353d6f1b9efb50
