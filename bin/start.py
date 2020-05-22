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

        # names_1 = Utility.get_str('../conf/yun/test.conf')
        # print(names_1)
        # names = Utility.get_str('../conf/yang/test.conf')
        # print(names)
        huangnames = Utility.get_str('../conf/huang/test.conf')
        print(huangnames)
        # pengnames=Utility.get_str('../conf/peng/test.conf')
        # print(pengnames)
        # tests=loader.loadTestsFromNames(huangnames)

        # names.extend(huangnames)
        # huangnames.extend(names)

        test=loader.loadTestsFromNames(huangnames)

        suit.addTest(test)
=======
        names = Utility.get_str('../conf/yang/test.conf')
        # huangnames.extend(names)
        tests=loader.loadTestsFromNames(names)
        suit.addTests(tests)
>>>>>>> 0fe107b6dd92f59034d1b54ad6a7d261a3c6af95
        with open (f"..//reports/{Utility.ctime()}.html","w") as file:
            from HTMLTestRunner import HTMLTestRunner
            runner=HTMLTestRunner(stream=file,verbosity=2)
            runner.run(suit)

if __name__ == '__main__':
    Start().start()

