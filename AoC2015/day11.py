"""Day 11: Corporate Policy"""

import re

from Utilities.aoc_day import AdventOfCodeDay
from Utilities.file_utils import get_first_line


class Day11(AdventOfCodeDay):
    """Day 11: Corporate Policy"""

    def __init__(self, input_file):
        """Constructor for day 11: Corporate Policy."""
        AdventOfCodeDay.__init__(self, input_file)
        self.part1_answer = None

    def part1(self):
        password = get_first_line(self.input_file)
        self.part1_answer = self.next_valid_password(password)
        return self.part1_answer

    def part2(self):
        if self.part1_answer is None:
            self.part1()
        return self.next_valid_password(self.part1_answer)

    def next_valid_password(self, password):
        """Find the next valid password after the given password."""
        n = self.next_password(password)
        while not self.is_valid_password(n):
            n = self.next_password(n)
        return n

    def next_password(self, password):
        """Increment the password by one."""
        # Problem says password is always 8 characters long
        idx = 7
        while idx >= 0:
            if password[idx] == "z":
                password = password[:idx] + "a" + password[idx + 1 :]
                idx -= 1
            else:
                password = password[:idx] + chr(ord(password[idx]) + 1) + password[idx + 1 :]
                break
        return password

    def is_valid_password(self, password):
        """Check if the password is valid."""

        # There's 2 ways to do this, either going char by char and checking everything, or using regex.
        # Going to use regex since it's cleaner and will require less code. Will go with the first option if it is too slow.

        # Password should not contain the letters 'i', 'o', or 'l'
        if "i" in password or "o" in password or "l" in password:
            return False

        # Password should contain at least two different, non-overlapping pairs of letters
        if len(re.findall(r"(.)\1", password)) < 2:
            return False

        # Password should contain at least one increasing straight of at least three letters
        if not re.search(r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)", password):
            return False

        return True
