"""Day 1: Not Quite Lisp"""

from Utilities.aoc_day import AdventOfCodeDay


class Day1(AdventOfCodeDay):
    """Day 1: Not Quite Lisp"""

    def part1(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return sum(1 if c == "(" else -1 for c in lines[0])

    def part2(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            floor = 0
            for i, c in enumerate(lines[0]):
                floor += 1 if c == "(" else -1
                if floor < 0:
                    return i + 1

        return None
