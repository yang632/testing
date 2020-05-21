# -*- encoding: utf-8 -*-
# File    : student_test
# Author  : T430s1
# Email   : sc2818@163.com
# Software: PyCharm
# Time    : 2020/5/19 14:20
import unittest
import time


from lib.student import Student
from tools.service import Service
from  parameterized import parameterized

from tools.utility import Utility


class StudentTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/peng/testinfo.conf')
    print(contents[0])
    query_student_info = Utility.tran_tuple(contents[0])
    print(query_student_info)

    edit_student_info=Utility.tran_tuple(contents[1])

    @classmethod
    def setUpClass(cls):
        pass



    def setUp(self):
        self.driver = Service.get_driver("../conf/peng/base.conf")
        self.driver.implicitly_wait(10)
        self.student =Student(self.driver)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass


    @parameterized.expand(query_student_info)
    # @unittest.skip("忽略查询学员")
    def test_query_student(self,area,sname,state,direction,sclass,expect):
        query_student_data={"s_area":area,"s_name":sname,"s_state":state,"s_direction":direction,"s_sclass":sclass}
        self.student.query_student(query_student_data)
        time.sleep(2)

        num=self.student.get_student_total()

        if int(num) >0 :
            actual="query-success"

        else:
            actual="query-fail"

        self.assertEqual(actual,expect)



    @parameterized.expand(edit_student_info)
    def test_edit_student(self,edit_name,edit_state,edit_tel,edit_source,expect):
        edit_student_data={"edit_name":edit_name,"edit_state":edit_state,"edit_tel":edit_tel,"edit_source":edit_source}
        self.student.do_edit_student(edit_student_data)


        # 进行搜索
        self.driver.refresh()
        time.sleep(2)
        self.student.input_name(edit_name)

        self.student.click_query_button()

        list = []
        contents = self.driver.find_elements_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[6]")
        for content in contents:
            list.append(content.text)

        if edit_state in list:
            actual="edit-success"

        else:
            actual="edit-fail"


        self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)


