import unittest
import warnings
import re
from parameterized import parameterized
from lib.class_service import Class_service
from tools.utility import Utility
from tools.service import Service
class serviceTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/yun/testinfo.conf')
    #班级管理查询
    management_query_info = Utility.tran_tuple(contents[1])
    # 班级管理新增
    management_add_info = Utility.tran_tuple(contents[2])
    #学员考勤
    confirm=Utility.tran_tuple(contents[3])
    #学员请假查询
    leave_query=Utility.tran_tuple(contents[4])
    #学员请假修改
    change_leave=Utility.tran_tuple(contents[5])
    #学员请假新增
    add_leave=Utility.tran_tuple(contents[6])
    #学员转班
    change_class=Utility.tran_tuple(contents[7])

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self):
        self.driver = Service.get_driver('../conf/yun/base.conf')
        self.driver.implicitly_wait(15)
        self.cla= Class_service(self.driver)
    # 测试班级管理查询
    @parameterized.expand(management_query_info)
    #@unittest.skip("忽略增加")
    def test_query_data(self, regionId, status,expect):
        query_data_info = {"regionId":regionId,"status":status
                        }
        self.cla.do_query(query_data_info)
        total = Service.get_num(self.driver,'//*[@id="cmDiv"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        if total != 0:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    # 测试班级管理查询
    @parameterized.expand(management_add_info)
    #@unittest.skip("忽略增加")
    def test_add_data(self, class_no, orientation, opening_time,class_headmaster_id,expect):
        add_data_info = {"c.class_no": class_no, "c.orientation": orientation,
                         "c.opening_time":opening_time,"c.class_headmaster_id":class_headmaster_id}

        old_total=self.cla.do_add(add_data_info)
        import time
        time.sleep(2)
        new_total = Service.get_num(self.driver, '//*[@id="cmDiv"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        if new_total != old_total:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #测试考勤
    @parameterized.expand(confirm)
    #@unittest.skip("忽略增加")
    def test_confirm_data(self,attendance,expect):
        confirm_data_info = {"attendance": attendance
                        }

        old_total = self.cla.do_confirm(confirm_data_info)
        import time
        time.sleep(2)
        new_total = Service.get_kaoqin(self.driver,'/html/body/div[8]/div[2]/div/div/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[7]')
        if new_total != old_total:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #学员请假查询
    @parameterized.expand(leave_query)
    #@unittest.skip("忽略增加")
    def test_confirm_data(self,region_id,leave_status,expect):
        confirm_data_info = {"region_id":region_id,"leave_status":leave_status
                        }

        old_total = self.cla.do_leave_query(confirm_data_info)
        import time
        time.sleep(2)
        new_total = Service.get_num(self.driver,'//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')
        if new_total != old_total:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
     # 学员请假修改动作
    @parameterized.expand(change_leave)
    #@unittest.skip("忽略增加")
    def test_change_leave_data(self, stuName, reason, expect):
        change_leave_data_info = {"sl.stuName": stuName, "sl.reason": reason
                             }
        old_text = self.cla.change_leave(change_leave_data_info)
        import time
        time.sleep(2)
        new_text = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/span').text
        if new_text != old_text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    # 学员请假新增动作
    @parameterized.expand(add_leave)
    #@unittest.skip("忽略增加")
    def test_add_leave_data(self,start_time, end_time,leave_type,days,stuName,leave_count,reason,comment, expect):
        add_leave_data_info = {"sl.start_time":start_time,"sl.end_time":end_time,"sl.leave_type":leave_type,"sl.days":days,"sl.stuName": stuName, "sl.leave_count":leave_count,"sl.reason": reason,"sl.comment":comment
                                      }
        old_tatol = self.cla.change_leave(add_leave_data_info)
        import time
        time.sleep(2)
        new_tatol = Service.get_num(self.driver,'//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')
        if new_tatol != old_tatol:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    # 学员转班
    @parameterized.expand(change_class)
    #@unittest.skip("忽略增加")
    def test_change_class_data(self, regionId, stuClass,
                                expect):
        change_class_info = {"regionId": regionId, "stuClass": stuClass
                                   }
        old_text = self.cla.do_change_class(change_class_info)
        import time
        time.sleep(2)
        new_text = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]').text
        if new_text != old_text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
