# -*- coding:utf-8 -*-
#@Time      :2020/5/18
#@Author    :hxy
#@File      :course_arrangement.py
from tools.service import Service


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

    # 点击排课
    def click_new_course(self):
        # 点击排课按钮
        self.driver.find_element_by_css_selector("button.btn:nth-child(11)").click()

    #开始时间
    def start_time(self,start_time_value):
        start_time_ele=self.driver.find_element_by_partial_link_text('cur.start_time')
        Service.send_input(start_time_ele,start_time_value)

    #结束时间
    def end_time(self,end_time_value):
        end_time_ele = self.driver.find_element_by_partial_link_text('cur.end_time')
        Service.send_input(end_time_ele,end_time_value)

    # 选择讲师
    def select_teacher(self, teacher_value):
        teacher_ele = self.driver.find_element_by_xpath('//*[@id="addCourse-table"]/tr/td[1]/select')
        Service.select_text(teacher_ele, teacher_value)

    # 选择教室
    def select_classroom(self, classroom_value):
        classroom_ele = self.driver.find_element_by_xpath('//*[@id="addCourse-table"]/tr/td[2]/select')
        Service.select_text(classroom_ele, classroom_value)

    # 选择班号
    def select_classcode(self, classcode_value):
        classcode_ele = self.driver.find_element_by_xpath('//*[@id="addCourse-table"]/tr/td[3]/select')
        Service.select_text(classcode_ele, classcode_value)

    # 选择课程
    def select_course(self, course_value):
        course_ele = self.driver.find_element_by_xpath('//*[@id="addCourse-table"]/tr/td[4]/select')
        Service.select_text(course_ele, course_value)

    #点击保存
    def click_save(self):
        self.driver.find_element_by_xpath('//*[@id="course-add"]/div/div/div[3]/button').click()



    #新增排课组合操作
    def add_course(self,add_course_info):
        self.click_query()
        self.click_new_course()
        self.start_time()
        self.end_time()
        self.select_teacher()
        self.select_classroom()
        self.select_classcode()
        self.select_course()
        self.click_save()



if __name__ == '__main__':
    driver = Service.get_driver('../conf/huang/base.conf')
    driver.implicitly_wait(10)
    Service.ignor_login_decrypt(driver, '../conf/huang/base.conf')
    ca = CourseArrangement(driver)

    # add_resources_info={"cus.tel":"19877101296","cus.name":"三生三世",
    # "cus.sex":"女","cus.last_status":"新入库","cus.wechat":"啊啊撒啥啥所",
    # "cus.qq":"阿萨斯搜索","cus.school":"啊啊啊啊","cus.education":"本科",
    # "cus.major":"啊啊啊啊","cus.intent":"啊啊啊啊","cus.workage":"2年","cus.salary":"啊啊啊啊啊","cus.source":"今日头条","cus.email":"啊啊啊啊啊","cus.age":"2年",
    # "cus.eduexp":"啊啊啊","cus.experience":"三生三世",
    # "cus.last_tracking_remark":"少时诵诗书所"}
    #
    # ts.do_add_resources(add_resources_info)

