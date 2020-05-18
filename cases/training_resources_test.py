# -*- encoding: utf-8 -*-
# File    : training_resources_test
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/17 20:39
#分配资源的测试类
import time
import unittest
import warnings

from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized

class TranningResourcesTest(unittest.TestCase):
    #获取测试数据
    contents=Utility.get_json('../conf/yang/testinfo.conf')
    # print(contents[1])
    tranning_resources_info=Utility.tran_tuple(contents[1])
    print(tranning_resources_info)

    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        self.driver=Service.get_driver()
        self.driver.implicitly_wait(15)
        from lib.training_resources import TrainingResources
        Service.ignor_login_decrypt(self.driver)
        self.tr=TrainingResources(self.driver)
    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        pass

    # 测试增加
    @parameterized.expand(tranning_resources_info)
    def test_add_resources(self,cus_tel,cus_name,cus_sex,cus_last_status,cus_wechat,cus_qq,
                           cus_school,cus_education,cus_major,cus_intent,cus_workage,cus_salary,
                           cus_source,cus_email,cus_age,cus_eduexp,cus_experience,cus_last_tracking_remark,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        #获取页面数据条数
        old_num=Service.get_num(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        add_resources_info = {"cus.tel": cus_tel, "cus.name": cus_name,
          "cus.sex": cus_sex,"cus.last_status": cus_last_status,"cus.wechat": cus_wechat,
          "cus.qq": cus_qq, "cus.school": cus_school, "cus.education": cus_education,
          "cus.major": cus_major, "cus.intent": cus_intent, "cus.workage": cus_workage,
          "cus.salary": cus_salary,"cus.source": cus_source, "cus.email": cus_email,
          "cus.age": cus_age,"cus.eduexp": cus_eduexp, "cus.experience": cus_experience,
          "cus.last_tracking_remark": cus_last_tracking_remark}
        self.tr.do_add_resources(add_resources_info)

        # #执行数据后,点击搜索
        # self.tr.click_query()
        # new_num=Service.get_num(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        #
        #
        # if int(new_num)-int(old_num)==1:
        #     actual='add-success'
        # else:
        #     actual='add-fail'
        #     Utility.get_error_png(self.driver)
        # self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)