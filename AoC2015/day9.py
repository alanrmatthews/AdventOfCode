"""Day 9: All in a Single Night"""

import itertools
from Utilities.aoc_day import AdventOfCodeDay


class Day9(AdventOfCodeDay):
    """Day 9: All in a Single Night"""

    def part1(self):
        costs = self.parse_input()
        nodes = list(costs.keys())
        return self.calculate_routes(costs, nodes)[0]

    def part2(self):
        costs = self.parse_input()
        nodes = list(costs.keys())
        return self.calculate_routes(costs, nodes)[1]

    def parse_input(self) -> dict:
        """Parse the input file and return a dictionary of costs."""
        costs = {}

        with open(self.input_file, "r", encoding="utf=8") as file:
            for line in file:
                parts = line.strip().split(" ")
                costs.setdefault(parts[0], {})[parts[2]] = int(parts[4])
                costs.setdefault(parts[2], {})[parts[0]] = int(parts[4])
        return costs

    def calculate_routes(self, costs: dict, nodes: list) -> tuple:
        """Calculate the shortest and longest routes for the given nodes."""
        min_distance = float("inf")
        max_distance = 0

        for p in itertools.permutations(nodes):
            total = 0
            for i in range(len(p) - 1):
                total += costs[p[i]][p[i + 1]]
            min_distance = min(min_distance, total)
            max_distance = max(max_distance, total)

        return min_distance, max_distance
