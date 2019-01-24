import os
import yaml


def get_sms_data(file_name):
    with open('./data' + os.sep + file_name, 'r', encoding='utf-8') as f:
        return yaml.load(f)
