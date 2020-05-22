from tools.service import Service
import re
import time
class Marketing:
    def __init__(self,driver):
        self.driver=driver
        Service.ignor_login_decrypt(self.driver,'..\\conf\\yun\\base.conf')
    #获取列表总数
    def total(self,driver):
        Service.open_menu(self.driver, '资源管理')
        Service.open_menu(self.driver, '培训资源')
        self.driver.find_element_by_css_selector("button.btn:nth-child(7)").click()
        # 获取数量
        content = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]').text
        return re.findall(r"总共 (.*?)条记录", content)[0]

    def open_marketing_page(self,driver):
        Service.open_menu(self.driver, '市场营销')
        Service.open_menu(self.driver, '简历资源')

    #新增
    def add_button(self):
        self.driver.find_element_by_css_selector("button.btn:nth-child(9)").click()
    #区域
    def select_area(self, region_id):
        select_area = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[1]/select')
        Service.select_text(select_area,region_id)
    #部门
    def select_department(self, cusIsExist):
        select_department = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[2]/select")
        Service.select_text(select_department,cusIsExist)
    #电话
    def input_tel(self,tel):
        telphone = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[3]/input")
        Service.send_input(telphone,tel)
    #姓名
    def input_name(self,name):
        studentname = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[4]/input")
        Service.send_input(studentname,name)

    # 性别
    def select_sex(self,sex):
        select_sex = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[5]/select")
        Service.select_text(select_sex,sex)
    #最新状态
    def select_status(self,last_status):
        select_status=self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[6]/select")
        Service.select_text(select_status,last_status)
    #微信
    def input_wechat(self,wechat):
        wechatnum = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[7]/input")
        Service.send_input(wechatnum,wechat)
    #QQ
    def input_qq(self,qq):
        qqnum=self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[8]/input")
        Service.send_input(qqnum,qq)
    #学校
    def input_school(self,school):
        schoolname = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[9]/input")
        Service.send_input(schoolname,school)
    #学历
    def select_education(self,education):
        select_education=self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[10]/select")
        Service.select_text(select_education,education)
    #专业
    def input_major(self,major):
        majorname = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[11]/input")
        Service.send_input(majorname, major)
    #工作年限
    def select_workage(self,workage):
        select_workage=self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[12]/select")
        Service.select_text(select_workage, workage)
    #年龄
    def input_age(self,age):
        agenum=self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[13]/input")
        Service.send_input(agenum,age)
    #渠道来源
    def select_source(self,source):
        select_source=self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div/div[14]/select")
        Service.select_text(select_source,source)
    #教育经历
    def input_eduxep(self,eduxep):
        input_eduxep=self.driver.find_element_by_xpath("//*[@id='addResource-form']/div/div/div[15]/textarea")
        Service.send_input(input_eduxep,eduxep)
    #工作经历
    def input_experience(self,experience):
        input_experience=self.driver.find_element_by_xpath("//*[@id='addResource-form']/div/div/div[16]/textarea")
        Service.send_input(input_experience,experience)
    #最后跟踪
    def input_last_tracking_remark(self,last_tracking_remark):
        input_last_tracking_remark = self.driver.find_element_by_xpath("//*[@id='addResource-form']/div/div/div[17]/textarea")
        Service.send_input(input_last_tracking_remark,last_tracking_remark)
    #保存
    def addCusBtn(self):
        self.driver.find_element_by_id("addCusBtn").click()

    #确定保存
    def confirm_save(self):
        self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[3]/button').click()

    #执行动作
    def do_add(self,driver,add_data):
        self.open_marketing_page(self.driver)
        self.add_button()
        self.select_area(add_data["cus.region_id"])
        self.select_department(add_data["cus.department_id"])
        self.input_tel(add_data["cus.tel"])
        self.input_name(add_data["cus.name"])
        self.select_sex(add_data["cus.sex"])
        self.select_status(add_data["cus.last_status"])
        self.input_wechat(add_data["cus.wechat"])
        self.input_qq(add_data["cus.qq"])
        self.input_school(add_data["cus.school"])
        self.select_education(add_data["cus.education"])
        self.input_major(add_data["cus.major"])
        self.select_workage(add_data["cus.workage"])
        self.input_age(add_data["cus.age"])
        self.select_source(add_data["cus.source"])
        self.input_eduxep(add_data["cus.eduexp"])
        self.input_experience(add_data["cus.experience"])
        self.input_last_tracking_remark(add_data["cus.last_tracking_remark"])
        self.addCusBtn()
        self.confirm_save()

if __name__ == '__main__':
    pass
    # from selenium import webdriver
    # driver = webdriver.Firefox()
    # nt=Marketing(driver)
    # nt.do_add('..\\conf\\yun\\testinfo.conf')
# cus.customer_id=&
# cusIsExist=&
# cus.region_id=1
# cus.department_id=2&
# cus.tel=&
# cus.name=
# cus.sex=%E5%A5%B3&
# cus.last_status=01&
# cus.wechat=0&
# cus.qq=23121324&
# cus.school=&
# cus.education=01&cus.major=&
# cus.workage=03&cus.age=&cus.source=21&cus.eduexp=&cus.experience=&
# cus.last_tracking_remark=
