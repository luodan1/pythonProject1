# -*- coding:utf-8 -*-
"""
作者: mi
日期: 2021年08月18日
"""
# 模块级别
def setup_module():
    print('setup module')
def teardown_module():
    print('teardown module')
class TestDemo:
    # 执行类 前后分别执行 setup_class teardown_class
    def setup_class(self):
        print('TestDemo setup_class')
    def teardown_class(self):
        print('TestDemo teardown_class')
    # 每个类里面的方法前后分别执行  setup，teardown
    def setup(self):
        print('TestDemo setup')
    def teardown(self):
        print('TestDemo teardown')
    def test_demo1(self):
        print('test demo1')
    def test_demo2(self):
        print('test demo2')

# class TestDemo1:
#     def test_demo3(self):
#         print('test demo3')