from selenium.webdriver.common.by import By
#启动应用的包名和启动名
sms_app_package ='com.android.mms'
sms_app_activity = '.ui.ConversationList'
#发送短信功能
sms_add_btn = (By.ID,'com.android.mms:id/action_compose_new')
#定位接收者
sms_reciver = (By.ID,'com.android.mms:id/recipients_editor')
#定位输入框
sms_input_edit = (By.ID,'com.android.mms:id/embedded_text_editor')
#发送按钮
sms_send_btn = (By.ID,"com.android.mms:id/send_button_sms")
#定位一组元素
sms_send_list = (By.ID,'com.android.mms:id/text_view')