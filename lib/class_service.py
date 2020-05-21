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
    def area_query(self,region):
        # select_area=self.driver.find_element_by_css_selector('select.sel-text:nth-child(1)').click()
        select_area = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[1]/div[1]/select[1]')
        Service.select_text(select_area,region)
    #状态查询
    def status_query(self, status):
        select_status = self.driver.find_element_by_css_selector('.col-lg-12 > select:nth-child(2)').click()
        Service.select_text(select_status,status)

    #新增
    def button_add(self):
        self.driver.find_element_by_xpath("//*[@id='cmDiv']/div[1]/button").click()

    #班名
    def input_classname(self,class_no):
        classname = self.driver.find_element_by_xpath('''//*[@id="addClass-form"]/div/div[1]/input''')
        Service.send_input(classname,class_no)
    #方向
    def direction(self,orientation):
        direction=self.driver.find_element_by_xpath('//*[@id="addClass-form"]/div/div[2]/select')
        Service.select_text(direction,orientation)
    #时间
    def selec_time(self,opening_time):
        Service.input_time(self.driver,"document.querySelector('#addClass-form > div > div:nth-child(3) > input')",opening_time)
    #班主任
    def selec_teacher(self,class_headmaster_id):
        teacher=self.driver.find_element_by_xpath('//*[@id="addClass-form"]/div/div[4]/select')
        Service.select_text(teacher,class_headmaster_id)
    def confirm_save(self):
        self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button').click()

    # c.class_no = WNCDC22 & c.orientation = % E6 % B5 % 8
    # B % E8 % AF % 95 & c.opening_time = 2020 - 05 - 20 & c.class_headmaster_id = 6
    #pageSize = 10 & pageIndex = 1 & regionId = & openStatus = 02
    #执行查询动作
    def do_query(self,query_data):
        self.class_management()
        self.area_query(query_data['regionId'])
        self.status_query(query_data['status'])
    #执行添加班级动作
    def do_add(self,add_data):
        self.class_management()
        self.button_add()
        self.input_classname(add_data["c.class_no"])
        self.direction(add_data["c.orientation"])
        self.selec_time(add_data["c.opening_time"])
        self.selec_teacher(add_data['c.class_headmaster_id'])
 #打开学员考勤
    def checking_in(self,driver):
        Service.open_menu(self.driver, '班务管理')
        Service.open_menu(self.driver, '学员考勤')
    #姓名搜索
    def student_name(self,stuName):
        student_name=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/input')
        Service.send_input(student_name,stuName)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/button[1]').click()
    #考勤选项
    def sele_attendance(self,attendance):
        sele_attendance=self.driver.find_element_by_xpath('//*[@id="stu-table"]/tbody/tr[1]/td[8]/select')
        Service.select_text(sele_attendance,attendance)
    #点击考勤按钮
    def confirmAttenBtn(self):
        self.driver.find_element_by_xpath('//*[@id="confirmAttenBtn_3553"]').click()
    #执行考勤动作
    def do_confirm(self,driver,confirm_data):
        self.checking_in(driver)
        self.student_name(confirm_data['stuName'])
        self.sele_attendance(confirm_data['attendance'])
        self.confirmAttenBtn()

    # 打开学员请假
    def leave(self, driver):
        Service.open_menu(self.driver, '班务管理')
        Service.open_menu(self.driver, '学员请假')
    #区域
    def quyu(self,region_id):
        quyu=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/select[1]')
        Service.select_text(quyu,region_id)
    #请假状态
    def status(self,leave_status):
        status=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/select[2]')
        Service.select_text(status,leave_status)
    #点击查询按钮
    def query(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/button').click()
    #点击修改按钮
    def button_change(self):
        self.driver.find_element_by_xpath('//*[@id="leave-table"]/tbody/tr[1]/td[12]/button[3]').click()
    #修改请假条内容
    def ch_star_time(self,startime):
        Service.input_time(self.driver,'//*[@id="modLeave-form"]/div[1]/div[1]/input',startime)
    #修改结束时间
    def ch_end_time(self,endtime):
        Service.input_time(self.driver,'//*[@id="modLeave-form"]/div[1]/div[2]/input',endtime)
    #请假类型
    def ch_type(self,leave_type):
        type=self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[2]/div[1]/select')
        Service.select_text(type,leave_type)
    #请假天数
    def ch_day(self,days):
        day=self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[2]/div[2]/input')
        Service.send_input(day,days)
    #修改姓名
    def ch_name(self,stuName):
        name=self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[3]/div[1]/input')
        Service.send_input(name,stuName)
    #修改是否扣分
    def ch_cont(self,leave_cont):
        cont=self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[3]/div[2]/select')
        Service.select_text(cont,leave_cont)
    #请假原因
    def ch_reson(self,reason):
        reson=self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[4]/div/textarea')
        Service.send_input(reson,reason)
    #修改处理意见
    def ch_opinion(self,comment):
        opinion=self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[5]/div/textarea')
        Service.send_input(opinion,comment)
    def ch_save(self):
        self.driver.find_element_by_xpath('//*[@id="modLeave-modal"]/div/div/div[3]/button').click()
    #销假
    def quxiao(self):
        self.driver.find_element_by_xpath('//*[@id="leave-table"]/tbody/tr[1]/td[12]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[16]/div/div/div[3]/button[2]').click()
    #新增
    def add_leave(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/div/button').click()
    def add_startime(self,startime):
        Service.input_time(self.driver,'//*[@id="leave-form"]/div[1]/div[1]/input',startime)
    def add_endtime(self,endtime):
        Service.input_time(self.driver,'//*[@id="leave-form"]/div[1]/div[2]/input',endtime)
    def add_type(self,type):
        add_type=self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[2]/div[1]/select')
        Service.select_text(add_type,type)
    def add_day(self,days):
        add_day=self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[2]/div[2]/input')
        Service.send_input(add_day,days)
    def add_name(self,stuName):
        add_name=self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[3]/div/input')
        Service.send_input(add_name,stuName)
    def add_count(self,leave_count):
        add_count=self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[3]/select')
        Service.select_text(add_count,leave_count)
    def add_reason(self,reason):
        add_reason=self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[4]/div/textarea')
        Service.send_input(add_reason,reason)
    def add_comment(self,comment):
        add_comment=self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[5]/div/textarea')
        Service.send_input(add_comment,comment)
    def add_save(self):
        self.driver.find_element_by_xpath('//*[@id="leave-modal"]/div/div/div[3]/button').click()
    #执行请假查询动作
    def do_leave_query(self,driver,leave_query_data):
        self.leave(driver)
        self.quyu(leave_query_data['region_id'])
        self.status(leave_query_data['leave_status'])
        self.query()
    #执行修改动作
    def change_leave(self,driver,change_data):
        self.leave(driver)
        self.button_change()
        self.ch_star_time(change_data['sl.start_time'])
        self.ch_end_time(change_data['sl.end_time'])
        self.ch_type(change_data['sl.leave_type'])
        self.ch_day(change_data['sl.days'])
        self.ch_name(change_data['sl.stuName'])
        self.ch_cont(change_data['sl.leave_count'])
        self.ch_reson(change_data['sl.reason'])
        self.ch_opinion(change_data['sl.comment'])
        self.ch_save()
    #执行新增动作
    def do_add_leave(self,driver,add_leave_data):
        self.leave(driver)
        self.add_leave()
        self.add_startime(add_leave_data['sl.start_time'])
        self.add_endtime(add_leave_data['sl.end_time'])
        self.add_type(add_leave_data['sl.leave_type'])
        self.add_day(add_leave_data['sl.days'])
        self.add_name(add_leave_data['sl.stuName'])
        self.add_count(add_leave_data['sl.leave_count'])
        self.add_reason(add_leave_data['sl.reason'])
        self.add_comment(add_leave_data['sl.comment'])
        self.add_save()

    #学员转班
    def change_class(self,driver):
        Service.open_menu(self.driver, '班务管理')
        Service.open_menu(self.driver, '学员转班')
    #点击转班按钮stuId=3556&stuClass=WNCDC99&regionId=1
    def change_class_but(self):
        self.driver.find_element_by_xpath('//*[@id="stuInfo_table"]/tbody/tr[1]/td[12]/button').click()
    def changeRegion(self,regionId):
        changeRegion=self.driver.find_element_by_xpath('//*[@id="changeClass-modal"]/div/div/div[2]/div[1]/select')
        Service.select_text(changeRegion,regionId)
    def change_classno(self,stuClass):
        change_Class=self.driver.find_element_by_xpath('//*[@id="changeClass-modal"]/div/div/div[2]/div[2]/select')
        Service.select_text(change_Class,stuClass)
    def change_save(self):
        self.driver.find_element_by_xpath('//*[@id="changeClass-modal"]/div/div/div[3]/button').click()
    def save_save(self):
        self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button[2]').click()
    def ok(self):
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button').click()
    def do_change_class(self,driver,change_class_data):
        self.change_class(driver)
        self.change_class_but()
        self.changeRegion(change_class_data['regionId'])
        self.change_classno(change_class_data['stuClass'])
        self.change_save()
        self.save_save()
        self.ok()
if __name__ == '__main__':
    pass