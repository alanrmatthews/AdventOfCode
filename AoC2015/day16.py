"""Day 16: Aunt Sue"""

import re
from Utilities.aoc_day import AdventOfCodeDay


class Day16(AdventOfCodeDay):
    """Day 16: Aunt Sue"""

    def __init__(self, input_file: str):
        """Constructor for Day 16: Aunt Sue."""
        AdventOfCodeDay.__init__(self, input_file)
        self.target = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }

    def part1(self):
        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                match = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)
                if (
                    self.target[match.group(2)] == int(match.group(3))
                    and self.target[match.group(4)] == int(match.group(5))
                    and self.target[match.group(6)] == int(match.group(7))
                ):
                    return int(match.group(1))
        return None

    def part2(self):
        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                match = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)
                if self.is_match(match):
                    return int(match.group(1))
        return None

    def is_match(self, match):
        """Check if the match is a match."""
        for m in [
            (match.group(2), int(match.group(3))),
            (match.group(4), int(match.group(5))),
            (match.group(6), int(match.group(7))),
        ]:
            if m[0] in ["cats", "trees"]:
                if m[1] <= self.target[m[0]]:
                    return False
            elif m[0] in ["pomeranians", "goldfish"]:
                if m[1] >= self.target[m[0]]:
                    return False
            elif m[1] != self.target[m[0]]:
                return False
        return True
