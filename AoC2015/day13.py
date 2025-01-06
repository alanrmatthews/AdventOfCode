"""Day 13: Knights of the Dinner Table"""

import itertools
from Utilities.aoc_day import AdventOfCodeDay


class Day13(AdventOfCodeDay):
    """Day 13: Knights of the Dinner Table"""

    # Like Day 9, there's probably a more efficient way to do this, but if going thru permutations works,
    # and is fast enough, I'll stick with that.

    def part1(self):
        scores = self.parse_input()
        return self.get_max_seating_score(scores)

    def part2(self):
        scores = self.parse_input()
        for person in set(x[0] for x in scores):
            scores[(person, "me")] = 0
            scores[("me", person)] = 0
        return self.get_max_seating_score(scores)

    def parse_input(self) -> dict:
        """Parse the input file and return a dictionary of scores."""
        scores = {}

        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                person = parts[0]
                neighbor = parts[-1][:-1]
                score = int(parts[3])
                if parts[2] == "lose":
                    score = -score
                scores[(person, neighbor)] = score

        return scores

    def get_max_seating_score(self, scores: dict) -> int:
        """Get the maximum seating score for the given scores."""
        totals = []
        for p in itertools.permutations(set(x[0] for x in scores)):
            total = 0
            for idx, person in enumerate(p):
                next_person = p[(idx + 1) % len(p)]
                total += scores[(person, next_person)] + scores[(next_person, person)]
            totals.append(total)
        return max(totals)
