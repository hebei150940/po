import time

import yaml

from day06 import page
from day06.base.base_action import BaseAction


class SmsPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #点击新增
    def click_sms_add_btn(self):
        self.find_element(page.sms_add_btn).click()
    #定位接收者
    def input_reciver_content(self,num):
        time.sleep(1)
        self.find_element(page.sms_reciver).send_keys(num)
    #定位输入框
    def input_content_edit(self,content):
        time.sleep(1)
        self.find_element(page.sms_input_edit).send_keys(content)
    #点击发送
    def sms_send_btn(self):
        self.find_element(page.sms_send_btn).click()
    #验证是否成功
    def get_sms_send_list(self):
        return self.find_elements(page.sms_send_list)
