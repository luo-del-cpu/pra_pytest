import time
from typing import Callable, AnyStr, Any

import allure


class AsyncPoller:
    def __init__(self,timeout:int = 30,interval:int = 3):
        self.timeout = timeout
        self.interval = interval

    def wait_until(
            self,
            condition:Callable[[],bool],
            success_msg:str="条件满足",
            timeout_msg:str="等待超时"
    ) -> bool:

         """
         通用异步等待方法
         :param condition:条件判断函数 返回bool
         :param success_msg: 成功时的日志信息
         :param timeout_msg: 超时时的日志信息
         """

         end_time = time.time() + self.timeout
         attempt = 0
         while time.time() < end_time:
             attempt += 1
             with allure.step(f"第 {attempt} 次检查条件"):
                if condition():
                    allure.attach(success_msg,name="成功信息")
                    return True
                time.sleep(self.interval)
         raise TimeoutError(timeout_msg)
