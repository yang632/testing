# -*- coding:utf-8 -*-
#@Time      :2020/5/18
#@Author    :hxy
#@File      :course_arrangement.py
import random

from tools.service import Service


class CourseArrangement:

    query_all_course_info = {'campus': '全部', 'teacher': '全部', 'specialty': '全部',
                             'start_time': '', 'end_time': ''
                             }

    def __init__(self,driver):
            self.driver = driver
            # 点击教学管理
            self.driver.find_element_by_xpath('//*[@id="nav2"]/div[7]/div[1]/a').click()
            # 点击课程安排
            self.driver.find_element_by_xpath('//*[@id="list-11"]/div/ul/li[1]/a').click()

# 查询
# -------------------------------------------------------------------------------------------

    # 点击查询
    def click_query(self):
        self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/button[1]').click()

    # 选择校区
    def select_campus(self, campus_value):
        campus_ele = self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/select[1]')
        Service.select_text(campus_ele, campus_value)

    # 选择讲师
    def query_teacher(self, teacher_value):
        teacher_ele = self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/select[2]')
        Service.select_text(teacher_ele, teacher_value)

    #选择方向
    def select_specialty(self, specialty_value):
        specialty_ele = self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/select[3]')
        Service.select_text(specialty_ele, specialty_value)

    # 开始时间
    def query_start_time(self, start_time_value):
        start_time_ele = self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/input[1]')
        Service.send_input(start_time_ele, start_time_value)

    # 结束时间
    def query_end_time(self, end_time_value):
        end_time_ele = self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/input[2]')
        Service.send_input(end_time_ele, end_time_value)

    # 执行搜索
    def do_query(self, query_course_info):
        self.select_campus(query_course_info['campus'])
        self.query_teacher(query_course_info['teacher'])
        self.select_specialty(query_course_info['specialty'])
        self.query_start_time(query_course_info['start_time'])
        self.query_end_time(query_course_info['end_time'])
        self.click_query()

# 排课
# --------------------------------------------------------------------------------------------

    # 点击排课
    def click_new_course(self):
        # 点击排课按钮
        self.driver.find_element_by_css_selector("button.btn:nth-child(11)").click()

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

    # 点击确定
    def click_confirm(self):
        self.driver.find_element_by_xpath('/html/body/div[16]/div/div/div[3]/button').click()

    #新增排课组合操作
    def do_add_course(self,add_course_info):
        self.click_query()
        self.click_new_course()
        # 输入开始时间
        Service.input_time(self.driver,add_course_info['start_js'],add_course_info['start_time'])
        Service.input_time(self.driver,add_course_info['end_js'],add_course_info['end_time'])
        self.select_teacher(add_course_info['teacher'])
        self.select_classroom(add_course_info['classroom'])
        self.select_classcode(add_course_info['classcode'])
        self.select_course(add_course_info['course'])
        self.click_save()
        self.click_confirm()

# 修改排课
# ---------------------------------------------------------------------------------------------

    # 点击修改按钮
    def click_alter(self):
        # 随机修改
        # 获取班级总数
        num = Service.get_num(driver, '//*[@id="course"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        # 随机选择课程
        classnum = random.randint(1, int(num))
        self.driver.find_element_by_xpath(f'//*[@id="course_table"]/tbody/tr[{classnum}]/td[9]/button').click()

    # 输入开始时间
    def alter_start_time(self):
        Service.input_time(self.driver,alter_course_info['satrt_js'],alter_course_info['start_time'])

    #输入结束时间
    def alter_end_time(self):
        Service.input_time(self.driver,alter_course_info['end_js'],alter_course_info['end_time'])

    # 修改讲师
    def alter_teacher(self,teacher_value):
        teacher_ele = self.driver.find_element_by_xpath('//*[@id="modifyCourseForm"]/div/div/div[3]/select')
        Service.select_text(teacher_ele,teacher_value)

    # 修改教室
    def alter_classroom(self,classroom_value):
        classroom_ele = self.driver.find_element_by_xpath('//*[@id="modifyCourseForm"]/div/div/div[4]/select')
        Service.select_text(classroom_ele,classroom_value)

    # 修改班号
    def alter_classcode(self,classcode_value):
        classcode_ele = self.driver.find_element_by_xpath('//*[@id="modifyCourseForm"]/div/div/div[5]/select')
        Service.select_text(classcode_ele,classcode_value)

    # 修改课程
    def alter_course(self,course_value):
        course_ele = self.driver.find_element_by_xpath('//*[@id="modifyCourseForm"]/div/div/div[6]/select')
        Service.select_text(course_ele,course_value)

    # 点击保存
    def click_alter_save(self):
        self.driver.find_element_by_xpath('//*[@id="modifyCourse"]/div/div/div[2]/button').click()

    def do_alter_course(self,alter_course_info):
        self.alter_start_time()
        self.alter_end_time()
        self.alter_teacher(alter_course_info['teacher'])
        self.alter_classroom(alter_course_info['classroom'])
        self.alter_classcode(alter_course_info['calsscode'])
        self.alter_course(alter_course_info['course'])
        self.click_alter_save()



# -------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    driver = Service.get_driver('../conf/huang/base.conf')
    driver.implicitly_wait(10)
    # 忽略登录
    Service.ignor_login_decrypt(driver, '../conf/huang/base.conf')
    ca = CourseArrangement(driver)

    query_course_info = {'campus': '成都', 'teacher': '我是谁', 'specialty': '全部',
                           'start_time': '', 'end_time': ''
                           }

    # ca.do_query(query_course_info)

    add_course_info={"start_js":"document.querySelector(\"#addcourse > div.row > div:nth-child(1) > input\")",
                     "end_js":"document.querySelector(\"#modifyCourseForm > div > div > div:nth-child(2) > input\")",
                     "start_time":"2020-05-10","end_time":"2020-06-01",
                     "teacher":"我是谁","classroom":"教室一","classcode":"WNCDC002",
                     "course":"第一阶段-第二周-MySQL数据库"
                     }

    # ca.do_add_course(add_course_info)

    alter_course_info = {"start_js":"document.querySelector(\"#modifyCourseForm > div > div > div:nth-child(1) > input\")",
                        "end_js":"document.querySelector(\"#modifyCourseForm > div > div > div:nth-child(2) > input\")",
                        "teacher":"阿大"
                        }

    ca.do_alter_course(alter_course_info)