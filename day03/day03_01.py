# AOC 2022 - Day 3 - Part 1
from string import ascii_letters

with open("input.txt", "r", encoding="utf-8") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

priorities = {s: n for s, n in zip(ascii_letters, range(1, 53))}

priorities_sum = 0
for rucksack in data:
    r1 = set(rucksack[: len(rucksack) // 2])
    r2 = set(rucksack[len(rucksack) // 2 :])
    common = r1.intersection(r2)
    priorities_sum += priorities[common.pop()]
print(priorities_sum)
