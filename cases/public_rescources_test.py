# -*- encoding: utf-8 -*-
# File    : public_rescources_test
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 15:59
import unittest
import warnings

from tools.service import Service


class PublicRescourcesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
    def setUp(self):
        self.driver=Service.get_driver('../conf/yang/base.conf')
        self.driver.implicitly_wait(15)
        Service.ignor_login_decrypt(self.driver,'../conf/yang/base.conf')

    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        pass
