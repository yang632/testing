# -*- encoding: utf-8 -*-
# File    : overall_score_test
# Author  : T430s1
# Email   : sc2818@163.com
# Software: PyCharm
# Time    : 2020/5/20 16:39

import unittest
import time
from selenium.webdriver.common.by import By

from lib.overall_score import OverallScore
from lib.student import Student
from lib.week_mark import WeekMark
from tools.service import Service
from  parameterized import parameterized

from tools.utility import Utility


class OverallTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/peng/testinfo.conf')
    print(contents[0])
    query_week_info = Utility.tran_tuple(contents[8])
    print(query_week_info)
    @classmethod
    def setUpClass(cls):
        pass



    def setUp(self):
        self.driver = Service.get_driver("../conf/peng/base.conf")
        self.driver.implicitly_wait(10)
        self.score =OverallScore(self.driver)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand(query_week_info)
    def test_query_score(self,s_area,s_name,s_stage,s_direction,s_sclass,expect):
        query_week_data={"s_area":s_area,"s_name":s_name,"s_stage":s_stage,
                         "s_direction":s_direction,"s_sclass":s_sclass}
        self.score.query_score(query_week_data)
        time.sleep(2)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR, ".no-records-found > td:nth-child(1)"):
            actual = "none"
        else:

            num = self.score.get_student_total()

            if int(num) > 0:
                actual = "query-success"
            else:
                actual = "query-fail"
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)