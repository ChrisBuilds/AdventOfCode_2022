# AOC 2022 - Day 2 - Part 2
from collections import deque

with open("input.txt", "r", encoding="utf-8") as f:
    data = [line.strip().split(" ") for line in f.readlines()]

rotate_map = {"X": 1, "Y": 0, "Z": -1}
throw_value_map = {"A": 1, "B": 2, "C": 3}
results_map = {"X": 0, "Y": 3, "Z": 6}
throws = deque(throw_value_map.keys())

point_total = 0
for opponent_throw, result in data:
    throws.rotate(rotate_map[result])
    point_total += throw_value_map.get(throws[throw_value_map[opponent_throw] - 1]) + results_map[result]
    throws.rotate(rotate_map[result] * -1)
print(point_total)
