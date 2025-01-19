"""Test runner for 2016 Advent of Code solutions."""

import cProfile
import unittest
import time
import os

from parameterized import parameterized_class

from AoC2016.day1 import Day1
from AoC2016.day2 import Day2
from AoC2016.day3 import Day3
from AoC2016.day4 import Day4
from AoC2016.day5 import Day5
from AoC2016.day6 import Day6
from AoC2016.day7 import Day7
from AoC2016.day8 import Day8
from AoC2016.day9 import Day9
from AoC2016.day10 import Day10
from AoC2016.day11 import Day11
from AoC2016.day12 import Day12
from AoC2016.day13 import Day13
from AoC2016.day14 import Day14
from AoC2016.day15 import Day15
from AoC2016.day16 import Day16
from AoC2016.day17 import Day17
from AoC2016.day18 import Day18
from AoC2016.day19 import Day19
from AoC2016.day20 import Day20
from AoC2016.day21 import Day21
from AoC2016.day22 import Day22
from AoC2016.day23 import Day23
from AoC2016.day24 import Day24
from AoC2016.day25 import Day25


inputs_dir = os.path.join(os.getcwd(), "Tests", "inputs", "2016")

test_suite = [
    (Day1, 271, 153),
    (Day2, None, None),
    (Day3, None, None),
    (Day4, None, None),
    (Day5, None, None),
    (Day6, None, None),
    (Day7, None, None),
    (Day8, None, None),
    (Day9, None, None),
    (Day10, None, None),
    (Day11, None, None),
    (Day12, None, None),
    (Day13, None, None),
    (Day14, None, None),
    (Day15, None, None),
    (Day16, None, None),
    (Day17, None, None),
    (Day18, None, None),
    (Day19, None, None),
    (Day20, None, None),
    (Day21, None, None),
    (Day22, None, None),
    (Day23, None, None),
    (Day24, None, None),
    (Day25, None, None),
]


def get_class_name(cls, num, params_dict):
    # By default the generated class named includes either the "name"
    # parameter (if present), or the first string value. This example shows
    # multiple parameters being included in the generated class name:
    return f"{params_dict['Solver'].__name__}"


@parameterized_class(("Solver", "Expected1", "Expected2"), test_suite, class_name_func=get_class_name)
class Test2016(unittest.TestCase):
    """Test runner for 2016 Advent of Code solutions."""

    def setUp(self):
        name = self.Solver.__name__
        file_name = name.replace(" ", "").lower() + ".txt"
        input_path = os.path.join(inputs_dir, file_name)
        self.startTime = time.time()
        self.day = self.Solver(input_path)

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_part_1(self):
        """Test part 1 solutions."""
        result = self.day.part1()
        if self.Expected1 is not None:
            self.assertEqual(result, self.Expected1)
        else:
            print("Part 1 answer is: ", result)

    def test_part_2(self):
        """Test part 2 solutions."""
        # with cProfile.Profile() as pr:
        result = self.day.part2()
        # pr.print_stats()
        if self.Expected2 is not None:
            self.assertEqual(result, self.Expected2)
        else:
            print("Part 2 answer is: ", result)


if __name__ == "__main__":
    unittest.main()
