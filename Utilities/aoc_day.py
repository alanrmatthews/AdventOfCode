"""Base class for Advent of Code days."""


class AdventOfCodeDay:
    """Base class for Advent of Code days."""

    def __init__(self, input_file: str):
        self.input_file = input_file

    def part1(self):
        """Returns the solution for part 1 of the day."""
        raise NotImplementedError

    def part2(self):
        """Returns the solution for part 2 of the day."""
        raise NotImplementedError

    def in_bounds(self, grid: list[list], pos: tuple[int, int]) -> bool:
        """Returns True if the tuple is in bounds of the grid."""
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])
