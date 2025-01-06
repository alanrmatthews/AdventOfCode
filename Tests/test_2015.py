"""Test runner for 2015 Advent of Code solutions."""

import cProfile
from dataclasses import dataclass
import unittest
import os

from AoC2015.day1 import Day1
from AoC2015.day8 import Day8
from AoC2015.day9 import Day9
from AoC2015.day10 import Day10
from AoC2015.day11 import Day11
from AoC2015.day12 import Day12
from Utilities.aoc_day import AdventOfCodeDay


@dataclass
class TestData:
    """Class to hold test data for each day's solution."""

    day_name: str
    day_class: AdventOfCodeDay
    p1: int = None
    p2: int = None
    p1s: str = None
    p2s: str = None


class Test2015(unittest.TestCase):
    """Test runner for 2015 Advent of Code solutions."""

    inputs_dir = os.path.join(os.getcwd(), "Tests", "inputs", "2015")

    test_suite = [
        # TestData("Day 1", Day1(os.path.join(inputs_dir, "day1.txt")), 232, 1783),
        # TestData("Day 2", Day2(os.path.join(inputs_dir, "day2.txt")), None, None),
        # TestData("Day 3", Day3(os.path.join(inputs_dir, "day3.txt")), None, None),
        # TestData("Day 4", Day4(os.path.join(inputs_dir, "day4.txt")), None, None),
        # TestData("Day 5", Day5(os.path.join(inputs_dir, "day5.txt")), None, None),
        # TestData("Day 6", Day6(os.path.join(inputs_dir, "day6.txt")), None, None),
        # TestData("Day 7", Day7(os.path.join(inputs_dir, "day7.txt")), None, None),
        # TestData("Day 8", Day8(os.path.join(inputs_dir, "day8.txt")), 1350, 2085),
        # TestData("Day 9", Day9(os.path.join(inputs_dir, "day9.txt")), 117, 909),
        # TestData("Day 10", Day10(os.path.join(inputs_dir, "day10.txt")), 252594, 3579328),
        # TestData("Day 11", Day11(os.path.join(inputs_dir, "day11.txt")), p1s="hepxxyzz", p2s="heqaabcc"),
        TestData("Day 12", Day12(os.path.join(inputs_dir, "day12.txt")), 156366, 96852),
        # TestData("Day 13", Day13(os.path.join(inputs_dir, "day13.txt")), None, None),
        # TestData("Day 14", Day14(os.path.join(inputs_dir, "day14.txt")), None, None),
        # TestData("Day 15", Day15(os.path.join(inputs_dir, "day15.txt")), None, None),
        # TestData("Day 16", Day16(os.path.join(inputs_dir, "day16.txt")), None, None),
        # TestData("Day 17", Day17(os.path.join(inputs_dir, "day17.txt")), None, None),
        # TestData("Day 18", Day18(os.path.join(inputs_dir, "day18.txt")), None, None),
        # TestData("Day 19", Day19(os.path.join(inputs_dir, "day19.txt")), None, None),
        # TestData("Day 20", Day20(os.path.join(inputs_dir, "day20.txt")), None, None),
        # TestData("Day 21", Day21(os.path.join(inputs_dir, "day21.txt")), None, None),
        # TestData("Day 22", Day22(os.path.join(inputs_dir, "day22.txt")), None, None),
        # TestData("Day 23", Day23(os.path.join(inputs_dir, "day23.txt")), None, None),
        # TestData("Day 24", Day24(os.path.join(inputs_dir, "day24.txt")), None, None),
        # TestData("Day 25", Day25(os.path.join(inputs_dir, "day25.txt")), None, None),
    ]

    def test_part_1(self):
        """Test part 1 solutions."""
        for test in self.test_suite:
            with self.subTest(test=test, msg=test.day_name):
                if test.p1 is not None:
                    self.assertEqual(test.day_class.part1(), test.p1)
                elif test.p1s is not None:
                    self.assertEqual(test.day_class.part1(), test.p1s)
                else:
                    print("Part 1 answer is: ", test.day_class.part1())

    def test_part_2(self):
        """Test part 2 solutions."""
        for test in self.test_suite:
            with self.subTest(test=test, msg=test.day_name):
                # with cProfile.Profile() as pr:
                if test.p2 is not None:
                    self.assertEqual(test.day_class.part2(), test.p2)
                elif test.p2s is not None:
                    self.assertEqual(test.day_class.part2(), test.p2s)
                else:
                    print("Part 2 answer is: ", test.day_class.part2())
                # pr.print_stats()


if __name__ == "__main__":
    unittest.main()
