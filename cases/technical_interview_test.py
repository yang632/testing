# -*- coding:utf-8 -*-
#@Time      :2020/5/20
#@Author    :hxy
#@File      :technical_interview.py：技术面试测试


import unittest
import warnings

from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized

class TechnicalInterviewTest(unittest.TestCase):

    # 获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    