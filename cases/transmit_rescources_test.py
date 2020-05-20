# -*- encoding: utf-8 -*-
# File    : transmit_rescources_test
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 21:01
import time
import unittest
import warnings
from parameterized import parameterized
from lib.transmit_rescources import TransmitRescources
from tools.service import Service
from tools.utility import Utility


class TransmitRescourcesTest(unittest.TestCase):

    #获取转交资源的测试数据
    contents = Utility.get_json('../conf/yang/public_rescources_testinfo.conf')
    transmit_info=Utility.tran_tuple(contents[2])
    print(transmit_info)
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
    def setUp(self):
        self.driver=Service.get_driver('../conf/yang/base.conf')
        self.driver.implicitly_wait(15)
        #使用管理员进行登录,进入转交责任人
        Service.ignor_login_decrypt(self.driver,'../conf/yang/base_admin.conf')
        self.tran=TransmitRescources(self.driver)
    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        pass


    # 测试查询
    @parameterized.expand(transmit_info)
    def test_do_transmit_rescources(self,area_text_value,dpt_text_value,empname_text_value, \
                                    status_text_value, source_text_value,name_text_value,transmit_area_value,
                                    transmit_dpt_value,transmit_empname_value,expect ):
        transmit_rescources_info={
        "area_text_value":area_text_value,"dpt_text_value": dpt_text_value,
        "empname_text_value": empname_text_value,"status_text_value": status_text_value,
        "source_text_value": source_text_value,'name_text_value':name_text_value,
        "transmit_area_value": transmit_area_value,"transmit_dpt_value": transmit_dpt_value,"transmit_empname_value": transmit_empname_value}

        old_num=self.tran.do_query_rescources(transmit_rescources_info)
        print(old_num)
        #随机执行分配
        self.tran.do_transmit_rescources(int(old_num),transmit_rescources_info)
        # #再次执行搜索
        new_num = self.tran.do_query_rescources(transmit_rescources_info)
        print(new_num)
        time.sleep(2)
        if int(old_num) - int(new_num):
            actual='transmit-success'
        else:
            actual='transmit-fail'

        self.assertEqual(actual,expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)