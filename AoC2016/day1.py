"""Advent of Code Day"""

from enum import Enum
import re

from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_first_line

class Direction(Enum):
    """Direction enum for Day 1."""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Point:
    """Point class for Day 1."""

    def __init__(self, start_x=0, start_y=0):
        """Initialize the Point class."""
        self.start_x = start_x
        self.start_y = start_y
        self.x = self.start_x
        self.y = self.start_y
        self.visited = {(self.start_x, self.start_y)}
        self.direction = Direction.NORTH

    def distance_from_origin(self) -> int:
        """Return the Manhattan distance from the origin."""
        return abs(self.x - self.start_x) + abs(self.y - self.start_y)

    def turn(self, turn: str):
        """Turn the point."""
        if turn == "L":
            self.direction = Direction((self.direction.value - 1) % 4)
        else:
            self.direction = Direction((self.direction.value + 1) % 4)

    def move(self, steps: int, stop_at_duplicate=False) -> bool:
        """Move the point and update the visited list."""
        for _ in range(steps):
            if self.direction == Direction.NORTH:
                self.y += 1
            elif self.direction == Direction.EAST:
                self.x += 1
            elif self.direction == Direction.SOUTH:
                self.y -= 1
            elif self.direction == Direction.WEST:
                self.x -= 1

            if stop_at_duplicate and (self.x, self.y) in self.visited:
                return True
            self.visited.add((self.x, self.y))
        return False

class Day1(AdventOfCodeDay):
    """Advent of Code Day"""

    def part1(self):
        line = get_first_line(self.input_file)
        return self.traverse(Point(), line)

    def part2(self):
        line = get_first_line(self.input_file)
        return self.traverse(Point(), line, True)

    def traverse(self, pos, line, stop_at_duplicate=False):
        """Traverse the path and return the Manhattan distance from the origin."""
        for c in re.finditer(r"([A-Z])(\d+)", line):
            turn = c.group(1)
            n = int(c.group(2))

            pos.turn(turn)
            result = pos.move(n, stop_at_duplicate)

            if stop_at_duplicate and result:
                return pos.distance_from_origin()
        return pos.distance_from_origin()
