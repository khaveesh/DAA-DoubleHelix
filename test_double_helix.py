# coding=utf-8
"""Tests the solution."""
import unittest

import anarc05b_double_helix as dp
import anarc05b_double_helix_greedy as grdy


class Test(unittest.TestCase):
    """Unittest requires a class of TestCase to run."""

    def setUp(self) -> None:
        """Testcase class is setup to run tests."""
        with open("testcases.txt") as file_desc:
            raw_inp = filter(None, file_desc.read().splitlines())
            inp = [map(int, string.split()) for string in raw_inp]
            self.testcases = (
                (iter_list[0], iter_list[1], tuple(iter_list[2])[0])
                for iter_list in zip(inp[::3], inp[1::3], inp[2::3])
            )

    def test_double_helix_dp(self) -> None:
        """Function to test the dynamic programming solution using unittest framework."""
        for testcase in self.testcases:
            with self.subTest(testcase):
                self.assertEqual(
                    dp.DoubleHelix(testcase[0], testcase[1]).solve(), testcase[2],
                )

    def test_double_helix_greedy(self) -> None:
        """Function to test the greedy solution using unittest framework."""
        for testcase in self.testcases:
            with self.subTest(testcase):
                self.assertEqual(
                    grdy.DHG(testcase[0], testcase[1]).solve(), testcase[2],
                )


if __name__ == "__main__":
    unittest.main()
