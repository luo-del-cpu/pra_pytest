import os

import pytest
import logging.config

"""
根目录全局配置文件  
"""


"""
conftest.py文件：
    1：用于存放全局共享的夹具 fixture
    2：用于存放钩子 hook
"""

"""
什么时候使用:
    测试环境初始化：在测试开始之前初始化必要的环境，创建数据库连接、启动 Web 服务等。
    共享数据：当多个测试用例需要相同的初始化数据或资源时，可以使用 fixture 来避免重复的代码。
    清理资源：在测试完成后，执行清理任务，例如关闭文件、删除临时文件、断开数据库连接等。
    模拟与替换：使用 fixture 可以替换掉难以控制的外部依赖，比如模拟数据库操作、HTTP 请求、外部 API 等。
"""

# fixture就是在函数前置与后置的操作，用生成器的原理
"""
@pytest.fixture(scope="",autouse=True) 作用域参数，常见的有：

    "function"：默认值，表示每个测试函数都会调用该 fixture。
    "class"：表示每个测试类调用一次该 fixture。
    "module"：表示在一个模块（文件）内所有测试函数调用一次该 fixture。
    "session"：表示在 pytest 会话的整个生命周期内只调用一次该 fixture。
    autouse=True：让 fixture 在其 scope 范围内的所有测试中 自动生效，无需显式引用(测试用例中声明)，此参数默认为False。

    优先级:
        session的优先级最高；最先执行 session>Module>Class>Function
        类级别的fixture的class的fixture级别高；函数级别的fixture的class的fixture级别高
"""
@pytest.fixture(scope="module")
def aaa():
    print("夹具1前置")
    yield
    print("夹具1后置")

@pytest.fixture(scope="module")
def bbb():
    print("夹具2前置")
    yield
    print("夹具2后置")

def read_yaml():
    return ["cs1","cs2","cs3"]
"""
@pytest.fixture(scope="function",params=read_yaml()) 
    1：设置 params 参数来实现 参数化,必须是列表类型
    2：夹具函数必须使用request来接收params参数
    3：fixture params 更偏向“资源或环境的多种配置场景测试”。
"""
@pytest.fixture(scope="function",params=read_yaml())
def ccc(request):
    """
    使用 params 参数来测试多种数据。
    request.param 表示当前测试使用的数据（"cs1","cs2","cs3"）。
    """
    print("夹具1前置")
    yield request.param
    print("夹具1后置")

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """在 pytest 运行前加载日志配置"""
    config_path = os.path.abspath("log.ini")
    if os.path.exists(config_path):
        logging.config.fileConfig(config_path)
    else:
        print(f"Logging configuration file not found: {config_path}")

# def pytest_configure(config):
#     env_value = config.getini('env')  # 获取 pytest.ini 中的 'env' 配置
#     print(f"Configured environment: {env_value}")

