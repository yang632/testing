# -*- encoding: utf-8 -*-
# File    : login_test
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 17:59
import time
import unittest
from tools.service import Service
from parameterized import parameterized

from tools.utility import Utility


class LoginTest(unittest.TestCase):
    #获取测试数据
    content=Utility.get_json('../conf/yang/testinfo.conf')
    login_info=Utility.tran_tuple(content[0])
    print(login_info)

    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        self.driver=Service.get_driver()
        from lib.login import Login
        self.login=Login(self.driver)
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    #测试登录
    @parameterized.expand(login_info)
    def test_login(self,uname,psword,code,expect):
        self.login.do_login(uname,psword,code)

        from selenium.webdriver.common.by import By
        #如果存在注销链接
        if Service.is_element_present(self.driver,By.LINK_TEXT,"注销"):
            actual="login-success"
            #退出系统
            time.sleep(3)
            self.login.click_logout()
        else:
            actual="login-fail"

        self.assertEqual(actual,expect)
if __name__ == '__main__':
    unittest.main(verbosity=2)