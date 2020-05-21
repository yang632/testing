# -*- coding:utf-8 -*-
#@Time      :2020/5/20
#@Author    :hxy
# @File      :teacher_on_duty.py：教师值班
import random

from tools.service import Service


class TeacherOnDuty:

    def __init__(self,driver):
        self.driver = driver
        # 点击教学管理
        self.driver.find_element_by_xpath('//*[@id="nav2"]/div[7]/div[1]/a').click()
        # 点击教师值班
        self.driver.find_element_by_xpath('//*[@id="list-11"]/div/ul/li[3]/a').click()

# 新增值班
# -------------------------------------------------------------------------------------------------
    # 点击指定值班
    def click_duty(self):
        self.driver.find_element_by_xpath('//*[@id="queryAera"]/div/button[2]').click()

    # 选择值班人
    def select_teacher(self,teacher_value):
        teacher_ele = self.driver.find_element_by_xpath('//*[@id="addDuty-table"]/tr/td[1]/select')
        Service.select_text(teacher_ele,teacher_value)

    # 选择值班日期
    def select_duty_time(self,time_js,duty_time):
        Service.input_time(self.driver,time_js,duty_time)

    # 点击保存
    def click_seve(self):
        self.driver.find_element_by_xpath('//*[@id="addDuty-modal"]/div/div/div[3]/button').click()

    # 点击确定
    def click_confirm(self):
        self.driver.find_element_by_xpath('/html/body/div[16]/div/div/div[3]/button').click()

    # 执行
    def do_add_duty(self,duty_info):
        self.click_duty()
        self.select_teacher(duty_info['teacher'])
        self.select_duty_time(duty_info['time_js'],duty_info['duty_time'])
        self.click_seve()
        self.click_confirm()

# 修改值班
# ------------------------------------------------------------------------------------------------

#     点击修改
    def click_alter(self):
        # 随机修改
        # 获取纪录总数
        num = Service.get_num(driver, '//*[@id="content"]/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]')
        # 随机选择值班
        dutynum = random.randint(1, int(num))
        print("num",num,"\tdutynum",dutynum)
        self.driver.find_element_by_xpath(f'//*[@id="duty_table"]/tbody/tr[{dutynum}]/td[10]/button[2]').click()
        return dutynum

    # 选择值班人
    def alter_teacher(self,teacher_value):
        teacher_ele = self.driver.find_element_by_xpath('//*[@id="editDuty-form"]/div/div[1]/select')
        Service.select_text(teacher_ele,teacher_value)

    # 选择值班日期
    def alter_duty_time(self,time_js,duty_time):
        Service.input_time(self.driver,time_js,duty_time)
    #     document.querySelector("#editDuty-form > div > div:nth-child(3) > input")

    # 点击保存
    def click_alter_seve(self):
        self.driver.find_element_by_xpath('//*[@id="editDuty-modal"]/div/div/div[3]/button').click()

    # 点击确定
    def click_alter_confirm(self):
        self.driver.find_element_by_xpath('/html/body/div[15]/div/div/div[3]/button').click()

    # 执行
    def do_alter_duty(self,alter_duty_info):
        self.click_alter()
        self.alter_teacher(alter_duty_info['teacher'])
        self.alter_duty_time()
        self.click_alter_seve()
        self.click_alter_confirm()


if __name__ == '__main__':
    driver = Service.get_driver('../conf/huang/base.conf')
    driver.implicitly_wait(10)
    # 忽略登录
    Service.ignor_login_decrypt(driver, '../conf/huang/base.conf')
    tod = TeacherOnDuty(driver)

    duty_info = {"teacher":"我是谁",
                 "time_js":"document.querySelector(\"#addDuty-table > tr > td:nth-child(2) > input\")",
                 "duty_time":"2020-05-20"
                 }

    tod.do_add_duty(duty_info)

    alter_duty_info = {"teacher": "吴用",
                       "time_js": "document.querySelector(\"#editDuty-form > div > div:nth-child(3) > input\")",
                       "duty_time": "2020-05-19"
                      }

    # tod.do_alter_duty(alter_duty_info)