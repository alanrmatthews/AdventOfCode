"""Advent of Code Day"""

from collections import namedtuple
from Utilities.aoc_day import AdventOfCodeDay


class Day2(AdventOfCodeDay):
    """Advent of Code Day"""

    Dimensions = namedtuple("Dimensions", ["l", "w", "h"])

    def __init__(self, input_file):
        super().__init__(input_file)

        self.dimensions = []
        with open(input_file, encoding="utf-8") as file:
            for line in file:
                l, w, h = map(int, line.strip().split("x"))
                self.dimensions.append(self.Dimensions(l, w, h))

    def part1(self):
        return sum(2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l) for l, w, h in self.dimensions)

    def part2(self):
        return sum(2 * (l + w + h - max(l, w, h)) + l * w * h for l, w, h in self.dimensions)
