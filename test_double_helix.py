# coding=utf-8
"""Author - Khaveesh N IMT2018036. Tests the solution."""
import unittest

import anarc05b_double_helix as dbl
import anarc05b_double_helix_greedy as grdy


class Test(unittest.TestCase):
    """Unittest requires a class of TestCase to run."""

    def setUp(self) -> None:
        """Testcase class is setup to run tests."""
        with open("./test/correct_tests.txt") as file_correct:
            # Read all the lines from file, removing empty lines and \n's
            raw_inp = filter(None, file_correct.read().splitlines())
            # Split string of integers into list of ints
            inp = [list(map(int, string.split())) for string in raw_inp]
            # Encapsulate the first, second and soln for each testcase in a separate tuple
            self.right_testcases = [
                (iter_list[0], iter_list[1], iter_list[2][0])
                for iter_list in zip(inp[::3], inp[1::3], inp[2::3])
            ]

        with open("./test/wrong_tests.txt") as file_wrong:
            # Read all the lines from file, removing empty lines and \n's
            raw_inp = filter(None, file_wrong.read().splitlines())
            # Split string of integers into list of ints
            inp = [list(map(int, string.split())) for string in raw_inp]
            # Encapsulate the first, second and soln for each testcase in a separate tuple
            self.wrong_testcases = [
                (iter_list[0], iter_list[1], iter_list[2][0])
                for iter_list in zip(inp[::3], inp[1::3], inp[2::3])
            ]

    def test_double_helix(self) -> None:
        """Function to test the dynamic programming solution using unittest framework."""
        for testcase in self.right_testcases:
            with self.subTest(testcase):
                self.assertEqual(
                    dbl.DoubleHelix(testcase[0], testcase[1]).solve(), testcase[2],
                )

        for testcase in self.wrong_testcases:
            with self.subTest(testcase):
                self.assertNotEqual(
                    dbl.DoubleHelix(testcase[0], testcase[1]).solve(), testcase[2],
                )

    def test_double_helix_greedy(self) -> None:
        """Function to test the greedy solution using unittest framework."""
        for testcase in self.right_testcases:
            with self.subTest(testcase):
                self.assertEqual(
                    grdy.DHG(testcase[0], testcase[1]).solve(), testcase[2],
                )

        for testcase in self.wrong_testcases:
            with self.subTest(testcase):
                self.assertNotEqual(
                    grdy.DHG(testcase[0], testcase[1]).solve(), testcase[2],
                )


if __name__ == "__main__":
    unittest.main()
