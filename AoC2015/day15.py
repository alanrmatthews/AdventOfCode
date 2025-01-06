"""Day 15: Science for Hungry People"""

from dataclasses import dataclass
from Utilities.aoc_day import AdventOfCodeDay


@dataclass
class Ingredient:
    """Class to hold an ingredient and its properties."""

    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


class Day15(AdventOfCodeDay):
    """Day 15: Science for Hungry People"""

    def __init__(self, input_file: str):
        """Constructor for Day"""
        AdventOfCodeDay.__init__(self, input_file)
        self.ingredients = None

    def part1(self):
        self.ingredients = self.parse_input()
        return self.find_best_cookie()

    def part2(self):
        self.ingredients = self.parse_input()
        return self.find_best_cookie_calories()

    def parse_input(self) -> dict:
        """Parse the input file and return a dictionary of scores."""
        ingredients = []

        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                ingredients.append(Ingredient(parts[0][:-1], int(parts[2][:-1]), int(parts[4][:-1]), int(parts[6][:-1]), int(parts[8][:-1]), int(parts[10])))

        return ingredients

    def score_cookie(self, amounts: list) -> int:
        """Calculate the score of a cookie based on its ingredients and amounts."""
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0

        for idx, ingredient in enumerate(self.ingredients):
            capacity += ingredient.capacity * amounts[idx]
            durability += ingredient.durability * amounts[idx]
            flavor += ingredient.flavor * amounts[idx]
            texture += ingredient.texture * amounts[idx]

        return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

    def score_cookie_calories(self, amounts: list) -> int:
        """Calculate the score of a cookie based on its ingredients and amounts."""
        return sum(amounts[i] * self.ingredients[i].calories for i in range(len(self.ingredients)))

    def find_best_cookie(self) -> int:
        """Find the best cookie based on the ingredients."""
        best_score = 0

        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - i - j):
                    l = 100 - i - j - k
                    amounts = [i, j, k, l]
                    score = self.score_cookie(amounts)

                    best_score = max(score, best_score)

        return best_score

    def find_best_cookie_calories(self) -> int:
        """Find the best cookie based on the ingredients and calorie count."""
        best_score = 0

        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - i - j):
                    l = 100 - i - j - k
                    amounts = [i, j, k, l]
                    if self.score_cookie_calories(amounts) == 500:
                        score = self.score_cookie(amounts)
                        best_score = max(score, best_score)
        return best_score
