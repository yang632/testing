# -*- encoding: utf-8 -*-
# File    : weekmark_test
# Author  : T430s1
# Email   : sc2818@163.com
# Software: PyCharm
# Time    : 2020/5/20 11:49

import unittest
import time

from selenium.webdriver.common.by import By

from lib.student import Student
from lib.week_mark import WeekMark
from tools.service import Service
from  parameterized import parameterized

from tools.utility import Utility


class WeekMarkTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/peng/testinfo.conf')
    print(contents[0])
    query_week_info = Utility.tran_tuple(contents[2])
    print(query_week_info)

    import_week_info=Utility.tran_tuple(contents[3])
    import_week_info_plus=Utility.tran_tuple(contents[4])
    @classmethod
    def setUpClass(cls):
        pass



    def setUp(self):
        self.driver = Service.get_driver("../conf/peng/base.conf")
        self.driver.implicitly_wait(10)
        self.week =WeekMark(self.driver)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass


    @parameterized.expand(query_week_info)
    @unittest.skip("忽略查询")
    def test_query_week(self,s_name,s_area,s_sclass,expect):
        query_week_data={"s_name":s_name,"s_area":s_area,"s_sclass":s_sclass}

        self.week.query_mark(query_week_data)
        time.sleep(2)

        num = self.week.get_student_total()

        if int(num) > 0:
            actual = "query-success"

        else:
            actual = "query-fail"

        self.assertEqual(actual, expect)



    @parameterized.expand(import_week_info)
    @unittest.skip("忽略录用")
    def test_import_week(self,s_sclass,stage,week,score,expect):
        import_week_data={"s_sclass":s_sclass,"stage":stage,"week":week,"score":score}
        self.week.do_week_mark(import_week_data)
        if Service.is_element_present(self.driver, By.XPATH, "/html/body/div[11]/div/div/div[1]/h4"):
            actual = "import-fail"
        else:
            actual="import-success"

        self.assertEqual(actual,expect)



    @parameterized.expand(import_week_info_plus)
    # @unittest.skip("")
    def test_import_week_two(self,s_sclass,stage,week,file,expect):
        import_week_data_plus={"s_sclass":s_sclass,"stage":stage,"week":week,"file":file}
        self.week.do_import(import_week_data_plus)
        time.sleep(2)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR, ".bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)"):
            actual = "import-fail"
        else:
            actual = "import-success"

        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)