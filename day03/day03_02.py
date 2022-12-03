# AOC 2022 - Day 3 - Part 2
from string import ascii_letters

with open("input.txt", "r", encoding="utf-8") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

priorities = {s: n for s, n in zip(ascii_letters, range(1, 53))}
print(sum([priorities[set(r1).intersection(set(r2), set(r3)).pop()] for r1, r2, r3 in zip(*[iter(data)] * 3)]))
