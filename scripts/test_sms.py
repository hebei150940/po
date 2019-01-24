import pytest
import time
from day06 import page
from day06.base.init_driver import get_driver
from day06.base.read_yaml_data import get_sms_data
from day06.page.sms_page import SmsPage

def get_data():
    data = get_sms_data('data.yaml')
    # {'smsdata': ['aaa', 'bbb', 'ccc']}
    return data.get('smsdata')

class TestSms:
    def setup_class(self):
        # 获取driver
        self.driver = get_driver(page.sms_app_package,page.sms_app_activity)
        #创建SmsPage对象
        self.sms_page = SmsPage(self.driver)
    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()
    def test_input_receiver(self):
        #1.实现点击新增短信按钮
        self.sms_page.click_sms_add_btn()
        #2.定位到接收者
        self.sms_page.input_reciver_content('10086')
    #实现发送短信
    @pytest.mark.parametrize("content",get_data() )
    def test_send_sms(self,content):
        #1.找到输入框,输入内容
        self.sms_page.input_content_edit(content)
        #2.找到发送按钮
        self.sms_page.sms_send_btn()
        #如何验证发送成功了呢
        sms_send_list = self.sms_page.get_sms_send_list()
        assert content in [i.text for i in sms_send_list]