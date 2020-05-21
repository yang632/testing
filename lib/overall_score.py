# -*- encoding: utf-8 -*-
# File    : overall_score
# Author  : T430s1
# Email   : sc2818@163.com
# Software: PyCharm
# Time    : 2020/5/20 16:19

from tools.service import Service
from tools.utility import Utility
import time


class OverallScore:
    def __init__(self, driver):
        self.driver = driver
        # 绕过登录
        Service.ignor_login_decrypt(self.driver, '../conf/peng/base.conf')

    #选择区域学员信息
    def select_area(self,value):
        area_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/select[1]')
        Service.select_text(area_ele, value)

    # 选择方向学员信息
    def select_direction(self, value):
        direction_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/select[2]')
        Service.select_text(direction_ele, value)

    # 选择班级学员信息
    def select_class(self, value):
        class_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/select[3]')
        Service.select_text(class_ele, value)


    #选择阶段
    def select_stage(self,value):
        stage_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/select[4]')
        Service.select_text(stage_ele, value)


    #输入姓名学员信息
    def input_name(self,value):
        name_ele = self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/input')

        Service.send_input(name_ele,value)


    #点击学员信息搜索按钮
    def click_query_button(self):
        self.driver.find_element_by_xpath('//*[@id="stagetest"]/div[1]/button').click()

    # 获取页面中列表元素的个数
    def get_student_total(self):
        content = self.driver.find_element_by_xpath(
            '//*[@id="stagetest"]/div[2]/div[2]/div[4]/div[1]/span[1]').text
        import re
        p = re.compile("总共(.*)条记录")
        (num) = p.findall(content)[0]

        return int(num)

    # 查询组合
    def query_score(self, query_info):
        Service.open_module(self.driver, "综合成绩")
        self.input_name(query_info["s_name"])
        self.select_area(query_info["s_area"])
        self.select_direction(query_info["s_direction"])
        self.select_class(query_info["s_sclass"])
        self.select_stage(query_info["s_stage"])
        self.click_query_button()


