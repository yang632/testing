# -*- coding:utf-8 -*-
#@Time      :2020/5/19
#@Author    :hxy
#@File      :course_arrangement_test.py

import unittest
from tools.utility import Utility

class CouresArrangementTest(unittest.TestCase):

    #获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    # 获取
    course_arrangement_info = Utility.tran_tuple(contents[1])



if __name__ == '__main__':
    unittest.main(verbosity=2)