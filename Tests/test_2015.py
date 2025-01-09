"""Test runner for 2015 Advent of Code solutions."""

import cProfile
import unittest
import time
import os

from parameterized import parameterized_class, parameterized

from AoC2015 import day1

from AoC2015.day2 import Day2
from AoC2015.day3 import Day3
from AoC2015.day4 import Day4
from AoC2015.day5 import Day5
from AoC2015.day6 import Day6
from AoC2015.day7 import Day7
from AoC2015.day8 import Day8
from AoC2015.day9 import Day9
from AoC2015.day10 import Day10
from AoC2015.day11 import Day11
from AoC2015.day12 import Day12
from AoC2015.day13 import Day13
from AoC2015.day14 import Day14
from AoC2015.day15 import Day15
from AoC2015.day16 import Day16
from AoC2015.day17 import Day17
from AoC2015.day18 import Day18
from AoC2015.day19 import Day19
from AoC2015.day20 import Day20
from AoC2015.day21 import Day21
from AoC2015.day22 import Day22
from AoC2015.day23 import Day23
from AoC2015.day24 import Day24
from AoC2015.day25 import Day25


inputs_dir = os.path.join(os.getcwd(), "Tests", "inputs", "2015")

test_suite = [
    (day1.Day1, 232, 1783),
    (Day2, 1598415, 3812909),
    (Day3, 2572, 2631),
    (Day4, 282749, 9962624),
    (Day5, 255, 55),
    (Day6, 377891, 14110788),
    (Day7, 16076, 2797),
    (Day8, 1350, 2085),
    (Day9, 117, 909),
    (Day10, 252594, 3579328),
    (Day11, "hepxxyzz", "heqaabcc"),
    (Day12, 156366, 96852),
    (Day13, 709, 668),
    (Day14, 2640, 1102),
    (Day15, 222870, 117936),
    (Day16, 213, 323),
    (Day17, 654, 57),
    (Day18, 1061, 1006),
    (Day19, 518, 200),
    (Day20, 786240, 831600),
    (Day21, 91, 158),
    (Day22, 900, 1216),
    (Day23, 307, 160),
    (Day24, 11266889531, 77387711),
    (Day25, 8997277, 0),
]


def get_class_name(cls, num, params_dict):
    # By default the generated class named includes either the "name"
    # parameter (if present), or the first string value. This example shows
    # multiple parameters being included in the generated class name:
    return f"{params_dict['Solver'].__name__}"


@parameterized_class(("Solver", "Expected1", "Expected2"), test_suite, class_name_func=get_class_name)
class Test2015(unittest.TestCase):
    """Test runner for 2015 Advent of Code solutions."""

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
        result = self.day.part2()
        if self.Expected2 is not None:
            self.assertEqual(result, self.Expected2)
        else:
            print("Part 2 answer is: ", result)


if __name__ == "__main__":
    r = unittest.main()
