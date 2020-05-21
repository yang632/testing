# -*- encoding: utf-8 -*-
# File    : utility
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 16:12

class Utility:
    #读取json文件的信息
    @classmethod
    def get_json(cls, path):
        import json
        with open(path,encoding='utf8') as file:
            contents = json.load(file)
        return contents


    #获取测试数据
    @classmethod
    def get_testinfo(cls,conf):
        import xlrd
        workbook=xlrd.open_workbook(conf["TESTINFO_PATH"])
        contents=workbook.sheet_by_name(conf["SHEETNAME"])
        # print(contents)
        testinfo = []
        for i in range(conf['START_ROW'], conf['END_ROW']):
            testdata=contents.cell(i,conf["TESTDATA_COL"]).value
            expect=contents.cell(i,conf['EXPECT_COL']).value
            tup={}
            temp=testdata.split('\n')
            for one in temp:
                # print(one)
                tup[one.split('=')[0]]=one.split('=')[1]
            tup['expext']=expect
            testinfo.append(tup)
        return testinfo

    @classmethod
    def tran_tuple(cls,conf):
        contents=Utility.get_testinfo(conf)
        # print(contents)
        list=[]
        for content in contents:
            tup=tuple(content.values())
            list.append(tup)
        return list
    # 获取当前的时间
    @classmethod
    def ctime(cls):
        import time
        return time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())

    # 创建数据库连接
    @classmethod
    def getConn(cls,path):
        import pymysql
        contents = cls.get_json(path)
        return pymysql.connect(contents['HOSTNAME'],
                               contents['DBUSER'], contents['DBPASS'],
                               contents['DBNAME'], charset='utf8')
    # 查询一条记录
    @classmethod
    def query_one(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchone()
        except Exception as e:
            result = None
        finally:
            cur.close()
            conn.close()
        return result

    # 查询多条记录
    @classmethod
    def query_all(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            result = None
        finally:
            cur.close()
            conn.close()
        return result


    #读取文本文件
    @classmethod
    def get_str(cls,path):
        list=[]
        with open(path,"r") as file:
            contents=file.readlines()
            for content in contents:
                content=content.strip()
                if not content.startswith("#"):
                    list.append(content)
        return list




    #输入日期
    @classmethod
    def input_date(cls, driver, id, date):
        ele = driver.find_element_by_id(id)
        driver.execute_script('document.getElementById("%s").readOnly=false;' % (id))
        ele.send_keys(date)

    # 截图操作
    @classmethod
    def get_png(cls, driver, path):
        import time
        time.sleep(2)
        driver.get_screenshot_as_file(path)

    # 出现缺陷或错误后的截图方法
    # '2020-03-23_15-17-30'
    @classmethod
    def get_error_png(cls, driver):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        screenshot_path = '..\\screenshot\\fail%s.png' % (ctime)
        cls.get_png(driver, screenshot_path)

    #生成1-10的随机数随机数
    @classmethod
    def get_random_num(cls,start,end):
        import random
        return random.randint(start, end)




if __name__ == '__main__':
    pass
    s=Utility.get_str("../conf/peng/test.conf")
    print(s)
    # t=Utility.get_testinfo(s[0])
    # print(t)
