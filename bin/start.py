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
<<<<<<< HEAD
        names = Utility.get_str('../conf//test.conf')

=======

        # names_1 = Utility.get_str('../conf/yun/test.conf')
        # print(names_1)
        names = Utility.get_str('../conf/yang/test.conf')
        # print(names)
>>>>>>> 189a9962cb30d077095cf334b068028b44ee26c3
        huangnames = Utility.get_str('../conf/huang/test.conf')
        # print(huangnames)
        # pengnames=Utility.get_str('../conf/peng/test.conf')
        # print(pengnames)
        # tests=loader.loadTestsFromNames(huangnames)
<<<<<<< HEAD
        # names.extend(huangnames)
        # print(names)
        tests=loader.loadTestsFromNames(names)
=======

        names.extend(names_1)
        huangnames.extend(names)
        pengnames.extend(huangnames)
        print(pengnames)
        tests=loader.loadTestsFromNames(pengnames)

<<<<<<< HEAD
        # huangnames = Utility.get_str('../conf/huang/test.conf')
        # print(huangnames)
        # names.extend(huangnames)
        # tests=loader.loadTestsFromNames(names)

=======
>>>>>>> 189a9962cb30d077095cf334b068028b44ee26c3
>>>>>>> 72c0044c1ea4aceaff638310995f2f0c14988e69
        suit.addTests(tests)
        with open (f"..//reports/{Utility.ctime()}.html","w") as file:
            from HTMLTestRunner import HTMLTestRunner
            runner=HTMLTestRunner(stream=file,verbosity=2)
            runner.run(suit)
if __name__ == '__main__':
    Start().start()

