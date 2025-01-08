"""Day 23: Opening the Turing Lock"""

import re
import functools
from Utilities.aoc_day import AdventOfCodeDay


class Day23(AdventOfCodeDay):
    """Day 23: Opening the Turing Lock"""

    def __init__(self, input_file: str):
        super().__init__(input_file)
        with open(self.input_file, encoding="utf-8") as file:
            self.instructions = [line.strip() for line in file]

    def part1(self):
        return self.run_instructions(0, 0)["b"]

    def part2(self):
        return self.run_instructions(1, 0)["b"]

    def run_instructions(self, initial_a, initial_b) -> tuple:
        """Run the instructions and return the registers"""
        registers = {"a": initial_a, "b": initial_b}
        i = 0
        while 0 <= i < len(self.instructions):
            di = 1
            ins, m2, m3 = self.decode_instruction(i)

            match ins:
                case "hlf":
                    registers[m2] //= 2
                case "tpl":
                    registers[m2] *= 3
                case "inc":
                    registers[m2] += 1
                case "jmp":
                    di = int(m2)
                case "jie":
                    if registers[m2] % 2 == 0:
                        di = int(m3)
                case "jio":
                    if registers[m2] == 1:
                        di = int(m3)
                case _:
                    raise ValueError(f"Unknown instruction {ins} at line {i}")
            i += di

        return registers

    @functools.lru_cache(maxsize=50)
    def decode_instruction(self, instruction: int) -> tuple:
        """Decode the instruction and return the components."""
        m = re.match(re.compile(r"(\w{3}) ([-+]?\d+|[ab]),? ?([+-]\d+)?"), self.instructions[instruction])
        if m:
            return m.group(1), m.group(2), m.group(3)
        else:
            raise ValueError(f"Invalid instruction format: {instruction}")
