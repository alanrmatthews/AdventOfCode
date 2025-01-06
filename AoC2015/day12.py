"""Day 12: JSAbacusFramework.io"""

import re
import json
from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_first_line


class Day12(AdventOfCodeDay):
    """Day 12: JSAbacusFramework.io"""

    def part1(self):
        line = get_first_line(self.input_file)
        return sum(map(int, re.findall(r"(-?\d+)", line)))

    def part2(self):
        line = get_first_line(self.input_file)
        data = json.loads(line)
        return self.json_sum(data)

    def json_sum(self, data):
        """Sum all numbers in the json data, ignoring any object (dict) that has a value of 'red'."""
        if isinstance(data, int):
            return data
        elif isinstance(data, list):
            return sum(self.json_sum(item) for item in data)
        elif isinstance(data, dict):
            if "red" in data.values():
                return 0
            return sum(self.json_sum(item) for item in data.values())
        return 0
