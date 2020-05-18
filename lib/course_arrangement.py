# -*- coding:utf-8 -*-
#@Time      :2020/5/18
#@Author    :hxy
#@File      :course_arrangement.py

class CourseArrangement:

    def __init__(self,driver):
            self.driver = driver
            # 点击教学管理
            self.driver.find_element_by_partial_link_text("教学管理").click()
            # 点击课程安排
            self.driver.find_element_by_partial_link_text("课程安排").click()

    # 点击查询
    def click_query(self):
        self.driver.find_element_by_css_selector("button.btn:nth-child(10)").click()

    # 排课
    def new_course(self):
        # 点击排课按钮
        self.driver.find_element_by_css_selector("button.btn:nth-child(11)").click()