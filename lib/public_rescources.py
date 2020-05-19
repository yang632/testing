# -*- encoding: utf-8 -*-
# File    : public_rescources
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/19 11:43

class PublicRescources:

    def __init__(self,driver):

        self.driver=driver
        self.driver.find_element_by_partial_link_text('资源管理').click()
        self.driver.find_element_by_partial_link_text('公共资源').click()

    
