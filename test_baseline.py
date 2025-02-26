# @Time : 2025/2/9 14:40
# @Author : luoxin
import random

import pytest
import allure


# 使用 allure 进行标签注解
@allure.feature("登录模块")
@allure.story("用户名和密码登录")
@pytest.mark.api  # 使用mark进行标记分类
@pytest.mark.ui  # 同一个用例可以进行多个标记
@pytest.mark.usefixtures("aaa")  # 使用定义好的fixture
# @pytest.mark.skip(reason='无理由跳过') # 跳过用例不执行
def test_login():
    username = "testuser"
    password = "testpassword"
    assert username == "testuser"
    assert password == "testpassword"


@pytest.mark.api
@pytest.mark.ut
@pytest.mark.usefixtures("aaa")  # 此种使用夹具的方法无法将夹具的返回值直接给测试用例使用，适用于：启动和停止某个服务、清理环境
def test_1():
    assert 1 == 1


def test_2(ccc):  # 此种使用夹具的方法可将夹具的返回值直接给测试用例使用
    assert 1 == 1

# 执行重试3次，每个延迟2s
@pytest.mark.flaky(retries=3,delay=2)
def test_3():
    assert random.choice([True, False])  # 随机生成失败或成功
