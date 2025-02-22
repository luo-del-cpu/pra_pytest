# @Time : 2025/2/11 14:22
# @Author : luoxin
import os
from pathlib import Path
import yaml

def get_obj_path():
    # 获取项目根目录，使用当前文件取找绝对路径不容易出问题
    source_dir = Path(__file__).resolve().parent.parent / "api-testcases"
    return source_dir


def read_yaml(yamlpath):
    # 读取yaml文件内容
    file_path = get_obj_path()/yamlpath
    with open(file_path, 'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data['testcases']

if __name__ == '__main__':
    get_obj_path()
    # print(read_yaml('user/user_data.yaml'))