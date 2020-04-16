# coding=utf-8
"""Tests the solution."""
import anarc05b_double_helix as db


def test_double_helix() -> None:
    """Function to test the double helix solution using py.test."""
    in_lists = (
        (
            "13 3 5 7 9 20 25 30 40 55 56 57 60 62",
            "11 1 4 7 11 14 25 44 47 55 57 100",
            450,
        ),
        ("4 -5 100 1000 1005", "3 -12 1000 1001", 2100),
    )

    lists = []
    for iter_list in in_lists:
        temp = []
        temp[0] = list(map(int, iter_list[0].split()))
        temp[1] = list(map(int, iter_list[1].split()))
        temp[2] = iter_list[2]
        lists.append(temp)

    for element in lists:
        assert db.DoubleHelix(element[0], element[1]) == element[2]
