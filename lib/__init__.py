# -*- encoding: utf-8 -*-
# File    : __init__.py
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/16 15:50

class Test:
    from selenium import webdriver
    # driver=webdriver.Firefox()
    # driver.find_element_by_css_selector()
    # driver.implicitly_wait()
    driver=webdriver.Chrome()
    driver.find_element()
    driver.f