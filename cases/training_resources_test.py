# -*- encoding: utf-8 -*-
# File    : training_resources_test
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/17 20:39
#分配资源的测试类
import unittest
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized

class TranningResourcesTest(unittest.TestCase):
    #获取测试数据
    contents=Utility.get_json('../conf/yang/testinfo.conf')
    # print(contents[1])
    tranning_resources_info=Utility.tran_tuple(contents[1])
    # print(tranning_resources_info)




    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        self.driver=Service.get_driver('../conf/yang/base.conf')
        self.driver.implicitly_wait(15)
        from lib.training_resources import TrainingResources
        tr=TrainingResources(self.driver)
    def tearDown(self):
        self.driver.close()
    @classmethod
    def tearDownClass(cls):
        pass

    #测试增加
    @parameterized.expand(tranning_resources_info)
    def test_add_resources(self):
