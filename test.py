#!/usr/bin/python3
import os
import unittest
from anarc05b_double_helix import DoubleHelix as DH
from anarc05b_double_helix_greedy import DHG

testip = os.path.join(os.path.dirname(__file__), 'input.dat')
testop = os.path.join(os.path.dirname(__file__), 'output.dat')

class Test(unittest.TestCase):

    def setUp(self):
        self.input = open(testip)
        self.ipdata = self.input.readlines()
        self.output = open(testop)
        self.opdata = self.output.readlines()

    def tearDown(self):
        self.input.close()
        self.output.close()

    def test_dp(self):
        i = 0
        while i < len(self.ipdata):
            arr1 = list(map(int, self.ipdata[i].split()))
            arr2 = list(map(int, self.ipdata[i+1].split()))
            op = int(self.opdata[i//2])
            dh = DH(arr1, arr2)
            result = dh.solve()
            self.assertEqual(result, op)
            i+=2

    def test_greedy(self):
        i = 0
        while i < len(self.ipdata):
            arr1 = list(map(int, self.ipdata[i].split()))
            arr2 = list(map(int, self.ipdata[i+1].split()))
            op = int(self.opdata[i//2])
            dhg = DHG(arr1, arr2)
            result = dhg.solve()
            self.assertEqual(result, op)
            i+=2

if __name__ == '__main__':
    unittest.main()
