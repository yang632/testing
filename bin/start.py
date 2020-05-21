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
        #创建测试套
        suit=unittest.TestSuite()
        #创建加载器
        loader = unittest.TestLoader()
        names = Utility.get_str('../conf/yang/test.conf')
<<<<<<< HEAD
        huangnames = Utility.get_str('../conf/huang/test.conf')
        pengnames=Utility.get_str('../conf/peng/test.conf')
        print(pengnames)
        tests=loader.loadTestsFromNames(pengnames)
=======
        # huangnames = Utility.get_str('../conf/huang/test.conf')
        # print(huangnames)
        # names.extend(huangnames)
        tests=loader.loadTestsFromNames(names)
>>>>>>> 99f54f3d2551ff7694551642c75a7582ed3a5774
        suit.addTests(tests)
        with open (f"..//reports/{Utility.ctime()}.html","w") as file:
            from HTMLTestRunner import HTMLTestRunner
            runner=HTMLTestRunner(stream=file,verbosity=2)
            runner.run(suit)
if __name__ == '__main__':
    Start().start()

