from enum import Enum

class Part(Enum):
    PART1 = 1
    PART2 = 2

def calc_fuel(mass: int, part: Part=Part.PART1) -> int:
    fuel = mass // 3 - 2
    if part == Part.PART1:
        return fuel
    else:
        assert part == Part.PART2
        if fuel < 0:
            return 0
        else:
            return calc_fuel(fuel, part) + fuel

with open("real_input.txt") as file:
    print(sum(calc_fuel(int(line), Part.PART2) for line in file))
