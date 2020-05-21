# -*- coding:utf-8 -*-
#@Time      :2020/5/21
#@Author    :hxy
#@File      :application_for_extra_work.py：加班申请
from tools.service import Service


class ApplicationForExtraWork:

    def __init__(self,driver):
        self.driver = driver
        # 点击教学管理
        self.driver.find_element_by_xpath('//*[@id="nav2"]/div[7]/div[1]/a').click()
        # 点击加班申请
        self.driver.find_element_by_xpath('//*[@id="list-11"]/div/ul/li[4]/a').click()


# 新增排班
# ----------------------------------------------------------------------------------------
    # 点击新增按钮
    def clicl_add_overtime(self):
        self.driver.find_element_by_xpath('//*[@id="queryPara"]/div[1]/button[2]').click()

    #输入开始时间
    def input_start_time(self,start_js,start_time):
        Service.input_time(self.driver,start_js,start_time)

    # 输入结束时间
    def input_end_time(self, end_js, end_time):
        Service.input_time(self.driver, end_js, end_time)

    #选择核算方式
    def select_accounting(self, accounting_value):
        accounting_ele = self.driver.find_element_by_xpath('//*[@id="addApply-form"]/div/div/div[3]/div[1]/select')
        Service.select_text(accounting_ele, accounting_value)

    # 选择加班时长
    def select_hours(self,hours_value):
        hours_ele = self.driver.find_element_by_xpath('//*[@id="addApply-form"]/div/div/div[3]/div[2]/select')
        Service.select_text(hours_ele,hours_value)

    #选择区域
    def select_region(self,region_value):
        region_ele = self.driver.find_element_by_xpath('//*[@id="addApply-form"]/div/div/div[4]/div/select')
        Service.select_text(region_ele,region_value)

    #填写加班事由
    def input_reason(self,reason_value):
        reason_ele = self.driver.find_element_by_xpath('//*[@id="addApply-form"]/div/div/div[5]/div/textarea')
        Service.send_input(reason_ele,reason_value)

    # 点击提交申请
    def click_save(self):
        self.driver.find_element_by_xpath('//*[@id="addApplyBtn"]').click()

    #点击确定
    def click_confirm(self):
        self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[3]/button').click()

    #执行排班
    def do_overtime(self,overtime_info):
        self.clicl_add_overtime()
        self.input_start_time(overtime_info['start_js'],overtime_info['start_time'])
        self.input_end_time(overtime_info['end_js'],overtime_info['end_time'])
        self.select_accounting(overtime_info['accounting'])
        self.select_hours(overtime_info['hours'])
        self.select_region(overtime_info['region'])
        self.input_reason(overtime_info['reason'])
        self.click_save()
        self.click_confirm()


if __name__ == '__main__':
    driver = Service.get_driver('../conf/huang/base.conf')
    driver.implicitly_wait(10)
    # 忽略登录
    Service.ignor_login_decrypt(driver, '../conf/huang/base.conf')
    afew = ApplicationForExtraWork(driver)

    overtime_info = {"start_js":"document.querySelector(\"#addApply-form > div > div > div:nth-child(2) > div:nth-child(1) > input\")",
                     "end_js":"document.querySelector(\"#addApply-form > div > div > div:nth-child(2) > div:nth-child(2) > input\")",
                     "start_time":"2020-05-10 09:30","end_time":"2020-05-10 11:30",
                     "accounting":"结算工资","hours":"2小时","region":"成都",
                     "reason":"没钱要赚更多的钱买买买"
                    }

    afew.do_overtime(overtime_info)
