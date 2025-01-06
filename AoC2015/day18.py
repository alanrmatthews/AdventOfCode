"""Day 18: Like a GIF For Your Yard"""

from dataclasses import dataclass

from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_character_lines


@dataclass
class Light:
    """Class to hold light data."""

    state: bool
    neighbors: list
    frozen: bool = False
    neighbors_on = 0

    def update_state(self):
        """Switch the light to the next state."""
        if not self.frozen:
            if self.state:
                self.state = self.neighbors_on in (2, 3)
            else:
                self.state = self.neighbors_on == 3
        self.neighbors_on = 0


class Day18(AdventOfCodeDay):
    """Day 18: Like a GIF For Your Yard"""

    def __init__(self, input_file: str):
        super().__init__(input_file)
        self.num_steps = 100

    def part1(self):
        lines = get_character_lines(self.input_file)
        lights = self.get_lights(lines, ())

        return self.run_steps(lights)

    def part2(self):
        lines = get_character_lines(self.input_file)

        max_x = len(lines[0]) - 1
        max_y = len(lines) - 1
        corners = ((0, 0), (0, max_y), (max_x, 0), (max_x, max_y))

        lights = self.get_lights(lines, corners)

        return self.run_steps(lights)

    def get_lights(self, lines: list, frozen_lights: list) -> dict:
        """Return a dictionary of lights."""
        lights = {}

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                neighbors = [
                    (nx, ny)
                    for dx in (-1, 0, 1)
                    for dy in (-1, 0, 1)
                    if (dx, dy) != (0, 0)
                    and 0 <= (nx := x + dx) < len(line)
                    and 0 <= (ny := y + dy) < len(lines)
                ]

                lights[(x, y)] = Light(c == "#", neighbors)

        for light in frozen_lights:
            lights[light].state = True
            lights[light].frozen = True

        return lights

    def run_steps(self, lights: dict) -> int:
        """Run the steps for the lights."""
        for _ in range(self.num_steps):
            for light in lights.values():
                if light.state:
                    for neighbor in light.neighbors:
                        lights[neighbor].neighbors_on += 1

            for light in lights.values():
                light.update_state()

        return sum(light.state for light in lights.values())
