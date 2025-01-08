"""Test runner for 2015 Advent of Code solutions."""

import cProfile
import unittest
import time
import os

from parameterized import parameterized_class

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
    ("Day 1", day1.Day1(os.path.join(inputs_dir, "day1.txt")), 232, 1783),
    ("Day 2", Day2(os.path.join(inputs_dir, "day2.txt")), None, None),
    ("Day 3", Day3(os.path.join(inputs_dir, "day3.txt")), None, None),
    ("Day 4", Day4(os.path.join(inputs_dir, "day4.txt")), None, None),
    ("Day 5", Day5(os.path.join(inputs_dir, "day5.txt")), None, None),
    ("Day 6", Day6(os.path.join(inputs_dir, "day6.txt")), None, None),
    ("Day 7", Day7(os.path.join(inputs_dir, "day7.txt")), None, None),
    ("Day 8", Day8(os.path.join(inputs_dir, "day8.txt")), 1350, 2085),
    ("Day 9", Day9(os.path.join(inputs_dir, "day9.txt")), 117, 909),
    ("Day 10", Day10(os.path.join(inputs_dir, "day10.txt")), 252594, 3579328),
    ("Day 11", Day11(os.path.join(inputs_dir, "day11.txt")), "hepxxyzz", "heqaabcc"),
    ("Day 12", Day12(os.path.join(inputs_dir, "day12.txt")), 156366, 96852),
    ("Day 13", Day13(os.path.join(inputs_dir, "day13.txt")), 709, 668),
    ("Day 14", Day14(os.path.join(inputs_dir, "day14.txt")), 2640, 1102),
    ("Day 15", Day15(os.path.join(inputs_dir, "day15.txt")), 222870, 117936),
    ("Day 16", Day16(os.path.join(inputs_dir, "day16.txt")), 213, 323),
    ("Day 17", Day17(os.path.join(inputs_dir, "day17.txt")), 654, 57),
    ("Day 18", Day18(os.path.join(inputs_dir, "day18.txt")), 1061, 1006),
    ("Day 19", Day19(os.path.join(inputs_dir, "day19.txt")), 518, 200),
    ("Day 20", Day20(os.path.join(inputs_dir, "day20.txt")), 786240, 831600),
    ("Day 21", Day21(os.path.join(inputs_dir, "day21.txt")), 91, 158),
    ("Day 22", Day22(os.path.join(inputs_dir, "day22.txt")), 900, 1216),
    ("Day 23", Day23(os.path.join(inputs_dir, "day23.txt")), 307, 160),
    ("Day 24", Day24(os.path.join(inputs_dir, "day24.txt")), None, None),
    ("Day 25", Day25(os.path.join(inputs_dir, "day25.txt")), None, None),
]


@parameterized_class(("Name", "Solver", "Expected1", "Expected2"), test_suite)
class Test2015(unittest.TestCase):
    """Test runner for 2015 Advent of Code solutions."""

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_part_1(self):
        """Test part 1 solutions."""
        result = self.Solver.part1()
        if self.Expected1 is not None:
            self.assertEqual(result, self.Expected1)
        else:
            print("Part 1 answer is: ", result)

    def test_part_2(self):
        """Test part 2 solutions."""
        result = self.Solver.part2()
        if self.Expected2 is not None:
            self.assertEqual(result, self.Expected2)
        else:
            print("Part 2 answer is: ", result)


if __name__ == "__main__":
    r = unittest.main()
