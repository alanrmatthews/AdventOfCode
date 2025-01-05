"""Day 8: Matchsticks"""

from Utilities.aoc_day import AdventOfCodeDay


class Day8(AdventOfCodeDay):
    """Day 8: Matchsticks"""

    def part1(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            return sum(self.decoded_difference(l.rstrip()) for l in file.readlines())

    def part2(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            return sum(self.encoded_difference(l.rstrip()) for l in file.readlines())

    def decoded_difference(self, line: str):
        """Calculate the difference in characters between the original string and the escaped string."""
        idx = 1
        total = 0
        while idx < len(line) - 1:
            total += 1
            if line[idx] == "\\":
                if line[idx + 1] == "x":
                    idx += 4
                else:
                    idx += 2
            else:
                idx += 1

        return len(line) - total

    def encoded_difference(self, line: str):
        """Calculate the difference in characters between the encoded string and the original string."""
        return 2 + line.count("\\") + line.count('"')
