#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from time import strftime, localtime

now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
chrome_options = webdriver.ChromeOptions()
# 设置为手机模式
mobile_emulation = {"deviceName": "iPhone X"}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
# 如果不加这个选项，有时定位会出现问题
chrome_options.add_argument('--disable-gpu')


def get_details():
    f_print('************************************ refresh ************************************')
    browser.get('https://h5.m.taobao.com/awp/core/detail.htm?id=577115972182')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="sys_list$sys_list_10014"]/div[7]').click()
    time.sleep(0.2)

    col_path = '//*[@id="detail"]/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/ul/'
    cat_path = '//*[@id="detail"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/ul/'
    mem_path = '//*[@id="detail"]/div[3]/div[2]/div[2]/div/div/div[2]/div[3]/ul/'
    ver_path = '//*[@id="detail"]/div[3]/div[2]/div[2]/div/div/div[2]/div[4]/ul/'
    col_len = len(browser.find_elements_by_xpath(col_path + '*'))
    cat_len = len(browser.find_elements_by_xpath(cat_path + '*'))
    mem_len = len(browser.find_elements_by_xpath(mem_path + '*'))
    ver_len = len(browser.find_elements_by_xpath(ver_path + '*'))

    browser.find_element_by_xpath(cat_path + 'li[1]').click()
    browser.find_element_by_xpath(ver_path + 'li[1]').click()

    # 机身颜色
    for i in range(1, col_len + 1):
        browser.find_element_by_xpath(col_path + 'li[' + str(i) + ']').click()
        time.sleep(0.2)
        # 套餐类型
        for j in range(1, cat_len + 1):
            # browser.find_element_by_xpath(cat_path + 'li[' + str(j) + ']').click()
            # time.sleep(0.2)
            # 存储容量
            for k in range(1, mem_len + 1):
                browser.find_element_by_xpath(mem_path + 'li[' + str(k) + ']').click()
                time.sleep(0.2)
                # 版本类型
                for m in range(1, ver_len + 1):
                    # browser.find_element_by_xpath(ver_path + 'li[' + str(m) + ']').click()
                    # time.sleep(0.2)
                    f_print(strftime('%Y-%m-%d %H:%M:%S  ', localtime())
                          + browser.find_element_by_xpath(
                        '//*[@id="detail"]/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/p[1]').text
                          + '  ' + browser.find_element_by_xpath(
                        '//*[@id="detail"]/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/p[3]/span[1]').text)

    f_print('********************************** refresh end **********************************')


def f_print(st):
    file.write(st + '\n')


if __name__ == '__main__':
    # 新建记录文件
    if not os.path.exists('log'):
        os.makedirs('log')

    file = open('log/' + now_time + '.txt', 'w', encoding='utf-8')
    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(options=chrome_options)

    try:
        get_details()
    finally:
        file.close()
        browser.quit()
