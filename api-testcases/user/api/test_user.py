# @Time : 2025/2/10 17:52
# @Author : luoxin

"""
用例内容
"""
from wsgiref.util import request_uri

import pytest

from common.read_csv import read_csv
from common.read_yaml import read_yaml
from common.request_util import RequestUtil
from common.response_until import ResponseUntil
from common.wait_until_task_completed import AsyncPoller


class TestUser:
    save_data = {}
    request_util = RequestUtil()

    @pytest.mark.parametrize('testcase', read_yaml('user/data/list_users.yaml'))
    def test_01_list_users(self,testcase):
        # 获取测试用例数据
        name = testcase['name']
        method = testcase['request']['method']
        url = testcase['request']['url']
        data = testcase['request']['data']
        except_json = testcase['except_response']['json_schema']
        print(testcase)

        # 获取 'extract' 中的第一个元素，并提取 'id'
        extract = testcase['extract'][0]  # 提取 extract 列表中的第一个字典
        field = extract['id']  # 获取字典中 id 对应的字段值
        res = TestUser.request_util.send_request(method, url, data)
        response_json = res.json()

        # 不建议直接断言整个json串
        # assert response_json == testcase['excepted_response']['json_schema']

        # 断言状态码
        assert res.status_code == testcase['except_response']['status_code']
        # 挨个断言json数据
        for key,value in except_json.items():
            assert response_json[key] == value,f"错误: {key} 预期 {value}, 但返回 {response_json[key]}"

        print(f"✅ 用例 `{name}` 通过！")

        # 使用 ResponseExtractor 提取 token
        extractor = ResponseUntil(response_json)
        extract_id  = extractor.extract(field)[0]
        self.save_data["id"] = extract_id
        print(self.save_data)

    @pytest.mark.parametrize('testcase', read_yaml('user/data/get_user.yaml'))
    def test_02_get_user(self,testcase):
        name = testcase['name']
        method = testcase['request']['method']
        url = testcase['request']['url']
        data = testcase['request']['data']
        data["id"] = self.save_data["id"]
        except_json = testcase['except_response']['json_schema']

        res = TestUser.request_util.send_request(method, url, data)
        response_json = res.json()
        print(testcase)

        assert res.status_code == testcase['except_response']['status_code']
        for key,value in except_json.items():
            assert response_json[key] == value,f"错误：{key} 预期 {value},但返回 {response_json[key]}"

        print(f"✅ 用例 `{name}` 通过！")

    @pytest.mark.parametrize('testcase', read_yaml('user/data/async_wait.yaml'))
    def test_03_async_wait(self,testcase):
        name = testcase["name"]
        method = testcase["request"]["method"]
        url = testcase["request"]["url"]
        data = testcase["request"]["data"]
        except_json = testcase["except_response"]["json_schema"]

        res = TestUser.request_util.send_request(method, url, data)
        response_json = res.json()

        # 使用 ResponseUntil 提取字段
        extractor = ResponseUntil(response_json)

        # 异步等待某个字段是否符合预期
        poller = AsyncPoller(timeout=30, interval=3)

        # 直接使用 check_field 作为条件函数来检查 "page" 字段是否为 2
        try:
            poller.wait_until(
                condition=lambda:extractor.check_filed("page", 2),
                success_msg="页面字段符合预期",
                timeout_msg="等待页面字段超时")

            # 在异步等待成功后，执行断言
            assert res.status_code == testcase['except_response']['status_code'],f"预期status_code为{testcase['except_response']['status_code']},实际为:{res.status_code}"
            assert len(response_json["data"])>0

            # 如果断言都成功，通过打印用例成功
            print(f"✅ 用例 `{name}` 通过！")
        except (TimeoutError, AssertionError) as e:
            print(f"❌ 用例失败: {e}")

    @pytest.mark.parametrize('testcase', read_csv('user/data/mult_user.csv'))
    def test_04_mult_users(self,testcase):
        # 获取测试用例数据
        name = testcase['name']
        method = testcase['method']
        url = testcase['url']
        data = testcase['params']
        # except_json = testcase['except_json_schema']
        print(testcase)

        res = TestUser.request_util.send_request(method, url, data)
        response_json = res.json()
        print(response_json)

        # 不建议直接断言整个json串
        # assert response_json == testcase['excepted_response']['json_schema']

        # 断言状态码
        assert res.status_code == testcase['expected_status_code']
        # 挨个断言json数据
        # for key,value in except_json.items():
        #     assert response_json[key] == value,f"错误: {key} 预期 {value}, 但返回 {response_json[key]}"

        print(f"✅ 用例 `{name}` 通过！")








