# -*- encoding: utf-8 -*-
# File    : public_rescources_test
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 15:59
import time
import unittest
import warnings
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized

class PublicRescourcesTest(unittest.TestCase):
    #获取查询公共池的数据
    contents = Utility.get_json('../conf/yang/public_rescources_testinfo.conf')
    query_public_info=Utility.tran_tuple(contents[0])
    #获取废弃的数据
    claim_public_info=Utility.tran_tuple(contents[1])
    # print(claim_public_info)


    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
    def setUp(self):
        self.driver=Service.get_driver('../conf/yang/base.conf')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        Service.ignor_login_decrypt(self.driver,'../conf/yang/base.conf')
        from lib.public_rescources import PublicRescources
        self.pu=PublicRescources(self.driver)
    def tearDown(self):
        self.driver.close()
    @classmethod
    def tearDownClass(cls):
        pass
    #测试搜索
    @parameterized.expand(query_public_info)
    # @unittest.skip("忽略搜索")
    def test_do_query_public(self,area_value,dpt_value,abandoned_value,status_value,source_value ,\
            education_value,name_value,expect):
        query_public_info={"area_value":area_value,'dpt_value':dpt_value,'abandoned_value':abandoned_value,'status_value':status_value,
            'source_value':source_value,'education_value':education_value,'name_value':name_value}
        driver=self.driver
        self.pu.do_query_public(query_public_info)
        time.sleep(4)
        #获取页面元素
        num=Service.get_num(driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')

        print(num)
        if int(num) > 0:
            actual='query-success'
        else:
            actual='query-fail'

        self.assertEqual(actual,expect)


    #测试认领
    @parameterized.expand(claim_public_info)
    def test_do_claim_rescources(self,temp,expect):

        #获取此生页面显示数量
        time.sleep(2)
        old_num=Service.get_num(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')

        self.pu.do_claim_rescources(int(old_num))

        #点击默认搜索
        self.driver.refresh()
        self.pu.click_public_query()
        time.sleep(2)
        new_num = Service.get_num(self.driver, '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')

        if int(old_num) - int(new_num) == 1:
                actual='claim-success'
        else:
            actual='claim-fail'
        self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)