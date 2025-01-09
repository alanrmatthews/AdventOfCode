"""Day 24: It Hangs in the Balance"""

import itertools
import math
from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_int_list


# Iterations = 84187
# Bins - 2 = 6
class Day24(AdventOfCodeDay):
    """Day 24: It Hangs in the Balance"""

    def part1(self):
        # Looks like a Largest Differencing Method problem
        lines = list(get_int_list(self.input_file))
        lines.sort(reverse=True)
        matching_bins = []
        self.partition(lines, 3, matching_bins)
        return min(math.prod(bin) for bin in matching_bins)

    def part2(self):
        # Looks like a Largest Differencing Method problem
        lines = list(get_int_list(self.input_file))
        lines.sort(reverse=True)
        matching_bins = []
        self.partition(lines, 4, matching_bins)
        return min(math.prod(bin) for bin in matching_bins)

    def partition(self, s: list, num_bins: int, matching_bins: list, first_bin_size=1):
        """Partition a list into k groups."""
        found = False
        sum_presents = sum(s)

        for p in itertools.combinations(s, first_bin_size):
            if sum(p) == sum_presents // num_bins:
                found = True
                matching_bins.append(p)

        if not found:
            self.partition(s, num_bins, matching_bins, first_bin_size + 1)
