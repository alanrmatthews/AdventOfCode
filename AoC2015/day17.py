"""Day 17: No Such Thing as Too Much"""

from Utilities.aoc_day import AdventOfCodeDay


class Day17(AdventOfCodeDay):
    """Day 17: No Such Thing as Too Much"""

    def part1(self):
        with open(self.input_file, encoding="utf-8") as f:
            containers = [int(line.strip()) for line in f]
        return len(list(self.subset_sum(containers, 150, [])))

    def part2(self):
        with open(self.input_file, encoding="utf-8") as f:
            containers = [int(line.strip()) for line in f]
        subset = list(self.subset_sum(containers, 150, []))
        min_containers = min(len(sub) for sub in subset)
        return sum(1 for sub in subset if len(sub) == min_containers)

    def subset_sum(self, containers, target: int, used_containers: list, partial_sum=0):
        """Find all combinations of containers that sum to target."""
        if partial_sum == target:
            yield used_containers
        if partial_sum > target:
            return
        for idx, val in enumerate(containers):
            remaining = containers[idx + 1 :]
            yield from self.subset_sum(
                remaining, target, used_containers + [val], partial_sum + val
            )
