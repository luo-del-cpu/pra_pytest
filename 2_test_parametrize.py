# @Time : 2025/2/10 19:14
# @Author : luoxin
import pytest


"""
@pytest.mark.parametrize(args_name,args_value)

    1:args_name:参数名称，用于将参数值传递给哈数
    2:args_value:参数值(列表和字典列表，元组和字典元组)，有N个值就执行n次
"""
class Test:
    # 单参数用法
    @pytest.mark.parametrize('caseinfo_01',['c1','c2','c3'])
    def test_01(self,caseinfo_01):
        print("Test_01"+"+"+caseinfo_01) # 执行三次，将c1，c2，c3分别传入

    @pytest.mark.parametrize('caseinfo_02',('c1','c2','c3'))
    def test_02(self,caseinfo_02):
        print("Test_02"+"+"+caseinfo_02) # 执行三次，将c1，c2，c3分别传入

    @pytest.mark.parametrize('caseinfo_03',[{"a":"01"},{"b":"02"},{"c":"03"}])
    def test_03(self,caseinfo_03):
        print("Test_03"+"+"+str(caseinfo_03)) # 执行三次，将三个字典整体分别传入

    # 拆包用法
    @pytest.mark.parametrize("input, expected", [
    (1, 2),
    (3, 4),
    (5, 6)
])
    def test_04(self, input, expected):
        assert input + 1 == expected # 执行三次，将value中的值进行拆包分别赋值给input与excepted