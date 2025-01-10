"""Advent of Code Day"""

from Utilities.aoc_day import AdventOfCodeDay


class Day3(AdventOfCodeDay):
    """Advent of Code Day"""

    def __init__(self, input_file):
        super().__init__(input_file)
        with open(input_file, encoding="utf-8") as file:
            self.data = file.readline().strip()

    def part1(self):
        visited = self.visit_houses(self.data, 1)
        return len(visited)

    def part2(self):
        visited = self.visit_houses(self.data, 2)
        return len(visited)

    def visit_houses(self, data, num_people):
        visited = set()
        people = [(0, 0) for _ in range(num_people)]
        current_person = 0

        visited.add((0, 0))

        for direction in data:
            x, y = people[current_person]
            if direction == "^":
                y += 1
            elif direction == "v":
                y -= 1
            elif direction == ">":
                x += 1
            elif direction == "<":
                x -= 1

            visited.add((x, y))
            people[current_person] = (x, y)
            current_person = (current_person + 1) % num_people

        return visited
