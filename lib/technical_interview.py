# -*- coding:utf-8 -*-
#@Time      :2020/5/19
#@Author    :hxy
#@File      :technical_interview.py：技术面试
import random

from tools.service import Service


class TechnicalInterview:

    def __init__(self,driver):
        self.driver = driver
        # 点击教学管理
        self.driver.find_element_by_xpath('//*[@id="nav2"]/div[7]/div[1]/a').click()
        # 点击技术面试
        self.driver.find_element_by_xpath('//*[@id="list-11"]/div/ul/li[2]/a').click()

    # 点击面试按钮
    def click_interview(self):
        # 获取学生总数
        num = Service.get_num(self.driver, '//*[@id="skills"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        print(num)
        # 随机选择学生
        studentnum = random.randint(1, 6)
        print(studentnum)
        self.driver.find_element_by_xpath(f'//*[@id="stuInfo_table"]/tbody/tr[{studentnum}]/td[9]/button').click()
        return studentnum

    # 选择面试结果
    def select_result(self,result_value):
        result_ele = self.driver.find_element_by_id('isPassSkill')
        Service.select_text(result_ele, result_value)

    # 输入评价
    def input_evaluate(self,evaluate_value):
        evaluate_ele = self.driver.find_element_by_id('sval')
        Service.send_input(evaluate_ele,evaluate_value)

    # 点击保存
    def click_save(self):
        self.driver.find_element_by_id('saveSkillbtn').click()

    # 点击确定
    def click_confirm(self):
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button').click()

    # 执行面试
    def do_interview(self,add_interview_info):
        self.click_interview()
        self.select_result(add_interview_info["outcome"])
        self.input_evaluate(add_interview_info["evaluate"])
        self.click_save()
        self.click_confirm()



if __name__ == '__main__':
    driver = Service.get_driver('../conf/huang/base.conf')
    driver.implicitly_wait(10)
    # 忽略登录
    Service.ignor_login_decrypt(driver, '../conf/huang/base.conf')
    ti = TechnicalInterview(driver)

    add_interview_info = {"outcome":"优","evaluate":"基础知识掌握牢固"}
    ti.do_interview(add_interview_info)