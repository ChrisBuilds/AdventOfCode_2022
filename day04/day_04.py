# day_04.py
# Advent of Code 2022 - Day 04


import pathlib
import sys


def parse(puzzle_input) -> list[tuple[tuple[int, int]]]:
    """Parse input."""
    parsed = []
    for line in puzzle_input.split("\n"):
        sections_assignments = line.split(",")
        assignment_ranges = []
        for sections_assignment in sections_assignments:
            start, end = sections_assignment.split("-")
            assignment_ranges.append((int(start), int(end)))
        parsed.append(tuple(assignment_ranges))
    return parsed


def part1(data):
    """Solve part 1."""
    subset_count = 0
    for assignment_range in data:
        assignment_a = set(range(assignment_range[0][0], assignment_range[0][1] + 1))
        assignment_b = set(range(assignment_range[1][0], assignment_range[1][1] + 1))
        if assignment_a <= assignment_b or assignment_b <= assignment_a:
            subset_count += 1
    return subset_count


def part2(data):
    """Solve part 2."""
    subset_count = 0
    for assignment_range in data:
        assignment_a = set(range(assignment_range[0][0], assignment_range[0][1] + 1))
        assignment_b = set(range(assignment_range[1][0], assignment_range[1][1] + 1))
        if assignment_a & assignment_b:
            subset_count += 1
    return subset_count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def main():
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print(f"Part 1 Solution: {solutions[0]}\nPart 2 Solution: {solutions[1]}")


if __name__ == "__main__":
    main()
