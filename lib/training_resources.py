# -*- encoding: utf-8 -*-
# File    : training_resources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/17 10:18   培训资源操作  add query  废弃
import time

from tools.service import Service


class TrainingResources:
    def __init__(self,driver):
        self.driver=driver
        #点击资源管理,点击培训资源
        self.driver.find_element_by_partial_link_text("资源管理").click()
        self.driver.find_element_by_partial_link_text("培训资源").click()



    #点击资源新增按钮
    def click_add_button(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/button[1]').click()
    #输入电话号码
    def input_tel(self,tel_value):
        tel=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[1]/div[1]/input')
        Service.send_input(tel,tel_value)
    #输入姓名
    def input_name(self,name_value):
        name=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/input[3]')
        # name = self.driver.find_element_by_css_selector('content > div.row.con-margin.con-body-header.queryDiv > div > input[type=text]:nth-child(6)')
        # content > div.row.con-margin.con-body-header.queryDiv > div > input[type=text]:nth-child(6)
        Service.send_input(name,name_value)
    #选择性别
    def select_sex(self,sex_value):
        sex_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[1]/div[3]/select')
        Service.select_text(sex_ele,sex_value)
    #选择状态
    def select_status(self,status_value):
        status_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[2]/div[1]/select')
        Service.select_text(status_ele,status_value)
    #输入微信
    def input_wechat(self,cus_wechat_value):
        wechat_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[2]/div[2]/input')
        Service.send_input(wechat_ele,cus_wechat_value)
    #输入QQ
    def input_cus_qq(self,cus_qq_value):
        cus_qq_ele = self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[2]/div[3]/input')
        Service.send_input(cus_qq_ele,cus_qq_value)
    #输入学校
    def input_school(self,cus_school_value):
        cus_school_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[3]/div[1]/input')
        Service.send_input(cus_school_ele,cus_school_value)
    #选择学历
    def select_education(self,education_value):
        cus_education_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[3]/div[2]/select')
        Service.select_text(cus_education_ele,education_value)
    #输入专业
    def input_major(self,cus_major_value):
        cus_major_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[3]/div[3]/input')
        Service.send_input(cus_major_ele,cus_major_value)
    #输入求职意向
    def input_intent(self,cus_intent_value):
        cus_intent_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[4]/div[1]/input')
        Service.send_input(cus_intent_ele,cus_intent_value)
    #选择工作年限
    def select_workage(self,workage_value):
        cus_workage_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[4]/div[2]/select')
        Service.select_text(cus_workage_ele,workage_value)
    #输入期望薪水
    def input_salary(self,cus_salary_value):
        cus_salary_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[4]/div[3]/input')
        Service.send_input(cus_salary_ele,cus_salary_value)
    #选择渠道
    def select_source(self,source_value):
        cus_source_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[5]/div[1]/select')
        Service.select_text(cus_source_ele,source_value)
    #输入邮箱
    def input_email(self,cus_email_value):
        cus_email_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[5]/div[2]/input')
        Service.send_input(cus_email_ele,cus_email_value)
    #输入年龄
    def input_age(self,cus_age_value):
        cus_age_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[5]/div[3]/input')
        Service.send_input(cus_age_ele,cus_age_value)
    #输入教育经历eduexp
    def input_eduexp(self,cus_eduexp_value):
        cus_eduexp_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[6]/div[1]/textarea')
        Service.send_input(cus_eduexp_ele,cus_eduexp_value)
        
    #输入工作经历experience
    def input_experience(self,cus_experience_value):
        cus_experience_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[6]/div[2]/textarea')
        Service.send_input(cus_experience_ele,cus_experience_value)

    #输入最后跟踪
    def input_last_tracking_remark(self,cus_last_tracking_remark_value):
        cus_last_tracking_remark_ele=self.driver.find_element_by_xpath('//*[@id="addCus"]/div[1]/div[7]/div/textarea')
        Service.send_input(cus_last_tracking_remark_ele,cus_last_tracking_remark_value)
    #点击保存
    def click_save_button(self):
        self.driver.find_element_by_id('addCusBtn').click()

    #接受保存成功弹窗
    def accept_success_alert(self):
        self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[3]/button').click()



    # #新增资源组合操作
    def do_add_resources(self,add_resources_info):
        self.click_add_button()
        self.input_tel(add_resources_info['cus.tel'])
        self.input_name(add_resources_info['cus.name'])
        self.select_sex(add_resources_info['cus.sex'])
        self.select_status(add_resources_info['cus.last_status'])
        self.input_wechat(add_resources_info['cus.wechat'])
        self.input_cus_qq(add_resources_info['cus.qq'])
        self.input_school(add_resources_info['cus.school'])
        self.select_education(add_resources_info['cus.education'])
        self.input_major(add_resources_info['cus.major'])
        self.input_intent(add_resources_info['cus.intent'])
        self.select_workage(add_resources_info['cus.workage'])
        self.input_salary(add_resources_info['cus.salary'])
        self.select_source(add_resources_info['cus.source'])
        self.input_email(add_resources_info['cus.email'])
        self.input_age(add_resources_info['cus.age'])
        self.input_eduexp(add_resources_info['cus.eduexp'])
        self.input_experience(add_resources_info['cus.experience'])
        self.input_last_tracking_remark(add_resources_info['cus.last_tracking_remark'])
        self.click_save_button()
        self.accept_success_alert()
        #刷新页面
        time.sleep(3)
        self.driver.refresh()

    #资源库选择
    def select_resource_library(self,resource_value):
        resource_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[1]')
        Service.select_text(resource_ele,resource_value)
    #搜索状态选择
    def query_status(self,status_value):
        status_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[2]')
        Service.select_text(status_ele,status_value)
    #搜索来源选择
    def query_source(self,source_value):
        source_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/select[3]')
        Service.select_text(source_ele,source_value)
    #开始时间
    def start_time(self,start_time_value):
        start_time_ele=self.driver.find_element_by_id('date1')
        Service.send_input(start_time_ele,start_time_value)
    #结束时间
    def end_time(self,end_time_value):
        end_time_ele = self.driver.find_element_by_id('date2')
        Service.send_input(end_time_ele,end_time_value)

    #输入姓名QQ或者电话
    def query_input_name(self,input_name_value):
        query_input_name_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/input[3]')
        Service.send_input(query_input_name_ele,input_name_value)
    #选择咨询师
    def select_consultant(self,consultant_value):
        consultant_ele=self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/select')
        Service.select_text(consultant_ele,consultant_value)
    #点击搜索
    def click_query(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/button').click()


    #执行搜索
    def do_query(self,query_resource_info):
        self.select_resource_library(query_resource_info['resource'])
        self.query_status(query_resource_info['status'])
        self.query_source(query_resource_info['source'])
        self.start_time(query_resource_info['start_time'])
        self.end_time(query_resource_info['end_time'])
        self.query_input_name(query_resource_info['query_name'])
        self.select_consultant(query_resource_info['consultant'])
        self.click_query()





if __name__ == '__main__':
    pass
    # driver=Service.get_driver()
    # driver.implicitly_wait(10)
    # Service.ignor_login_decrypt(driver)
    # ts=TrainingResources(driver)
    # s=Service.get_num(driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
    # print(s)
    # query_resource_info = {'resource': '临时池', 'status': '新入库', 'source': '全部',
    #                        'start_time': '', 'end_time': '', 'query_name': '',
    #                        "consultant": '全部'
    #                        }
    #
    # ts.do_query(query_resource_info)
    #
    #
    #
    # lis1t = Service.get_page_ele(driver,'//*[@id="personal-table"]/tbody/tr/td[2]')
    # print(lis1t)
    #



    # add_resources_info={"cus.tel":"19877101296","cus.name":"三生三世",
    # "cus.sex":"女","cus.last_status":"新入库","cus.wechat":"啊啊撒啥啥所",
    # "cus.qq":"阿萨斯搜索","cus.school":"啊啊啊啊","cus.education":"本科",
    # "cus.major":"啊啊啊啊","cus.intent":"啊啊啊啊","cus.workage":"2年","cus.salary":"啊啊啊啊啊","cus.source":"今日头条","cus.email":"啊啊啊啊啊","cus.age":"2年",
    # "cus.eduexp":"啊啊啊","cus.experience":"三生三世",
    # "cus.last_tracking_remark":"少时诵诗书所"}
    #
    # ts.do_add_resources(add_resources_info)
    #
