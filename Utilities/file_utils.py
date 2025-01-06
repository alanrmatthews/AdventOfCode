"""File utilities for reading files and returning data in a usable format."""

import json
import re
import typing


def get_first_line(file_path: str) -> str:
    """Read the file at the given path and return the first line."""
    with open(file_path, encoding="utf-8") as file:
        return file.readline().strip()


def get_json_data(file_path: str) -> dict:
    """Read the file at the given path and return the json data."""
    return json.load(open(file_path, encoding="utf-8"))


def get_int_lines(file_path: str) -> typing.Generator[list[int]]:
    """Read the file at the given path and yields a list of integers for each line in the file (whitespace separated)."""
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            yield [int(value) for value in line.split()]


def get_character_lines(file_path: str) -> list[list[chr]]:
    """Read the file at the given path and return a list of characters for each line in the file."""
    with open(file_path, encoding="utf-8") as file:
        return [list(line.strip()) for line in file]


def get_character_lines_and_elements(file_path: str, pattern: str) -> tuple:
    """Reads the file in a list of characters and also return a dictionary of element locations in the list."""
    output_list = []
    element_locations = {}

    regex = re.compile(pattern)
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            for match in regex.finditer(line):
                element_locations.setdefault(match.group(), set()).add((len(output_list), match.start()))

            output_list.append(list(line.strip()))

    return output_list, element_locations
