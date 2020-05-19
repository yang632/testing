from tools.service import Service
import re
import time
class Class_service:
    def __init__(self,driver):
        self.driver=driver
        Service.ignor_login_decrypt(self.driver,'..\\conf\\yun\\base.conf')

    #打开班级管理
    def class_management(self):
        Service.open_menu(self.driver, '班务管理')
        Service.open_menu(self.driver, '班级管理')

    #区域查询
    def area_query(self,region_id):
        select_area=self.driver.find_element_by_xpath("//*[@id='cmDiv']/div[1]/select[1]").click()
        Service.select_text(select_area,region_id)
    #状态查询
    def status_query(self, status):
        select_status = self.driver.find_element_by_xpath('//*[@id="cmDiv"]/div[1]/select[2]').click()
        Service.select_text(select_status,status)

    #新增
    def button_add(self,tel):
        self.driver.find_element_by_xpath("//*[@id='cmDiv']/div[1]/button").click()

    #班名
    def input_classname(self,name):
        classname = self.driver.find_element_by_xpath('''//*[@id="addClass-form"]/div/div[1]/input''')
        Service.send_input(classname,name)
    #方向
    def mm(self):
        mm=self.driver.find_element_by_xpath('//*[@id="addClass-form"]/div/div[2]/select')
        Service.select_text(select_status, status)

    #pageSize = 10 & pageIndex = 1 & regionId = & openStatus = 02
    #执行动作
    def do_add(self,driver,add_data):
        self.open_marketing_page(self.driver)
        self.add_button()
        self.select_area(add_data["cus.region_id"])
        self.select_department(add_data["cus.department_id"])
        self.input_tel(add_data["cus.tel"])


if __name__ == '__main__':
    pass