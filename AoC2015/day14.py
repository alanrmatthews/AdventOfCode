"""Day 14: Reindeer Olympics"""

import numpy as np
from Utilities.aoc_day import AdventOfCodeDay
from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    fly_speed: int
    fly_time: int
    rest_time: int


class Day14(AdventOfCodeDay):
    """Day 14: Reindeer Olympics"""

    def __init__(self, input_file: str):
        super().__init__(input_file)
        self.seconds = 2503

    def part1(self):
        reindeer = self.parse_input()
        return max(self.fly_seconds(r, self.seconds) for r in reindeer)

    def part2(self):
        reindeer = self.parse_input()
        reindeer_scores = [self.fly_seconds_points(r, self.seconds) for r in reindeer]
        reindeer_points = [0] * len(reindeer_scores)
        for i in range(1, self.seconds + 1):
            max_value = max(reindeer_scores[j][i] for j in range(len(reindeer_scores)))
            max_indices = [j for j in range(len(reindeer_scores)) if reindeer_scores[j][i] == max_value]
            for current_leader in max_indices:
                reindeer_points[current_leader] += 1
        return max(reindeer_points)

    def parse_input(self) -> list:
        """Parse the input file and return a list of classes."""
        output = []

        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                output.append(Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[13])))
        return output

    def fly_seconds(self, reindeer: Reindeer, seconds: int) -> int:
        """Calculate the distance a reindeer flies in the given number of seconds."""
        seconds_remaining = seconds
        distance = 0
        while seconds_remaining > 0:
            fly_time = min(reindeer.fly_time, seconds_remaining)
            distance += fly_time * reindeer.fly_speed
            seconds_remaining -= fly_time
            seconds_remaining -= reindeer.rest_time
        return distance

    def fly_seconds_points(self, reindeer: Reindeer, seconds: int) -> int:
        """Calculate the distance a reindeer has flown in a number of seconds."""
        seconds_remaining = seconds
        distances = [0]
        while seconds_remaining > 0:
            fly_time = min(reindeer.fly_time, seconds_remaining)
            distances += [distances[-1] + reindeer.fly_speed * s for s in range(1, fly_time + 1)]
            distances += [distances[-1]] * reindeer.rest_time
            seconds_remaining -= fly_time
            seconds_remaining -= reindeer.rest_time
        return distances
