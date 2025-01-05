"""Day 10: Elves Look, Elves Say"""

from Utilities.aoc_day import AdventOfCodeDay


class Day10(AdventOfCodeDay):
    """Day 10: Elves Look, Elves Say"""

    def part1(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            val = file.readline().strip()

        return self.look_and_say(val, 40)

    def part2(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            val = file.readline().strip()

        return self.look_and_say(val, 50)

    def look_and_say(self, val: str, iterations: int) -> int:
        """Look and say the input string for the given number of iterations."""
        for _ in range(iterations):
            val = self.look_and_say_once(val)
        return len(val)

    def look_and_say_once(self, val: list) -> str:
        """Look and say the input string once."""
        result = []
        i = 0
        len_val = len(val)
        while i < len_val:
            c = val[i]
            count = 1
            i += 1
            while i < len_val and val[i] == c:
                count += 1
                i += 1
            result += [str(count), c]
        return "".join(result)
