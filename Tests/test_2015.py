"""Test runner for 2015 Advent of Code solutions."""

from dataclasses import dataclass
import unittest
import os

from AoC2015.day1 import Day1
from AoC2015.day8 import Day8
from Utilities.aoc_day import AdventOfCodeDay


@dataclass
class TestData:
    """Class to hold test data for each day's solution."""

    day_name: str
    day_class: AdventOfCodeDay
    p1: int
    p2: int


class Test2015(unittest.TestCase):
    """Test runner for 2015 Advent of Code solutions."""

    inputs_dir = os.path.join(os.getcwd(), "Tests", "inputs", "2015")

    test_suite = [
        TestData("Day 1", Day1(os.path.join(inputs_dir, "day1.txt")), 232, 1783),
        TestData("Day 8", Day8(os.path.join(inputs_dir, "day8.txt")), 1350, 2085),
    ]

    def test_part_1(self):
        """Test part 1 solutions."""
        for test in self.test_suite:
            with self.subTest(test=test, msg=test.day_name):
                if test.p1 is not None:
                    self.assertEqual(test.day_class.part1(), test.p1)
                else:
                    print("Part 1 answer is: ", test.day_class.part1())

    def test_part_2(self):
        """Test part 2 solutions."""
        for test in self.test_suite:
            with self.subTest(test=test, msg=test.day_name):
                if test.p2 is not None:
                    self.assertEqual(test.day_class.part2(), test.p2)
                else:
                    print("Part 2 answer is: ", test.day_class.part2())


if __name__ == "__main__":
    unittest.main()
