# -*- encoding: utf-8 -*-
# File    : login_testing
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 17:59
import time
import unittest
from tools.service import Service
from parameterized import parameterized
from tools.utility import Utility
import warnings
class LoginTest(unittest.TestCase):
    #获取测试数据
    content=Utility.get_json('../../conf/yang/testinfo.conf')
    login_info=Utility.tran_tuple(content[0])
    print(login_info)
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        self.driver=Service.get_driver()
        self.driver.implicitly_wait(15)
        from lib.login import Login
        self.login=Login(self.driver)
    def tearDown(self):
        self.driver.close()
    @classmethod
    def tearDownClass(cls):
        pass
    #测试登录
    @parameterized.expand(login_info)
    def test_login(self,uname,psword,code,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        self.login.do_login(uname,psword,code)
        # time.sleep(25)
        from selenium.webdriver.common.by import By
        #如果存在注销链接
        time.sleep(3)
        if Service.is_element_present(self.driver,By.PARTIAL_LINK_TEXT,"修改密码"):
            actual="login-success"
            #退出系统
            self.login.click_logout()
        else:
            actual="login-fail"

        self.assertEqual(actual,expect)
if __name__ == '__main__':
    unittest.main(verbosity=2)