# -*- coding:utf-8 -*-
#@Time      :2020/5/19
#@Author    :hxy
#@File      :course_arrangement_test.py

import unittest
import warnings
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized
from lib.course_arrangement import CourseArrangement

class CouresArrangementTest(unittest.TestCase):

    #获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    # 获取添加的测试数据
    add_course_info = Utility.tran_tuple(contents[1])
    #获取查询的测试数据
    query_course_info = Utility.tran_tuple(contents[2])
    #获取修改的测试数据
    alter_course_info = Utility.tran_tuple(contents[3])

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore',ResourceWarning)

    def setUp(self):
        self.driver = Service.get_driver('../conf/huang/base.conf')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        Service.ignor_login_decrypt(self.driver,'../conf/huang/base.conf')
        self.ca = CourseArrangement(self.driver)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass

    #测试增加
    @parameterized.expand(add_course_info)
    @unittest.skip('fa')
    def test_add_course(self,start_time,end_time,teacher,classroom,classcode,course,expect):
        add_course_info = {"start_time":start_time,"end_time":end_time,"teacher":teacher,
                           "classroom":classroom,"classcode":classcode,"course":course}

        self.ca.do_add_course(add_course_info)

#       执行测试后搜索
        self.ca.do_query(self.ca.query_all_course_info)
        teacher_list=Service.get_page_ele(self.driver,'//*[@id="course_table"]/tbody/tr[1]/td[1]')
        if teacher in teacher_list:
            actual='add-success'
        else:
            actual='add-fail'
        self.assertEqual(actual,expect)

    # 测试查询
    @parameterized.expand(query_course_info)
    @unittest.skip('fa')
    def test_query_coure(self,campus,teacher,speialty,start_tiame,end_tiame,expect):
        query_all_course_info = {'campus':campus, 'teacher':teacher, 'specialty': speialty,
                                 'start_time': start_tiame, 'end_time': end_tiame
                                 }
        self.ca.do_query(query_all_course_info)
        query_num=Service.get_num(self.driver,'//*[@id="course"]/div[2]/div[2]/div[4]/div[1]/span[1]')

        if int(query_num) > 0:
            actual='query-success'
        else:
            actual = 'query-fail'

        self.assertEqual(actual,expect)

    # 测试修改
    @parameterized.expand(alter_course_info)
    def test_alter_course(self,start_time,end_time,teacher,classroom,classcode,course,expect):
        alter_course_info = {"start_time":start_time,"end_time":end_time,"teacher":teacher,
                           "classroom":classroom,"classcode":classcode,"course":course}
        self.ca.do_alter_course(alter_course_info)

        # classnum = self.ca.click_alter()

        teacher_list=Service.get_page_ele(self.driver,f'//*[@id="course_table"]/tbody/tr[1]/td[1]')

        if teacher in teacher_list:
            actual='alter-success'
        else:
            actual='alter-fail'
        self.assertEqual(actual,expect)
       

if __name__ == '__main__':
    unittest.main(verbosity=2)