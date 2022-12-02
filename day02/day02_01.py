# AOC 2022 - Day 2 - Part 1

with open("input.txt", "r", encoding="utf-8") as f:
    data = [line.strip().split(" ") for line in f.readlines()]

WIN = 6
DRAW = 3
LOSE = 0
throw_equivalence_map = {"A": "X", "B": "Y", "C": "Z"}
throw_win_map = {"X": "C", "Y": "A", "Z": "B"}
throw_value_map = {"X": 1, "Y": 2, "Z": 3}

point_total = 0
for opponent_throw, my_throw in data:
    if my_throw == throw_equivalence_map[opponent_throw]:
        point_total += DRAW
    elif opponent_throw == throw_win_map[my_throw]:
        point_total += WIN
    point_total += throw_value_map[my_throw]
print(point_total)
