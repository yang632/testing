import unittest
import warnings
from parameterized import parameterized
from lib.class_service import Class_service
from tools.utility import Utility
from tools.service import Service
class serviceTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/yun/testinfo.conf')
    #班级管理查询
    management_query_info = Utility.tran_tuple(contents[1])
    print(management_query_info)
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
        self.ser=Service()

    # 测试#班级管理查询
    @parameterized.expand(management_query_info)
    def test_query_data(self, regionId, status,expect):
        query_data_info = {"regionId":regionId,"status":status
                        }
        self.cla.do_query(query_data_info)
        total = self.ser.get_num(self.driver,'//*[@id="cmDiv"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        if total != 0:
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
