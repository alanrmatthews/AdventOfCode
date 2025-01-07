"""Day 20: Infinite Elves and Infinite Houses"""

from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_first_line


class Day20(AdventOfCodeDay):
    """Day 20: Infinite Elves and Infinite Houses"""

    def part1(self):
        # This is a sum-of-divisors problem, so we can skip multiplying by 10.
        last_house = int(get_first_line(self.input_file))
        target = last_house // 10
        visits = [0] * target

        end = target
        for i in range(target, 1, -1):
            for j in range(i, end, i):
                visits[j] += i
                if visits[j] >= target:
                    end = j
                    break
        for i, s in enumerate(visits):
            if s >= target:
                return i

        return None

    def part2(self):
        # This is a sum-of-divisors problem, so we can skip multiplying by 10.
        # Same as part 1 but divide by 11 and constrain the range in the 'j' loop.
        last_house = int(get_first_line(self.input_file))
        target = last_house // 11
        visits = [0] * target
        max_houses = 50

        end = target
        for i in range(target, 1, -1):
            for j in range(i, min(end, i * (max_houses + 1)), i):
                visits[j] += i
                if visits[j] >= target:
                    end = j
                    break
        for i, s in enumerate(visits):
            if s > target:
                return i

        return None
