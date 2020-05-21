# -*- encoding: utf-8 -*-
# File    : week_mark
# Author  : T430s1
# Email   : sc2818@163.com
# Software: PyCharm
# Time    : 2020/5/19 17:40

from tools.service import Service
from tools.utility import Utility
import time

class WeekMark:

    def __init__(self, driver):
        self.driver = driver
        # 绕过登录
        Service.ignor_login_decrypt(self.driver, '../conf/peng/base.conf')

    # 选择区域学员信息
    def select_area(self, value):
        area_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/select[1]')
        Service.select_text(area_ele, value)

    # 选择班级学员信息
    def select_class(self, value):
        class_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/select[2]')
        Service.select_text(class_ele, value)

    # 输入姓名学员信息
    def input_name(self, value):
        name_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/input')
        Service.send_input(name_ele, value)

    #点击学员信息搜索按钮
    def click_query_button(self):
        self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/button').click()

    # 查询组合
    def query_mark(self, query_info):
        Service.open_module(self.driver, "周考成绩")
        self.input_name(query_info["s_name"])
        self.select_area(query_info["s_area"])
        self.select_class(query_info["s_sclass"])
        self.click_query_button()













    # 选择班级学员信息
    def select_class_stu(self, value):
        class_ele = self.driver.find_element_by_xpath('//*[@id="we_cl"]')
        Service.select_text(class_ele, value)


    #选择阶段
    def select_stage(self,value):
        stage_ele = self.driver.find_element_by_xpath('//*[@id="we_phase"]')
        Service.select_text(stage_ele, value)

    def select_week(self, value):
        week_ele = self.driver.find_element_by_xpath('//*[@id="we_week"]')
        Service.select_text(week_ele, value)


    def input_score(self,value):
        score_ele = self.driver.find_element_by_xpath('//*[@id="weekExam-form"]/div[2]/div[4]/input')
        Service.send_input(score_ele, value)

    # 点击学员信息搜索按钮
    def click_keep_button(self):
        self.driver.find_element_by_xpath('//*[@id="weekExam-modal"]/div/div/div[3]/button').click()

    # 获取页面中列表元素的个数
    def get_student_total(self):
        content = self.driver.find_element_by_xpath(
            '//*[@id="stagetest"]/div[2]/div[2]/div[4]/div[1]/span[1]').text
        import re
        p = re.compile("总共(.*)条记录")
        (num) = p.findall(content)[0]

        return int(num)
    #录入组合

    def do_week_mark(self,logging__info):
        Service.open_module(self.driver, "周考成绩")
        self.click_query_button()
        time.sleep(2)
        student_total = self.get_student_total()
        if int(student_total) >= 10:
            student_total = 10
        num = Utility.get_random_num(1, student_total)
        self.driver.find_element_by_xpath(
            f'//*[@id="pe-result"]/tbody/tr[{num}]/td[9]/button').click()

        self.select_class_stu(logging__info["s_sclass"])
        self.select_stage(logging__info["stage"])
        self.select_week(logging__info["week"])
        self.input_score(logging__info["score"])
        self.click_keep_button()







    #周考导入
    def week_week_import(self):
        self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/div/button[2]').click()

    # 选择班级学员信息
    def select_class_stu_week(self, value):
        class_ele = self.driver.find_element_by_xpath('//*[@id="import_cl"]')
        Service.select_text(class_ele, value)

    # 选择阶段
    def select_stage_week(self, value):
        stage_ele = self.driver.find_element_by_xpath('//*[@id="import_ph"]')
        Service.select_text(stage_ele, value)

    def select_week_stu(self, value):
        week_ele = self.driver.find_element_by_xpath('//*[@id="import_we"]')
        Service.select_text(week_ele, value)

    #上传文件
    def upload_fail(self,value):
        self.driver.find_element_by_xpath('//*[@id="files"]').send_keys(value)


    #点击提交按钮
    def click_commit(self):
        self.driver.find_element_by_xpath('//*[@id="upRes-modal"]/div/div/div[3]/button').click()


    # #点击确定按钮
    # def click_ok(self):
    #     self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button')

    #导入组合
    def do_import(self,logging__week_info):
        Service.open_module(self.driver, "周考成绩")
        self.week_week_import()
        self.select_class_stu_week(logging__week_info["s_sclass"])
        self.select_stage_week(logging__week_info["stage"])
        self.select_week_stu(logging__week_info["week"])
        self.upload_fail(logging__week_info["file"])


        self.click_commit()
        # self.click_ok()


if __name__ == '__main__':
    driver = Service.get_driver('../conf/peng/base.conf')
    driver.implicitly_wait(10)

    logging__week_info = {"s_sclass": "WNCDC002", "stage": "第一阶段", "week": "第一阶段-第一周 JavaSE编程基础","file":"C:\\lipeng\\test\\testing\\data\\周考成绩.xls"}
    student_total = {"edit_name": "晒着", "edit_state": "在校学习", "edit_tel": "13111111111", "edit_source": "专属简历"}
    a = WeekMark(driver)
    a.do_import(logging__week_info)