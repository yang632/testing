# -*- encoding: utf-8 -*-
# File    : student
# Author  : T430s1
# Email   : sc2818@163.com
# Software: PyCharm
# Time    : 2020/5/19 9:27
from tools.service import Service
from tools.utility import Utility


class Student:

    def __init__(self, driver):
        self.driver = driver
        # 绕过登录
        Service.ignor_login_decrypt(self.driver, '../conf/peng/base.conf')

    #选择区域学员信息
    def select_area(self,value):
        area_ele = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/select[1]')
        Service.select_text(area_ele, value)

    #选择方向学员信息
    def select_direction(self,value):
        direction_ele = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/select[2]')
        Service.select_text(direction_ele, value)

    #选择班级学员信息
    def select_class(self,value):
        class_ele = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/select[3]')
        Service.select_text(class_ele, value)


    #选择状态学员信息
    def select_state(self,value):
        state_ele = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/select[4]')
        Service.select_text(state_ele, value)

    #输入姓名学员信息
    def input_name(self,value):
        name_ele = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/input')

        Service.send_input(name_ele,value)
    #点击学员信息搜索按钮
    def click_query_button(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/button').click()



    #查询组合
    def query_student(self,query_info):
        Service.open_module(self.driver,"学员信息")
        self.input_name(query_info["name"])
        self.select_area(query_info["area"])
        self.select_direction(query_info["direction"])
        self.select_class(query_info["class"])
        self.select_state(query_info["state"])










    #修改最新状态
    def edit_state(self,value):
        state_ele = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div/div[1]/div[1]/div[6]/select')
        Service.select_text(state_ele, value)


    #修改姓名
    def edit_name(self,edit_name_value):
        edit_name_ele=self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div/div[1]/div[1]/div[1]/input')
        Service.send_input(edit_name_ele,edit_name_value)

    # 修改电话号码
    def edit_tel(self, edit_tel_value):
        edit_tel_ele = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div/div[1]/div[1]/div[4]/input')
        Service.send_input(edit_tel_ele, edit_tel_value)

    # 修改渠道来源
    def edit_source(self, edit_source_value):
        edit_source_ele = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div/div[2]/div[1]/select')
        Service.select_text(edit_source_ele, edit_source_value)
    #点击保存
    def click_edit_button(self):
        self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div[2]/button').click()

    # 获取页面中列表元素的个数
    def get_student_total(self):
        content=self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text
        import re
        p = re.compile("总共(.*)条记录")
        num=p.findall(content)[0]


        return num
        # 执行修改组合操作


    def do_edit_recource(self, edit_student_info):
        student_total = self.get_student_total()
        if int(student_total) >=10:

            student_total= 10
        num = Utility.get_random_num(1, student_total)
        self.driver.find_element_by_xpath(f'/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{num}]/td[12]/button[2]').click()
        self.edit_name(edit_student_info['edit_name'])
        self.edit_state(edit_student_info['edit_state'])
        self.edit_tel(edit_student_info['edit_tel'])
        self.edit_source(edit_student_info['edit_source'])
        self.click_edit_button()


if __name__ == '__main__':
    driver = Service.get_driver('../conf/peng/base.conf')
    driver.implicitly_wait(10)
    # # 绕过登录
    # Service.ignor_login_decrypt(driver, '../conf/peng/base.conf')
    query_info={"area":"全部","name":"晒着","direction":"全部","class":"全部","state":"全部"}
    student_total={"edit_name":"晒着","edit_state":"在校学习"}
    a=Student(driver)
    a.query_student(query_info)