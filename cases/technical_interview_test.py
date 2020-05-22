# -*- coding:utf-8 -*-
#@Time      :2020/5/20
#@Author    :hxy
#@File      :technical_interview.py：技术面试测试


import unittest
import warnings
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized
from lib.technical_interview import TechnicalInterview

class TechnicalInterviewTest(unittest.TestCase):

    # 获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    # 获取技术面试的测试数据
    add_interview_info = Utility.tran_tuple(contents[4])

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore',ResourceWarning)

    def setUp(self):
        self.driver = Service.get_driver('../conf/huang/base.conf')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        Service.ignor_login_decrypt(self.driver,'../conf/huang/base.conf')
        self.ti = TechnicalInterview(self.driver)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass

    # 测试面试
    @parameterized.expand(add_interview_info)
    def test_add_interview(self,outcome,evaluate,expect):
        add_interview_info = {"outcome":outcome,"evaluate":evaluate}

        self.ti.do_interview(add_interview_info)

        # 获取面试的随机值
        # studentnum = self.ti.click_interview()
        outcome_list = Service.get_page_ele(self.driver,'//*[@id="stuInfo_table"]/tbody/tr[1]/td[8]')

        # print(studentnum)
        # print(outcome_list)
        if outcome in outcome_list:
            actual = 'add-success'
        else:
            actual = 'add-fail'
        
        self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)