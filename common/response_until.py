import logging

from jsonpath_ng import jsonpath, parse

class ResponseUntil:
    def __init__(self, response):
        # 假设response是Python字典
        self.response_json = response

    def extract(self, field):
        """ 使用 JSONPath 提取数据 """
        try:
            jsonpath_expr = parse(field)
            match = jsonpath_expr.find(self.response_json)  # 查找匹配的结果
            if match:
                return [m.value for m in match]
            else:
                raise KeyError(f"字段 {field} 不存在于响应中")
        except Exception as e:
            logging.error(f"提取数据 {field} 时发生错误: {e}")
            raise

    def check_filed(self, field:str,expected_value)->bool:
        """检查响应字段中的值是否匹配预期"""
        extracted_values = self.extract(field)
        if extracted_values and extracted_values[0] == expected_value:
            return True
        else:
            logging.error(f"字段 {field} 的值 {extracted_values} 与预期 {expected_value} 不匹配")
            return False


if __name__ == '__main__':
    response_json = {
        "page": 2,
        "data": [
            {"id": 7, "email": "michael.lawson@reqres.in"},
            {"id": 8, "email": "lindsay.ferguson@reqres.in"}
        ]
    }

    res = ResponseUntil(response_json)

    # 提取单个字段
    page = res.extract("page")
    print(page)  # 输出: [2]

    # 提取 data 中的 id
    ids = res.extract("$.data[*].id")
    print(ids)  # 输出: [7, 8]
