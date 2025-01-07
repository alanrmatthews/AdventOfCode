"""Day 19: Medicine for Rudolph"""

import re
import sys
from Utilities.aoc_day import AdventOfCodeDay


class Day19(AdventOfCodeDay):
    """Day 19: Medicine for Rudolph"""

    def __init__(self, input_file: str):
        """Constructor for Day 19: Medicine for Rudolph."""
        AdventOfCodeDay.__init__(self, input_file)
        self.replacements = {}
        self.rev_replacements = {}
        self.line = None
        self.min_part_2 = sys.maxsize

    def part1(self):
        self.parse_input()
        molecules = set()

        for key, replacements in self.replacements.items():
            for m in re.finditer(key, self.line):
                for replacement in replacements:
                    molecules.add(self.line[: m.start()] + replacement + self.line[m.end() :])

        return len(molecules)

    def part2(self):
        self.parse_input()
        self.min_replacements("e", self.line, 0)
        return self.min_part_2

    def parse_input(self):
        """Parse the input file for Day 19: Medicine for Rudolph."""
        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                s = line.split(" => ")

                if len(s) == 2:
                    self.replacements.setdefault(s[0], []).append(s[1])
                    self.rev_replacements.setdefault(s[1], []).append(s[0])
                else:
                    self.line = line

    def min_replacements(self, goal, test_line, count) -> tuple:
        """Find the minimum number of replacements to get to the target molecule."""
        if test_line == goal:
            return (True, count)

        for key, replacements in self.rev_replacements.items():
            for m in re.finditer(key, test_line):
                for replacement in replacements:
                    new_line = test_line[: m.start()] + replacement + test_line[m.end() :]
                    found, val = self.min_replacements(goal, new_line, count + 1)
                    if found:
                        self.min_part_2 = min(val, self.min_part_2)
                        return (True, val)

        return (False, 0)
