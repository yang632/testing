# -*- coding:utf-8 -*-
#@Time      :2020/5/19
#@Author    :hxy
#@File      :course_arrangement_test.py

import unittest
import warnings
from tools.service import Service
from tools.utility import Utility
from lib.course_arrangement import CourseArrangement

class CouresArrangementTest(unittest.TestCase):

    #获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    # 获取添加的测试数据
    add_course_info = Utility.tran_tuple(contents[1])
    #获取查询的测试数据
    query_coure_info = Utility.tran_tuple(contents[2])

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore',ResourceWarning)

    def setUp(self) -> None:
        self.driver = Service.get_driver('../conf/huang/base.conf')
        self.driver.implicitly_wait(10)
        Service.ignor_login_decrypt(self.driver,'../conf/huang/base.conf')
        self.ca = CourseArrangement(self.driver)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)