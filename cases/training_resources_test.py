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

    rescoure_query_info=Utility.tran_tuple(contents[2])
    # print(rescoure_query_info)

    discard_info=Utility.tran_tuple(contents[3])
    # print(discard_info)

    #跟踪资源的测试数据
    track_resource_info=Utility.tran_tuple(contents[4])
    print(track_resource_info)


    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
    def setUp(self):
        self.driver=Service.get_driver('../conf/yang/base.conf')
        self.driver.implicitly_wait(15)
        from lib.training_resources import TrainingResources
        Service.ignor_login_decrypt(self.driver,'../conf/yang/base.conf')
        self.tr=TrainingResources(self.driver)
    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        pass

    # 测试增加
    @parameterized.expand(tranning_resources_info)
    @unittest.skip("1")
    def test_add_resources(self,cus_tel,cus_name,cus_sex,cus_last_status,cus_wechat,cus_qq,
                           cus_school,cus_education,cus_major,cus_intent,cus_workage,cus_salary,
                           cus_source,cus_email,cus_age,cus_eduexp,cus_experience,cus_last_tracking_remark,expect):

        add_resources_info = {"cus.tel": cus_tel, "cus.name": cus_name,
          "cus.sex": cus_sex,"cus.last_status": cus_last_status,"cus.wechat": cus_wechat,
          "cus.qq": cus_qq, "cus.school": cus_school, "cus.education": cus_education,
          "cus.major": cus_major, "cus.intent": cus_intent, "cus.workage": cus_workage,
          "cus.salary": cus_salary,"cus.source": cus_source, "cus.email": cus_email,
          "cus.age": cus_age,"cus.eduexp": cus_eduexp, "cus.experience": cus_experience,
          "cus.last_tracking_remark": cus_last_tracking_remark}
        self.tr.do_add_resources(add_resources_info)

        #执行数据后,点击搜索
        self.tr.query_input_name(cus_name)
        self.tr.click_query()

        tel_list=Service.get_page_ele(self.driver,'//*[@id="personal-table"]/tbody/tr/td[6]')
        if cus_tel in tel_list:
            actual='add-success'
        else:
            actual='add-fail'
        self.assertEqual(actual,expect)



    #测试搜索
    @parameterized.expand(rescoure_query_info)
    @unittest.skip("1")
    def test_do_query(self,resource,status,source,start_time,end_time,query_name,consultant,expect):
        query_resource_info = {'resource': resource, 'status':status, 'source': source,
                               'start_time': start_time, 'end_time': end_time, 'query_name':query_name,
                               "consultant": consultant
                               }


        self.tr.do_query(query_resource_info)
        time.sleep(2)
        qury_num=Service.get_num(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        # print(qury_num_list)
        if int(qury_num) > 0:
            actual='query-success'
        else:
            actual="query-fail"
        self.assertEqual(actual,expect)


    #测试废弃
    @parameterized.expand(discard_info)
    # @unittest.skip('2')
    def test_discard_resource(self,end,expect):
        driver=self.driver
        #获取废弃前的数量
        self.tr.click_query()
        old_num=Service.get_num(driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        # print(old_num)
        self.tr.discard_resource(old_num)
        #点击搜索
        self.tr.click_query()
        time.sleep(4)
        #获取废弃后的数量
        new_num=Service.get_num(driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        # print(new_num)
        if int(old_num) - int(new_num) == 1:
            actual='discard-success'
        else:
            actual='discard-fail'
        print(actual)
        self.assertEqual(actual,expect)


    #测试跟踪资源
    @parameterized.expand(track_resource_info)
    def test_do_track_resource(self,new_status,priority,next_time,track_keys,s_class,
                               payment_way,fee,account,amount,trade_time,expect
                               ):
        track_resource_info={"new_status":new_status,'priority':priority,
        'next_time':next_time,'track_keys':track_keys,'class':s_class,
        'payment_way':payment_way,'fee':fee,'account':account,'amount':amount,
        'trade_time':trade_time }

        #点击搜索
        self.tr.click_query()
        #获取页面上的列表个数
        old_num=Service.get_num(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        old_num=int(old_num)

        track_resource_tel=self.tr.do_track_resource(old_num,track_resource_info)

        #搜索电话号码进行断言
        self.tr.query_input_name(track_resource_tel)
        self.tr.click_query()
        #获取此时的电话号码信息
        tel_list=Service.get_page_ele(self.driver,'//*[@id="personal-table"]/tbody/tr/td[6]')
        if track_resource_tel in tel_list:
            actual='track-success'
        else:
            actual='track-fail'

        self.assertEqual(actual,expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)