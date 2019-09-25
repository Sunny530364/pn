#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI

import unittest
from base.method import Method
from base.method import *
from  page.lagou import *

class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsAssert()

    def statusCode(self,r):
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.status_code,200)

    def test_lagou_001(self):
        '''拉钩：测试翻页'''
        r=self.obj.post(1)
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=1,str2=r.text))
    def test_lagou_002(self):
        '''拉钩：测试性能自动化测试功能'''
        r=self.obj.post(1,data=setso(kd='性能自动化测试'))
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=1,str2=r.text))



if __name__=='__main__':
    if __name__ == '__main__':
        unittest.main(verbosity=2)
