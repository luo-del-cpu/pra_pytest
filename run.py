# @Time : 2025/2/10 14:17
# @Author : luoxin
import os
import time

import pytest

if __name__ == "__main__":
    # 用于本地调试
    # pytest.main()
    # time.sleep(3)
    # os.system("allure generate ./allure-results -o ./reports --clean")

    # 用于集成jenkins
    pytest.main(["--alluredir=./allure-results"])  # 仅生成原始数据，不调用 allure generate