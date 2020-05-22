# -*- coding:utf-8 -*-
#@Time      :2020/5/21
#@Author    :hxy
#@File      :application_for_extra_work_test.py：加班申请测试

import unittest
import warnings
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized
from lib.application_for_extra_work import ApplicationForExtraWork

class ApplicationForExtraWorkTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    # 获取加班申请的测试数据
    add_overtime_info = Utility.tran_tuple(contents[7])
    print(add_overtime_info)

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore',ResourceWarning)

    def setUp(self):
        self.driver = Service.get_driver('../conf/huang/base.conf')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        Service.ignor_login_decrypt(self.driver,'../conf/huang/base.conf')
        self.afew = ApplicationForExtraWork(self.driver)

    def tearDown(self):
        # pass
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass


    #测试值班申请
    @parameterized.expand(add_overtime_info)

    def test_add_overtime(self,start_time,end_time,accounting,hours,region,reason,expect):
        add_overtime_info = {"start_time":start_time,"end_time":end_time,"accounting": accounting,
                            "hours":hours, "region":region,"reason": reason
                            }
        overtime_info = {
            "start_js": "document.querySelector(\"#addApply-form > div > div > div:nth-child(2) > div:nth-child(1) > input\")",
            "end_js": "document.querySelector(\"#addApply-form > div > div > div:nth-child(2) > div:nth-child(2) > input\")",
            "start_time": "2020-05-10 09:30", "end_time": "2020-05-10 11:30",
            "accounting": "结算工资", "hours": "2小时", "region": "成都",
            "reason": "没钱要赚更多的钱买买买"
            }
        # print(add_overtime_info)

        self.afew.do_overtime(add_overtime_info)

        reason_list = Service.get_page_ele(self.driver,'//*[@id="apply-table"]/tbody/tr[1]/td[7]/span')
        if reason in reason_list:
            actual = 'add-success'
        else:
            actual = 'add-fail'

        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)