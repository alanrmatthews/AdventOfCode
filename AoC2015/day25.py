"""Advent of Code Day"""

import re
from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_first_line


class Day25(AdventOfCodeDay):
    """Advent of Code Day"""

    def part1(self):
        line = get_first_line(self.input_file)
        nums = re.findall(r"\d+", line)
        row = int(nums[0])
        col = int(nums[1])
        index = self.get_linear_index(row, col)

        value = 20151125
        for _ in range(1, index):
            value = (value * 252533) % 33554393
        return value

    def part2(self):
        return 0

    def get_linear_index(self, row, col):
        """Get the linear index of the given row and column (1-based)."""
        #    | 1   2   3   4   5   6
        # ---+---+---+---+---+---+---+
        #  1 |  1   3   6  10  15  21
        #  2 |  2   5   9  14  20
        #  3 |  4   8  13  19
        #  4 |  7  12  18
        #  5 | 11  17
        #  6 | 16

        row_start = 1
        counter = 1
        for _ in range(2, row + 1):
            row_start += counter
            counter += 1

        index = row_start
        counter = row + 1
        for _ in range(2, col + 1):
            index += counter
            counter += 1

        return index
