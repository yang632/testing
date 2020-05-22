# -*- coding:utf-8 -*-
#@Time      :2020/5/21
#@Author    :hxy
#@File      :teacher_on_duty_test.py：教师值班测试

import unittest
import warnings
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized
from lib.teacher_on_duty import TeacherOnDuty

class TeacherOnDutyTest(unittest.TestCase):

    # 获取测试数据
    contents = Utility.get_json('../conf/huang/testinfo.conf')
    # 获取新增教师值班的测试数据
    add_duty_info = Utility.tran_tuple(contents[5])
    # 获取修改教室值班的数据
    alter_duty_info = Utility.tran_tuple(contents[6])


    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore',ResourceWarning)

    def setUp(self):
        self.driver = Service.get_driver('../conf/huang/base.conf')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        Service.ignor_login_decrypt(self.driver,'../conf/huang/base.conf')
        self.tod = TeacherOnDuty(self.driver)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass


    # 测试新增值班
    @parameterized.expand(add_duty_info)
    def test_add_duty(self,teacher,duty_time,expect):
        add_duty_info = {"teacher":teacher,"duty_time":duty_time}

        self.tod.do_add_duty(add_duty_info)

        teachername_list = Service.get_page_ele(self.driver,'//*[@id="duty_table"]/tbody/tr[1]/td[2]')
        print(teacher)
        print(teachername_list)

        if teacher in teachername_list:
            actual = 'add-success'
        else:
            actual = 'add-fail'
        
        self.assertEqual(actual,expect)

    
    #测试修改值班
    @parameterized.expand(alter_duty_info)
    def test_alter_duty(self,teacher,duty_time,expect):
        alter_duty_info = {"teacher": teacher,"duty_time": duty_time}
        # 执行修改
        self.tod.do_alter_duty(alter_duty_info)
        #获取修改的随机数
        alternum = self.tod.click_alter()
        # 获取界面老师名字元素
        teachername_list = Service.get_page_ele(self.driver, f'//*[@id="duty_table"]/tbody/tr[{alternum}]/td[2]')

        if teacher in teachername_list:
            actual = 'alter-success'
        else:
            actual = 'alter-success'

        self.assertEqual(actual, expect)

if __name__ == "__main__":
    unittest.main(verbosity=2)