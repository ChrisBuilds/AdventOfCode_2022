# AOC 2022 - Day 1 - Part 1

with open("input.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

elves: list[list[int]] = []
elf: list[int] = []
for calories in data:
    if not calories.strip():
        elves.append(elf)
        elf = []
        continue
    elf.append(int(calories.strip()))

print(sum(max(elves, key=sum)))
