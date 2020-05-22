# -*- encoding: utf-8 -*-
# File    : start
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 20:11
from tools.utility import Utility
import unittest
class Start:
    @classmethod
    def start(cls):
        # 创建测试套
        suit=unittest.TestSuite()
        #创建加载器
        loader = unittest.TestLoader()
        names = Utility.get_str('../conf/yang/test.conf')
        # huangnames.extend(names)
        tests=loader.loadTestsFromNames(names)
        suit.addTests(tests)
        with open (f"..//reports/{Utility.ctime()}.html","w") as file:
            from HTMLTestRunner import HTMLTestRunner
            runner=HTMLTestRunner(stream=file,verbosity=2)
            runner.run(suit)
if __name__ == '__main__':
    Start().start()

