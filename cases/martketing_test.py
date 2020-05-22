import unittest
import warnings
from parameterized import parameterized
from lib.marketing import Marketing
from tools.utility import Utility
from tools.service import Service
import re
class MarketingTest(unittest.TestCase):
    # 获取测试数据
    contents = Utility.get_json('../conf/yun/testinfo.conf')
    add_marketing_info = Utility.tran_tuple(contents[0])
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self):
        self.driver = Service.get_driver('../conf/yun/base.conf')
        self.driver.implicitly_wait(15)
        from lib.marketing import Marketing
        self.mar = Marketing(self.driver)
        self.old_total = self.mar.total(self.driver)

    # 测试增加
    @parameterized.expand(add_marketing_info)
    def test_add(self, region_id, department_id, tel, name, sex, last_status, wechat, qq,
                     school, education, major, workage, age, source, eduexp, experience, last_tracking_remark,
                     expect):

        add_info = {"cus.region_id": region_id, "cus.department_id": department_id,
                        "cus.tel": tel, "cus.name": name, "cus.sex": sex,
                        "cus.last_status": last_status, "cus.wechat": wechat, "cus.qq": qq,
                        "cus.school": school, "cus.education": education, "cus.major": major,
                        "cus.workage": workage, "cus.age": age, "cus.source": source,
                        "cus.eduexp": eduexp, "cus.experience": experience,
                        "cus.last_tracking_remark": last_tracking_remark,
                        }
        self.mar.do_add(self.driver, add_info)
            # self.driver.refresh()
            # 执行数据后,点击搜索
        new_total = self.mar.total(self.driver)
        if new_total != self.old_total:
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
