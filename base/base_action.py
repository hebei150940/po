import time
class BaseAction:
    def __init__(self,driver):
        self.driver = driver
    #查找元素
    def find_element(self,tup):
        time.sleep(1)
        return self.driver.find_element(tup[0],tup[1])
    #查找一组元素
    def find_elements(self,tup):
        time.sleep(1)
        return self.driver.find_elements(tup[0],tup[1])
    #点击元素
    def click_element(self,tup):
        self.find_element(tup).click()
    #向输入框输入内容
    def input_edit_content(self,tup,content):
        input_content = self.find_element(tup)
        input_content.clear()
        input_content.send_keys(content)
