# @Time : 2025/2/11 14:22
# @Author : luoxin
import csv
import json
import os
from pathlib import Path
import yaml

def get_obj_path():
    # 获取项目根目录，使用当前文件取找绝对路径不容易出问题
    source_dir = Path(__file__).resolve().parent.parent / "api-testcases"
    return source_dir


def read_csv(csvpath):
    # 读取yaml文件内容
    file_path = get_obj_path()/csvpath
    with open(file_path, 'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    # 处理得到的数据
    for row in rows:
        # 将 params 字符串转换为字典
        if row.get('params'):
            row['params'] = json.loads(row['params'])  # 如果params是JSON格式的字符串
        # 将 expected_status_code 转换为整数
        if row.get('expected_status_code'):
            row['expected_status_code'] = int(row['expected_status_code'])
    #         # 如果有 json_schema，将其处理为字典
    #     if row.get('except_json_schema'):
    #         row['except_json_schema'] = json.loads(row['except_json_schema'])  # 如果是JSON字符串

    return rows

if __name__ == '__main__':
    get_obj_path()
    # print(read_yaml('user/user_data.yaml'))
    print(read_csv('/Users/luoxin/PycharmProjects/pra_pytest/api-testcases/user/data/mult_user.csv'))