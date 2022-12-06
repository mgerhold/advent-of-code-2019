from enum import Enum
from typing import Callable


class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


def get_next_points(
    current_point: tuple[int, int, int],
    direction: Direction,
    amount: int
) -> list[tuple[int, int, int]]:
    start_x, start_y, start_distance = current_point
    movement = range(0, amount + 1)
    mapping: dict[Direction, Callable[[int], tuple[int, int, int]]] = {
        Direction.RIGHT: lambda delta: (start_x + delta, start_y, start_distance + delta),
        Direction.LEFT: lambda delta: (start_x - delta, start_y, start_distance + delta),
        Direction.UP: lambda delta: (start_x, start_y + delta, start_distance + delta),
        Direction.DOWN: lambda delta: (start_x, start_y - delta, start_distance + delta),
    }
    return [mapping[direction](delta) for delta in movement]


def string_to_direction(string: str) -> Direction:
    directions = {
        "R": Direction.RIGHT,
        "L": Direction.LEFT,
        "U": Direction.UP,
        "D": Direction.DOWN,
    }
    return directions[string]  # raises key error upon failure


def parse_route(string: str) -> dict[tuple[int, int], int]:
    parts = string.split(",")
    result = dict()
    last_point = (0, 0, 0)  # x, y, distance
    for part in parts:
        direction, amount = (string_to_direction(part[0]), int(part[1:]))
        next_points = get_next_points(last_point, direction, amount)
        for x, y, distance in next_points:
            if (x, y) not in result:
                result[(x, y)] = distance
        last_point = next_points[-1]
    return result


def get_route_intersections(
    first: dict[tuple[int, int], int],
    second: dict[tuple[int, int], int]
) -> set[tuple[int, int]]:
    result = set(first.keys()).intersection(set(second.keys()))
    result.discard((0, 0))  # origin doesn't count as intersection
    return result


def manhattan_distance(point: tuple[int, int]) -> int:
    return abs(point[0]) + abs(point[1])


class Part(Enum):
    PART_1 = 1
    PART_2 = 2


def get_closest_intersection(
    first: dict[tuple[int, int], int],
    second: dict[tuple[int, int], int],
    intersections: set[tuple[int, int]],
    part: Part
) -> tuple[int, int]:
    if part == Part.PART_1:
        return min(intersections, key=manhattan_distance)
    else:
        assert part == Part.PART_2
        return min(intersections, key=lambda intersection: first[intersection] + second[intersection])


def main() -> None:
    FILENAME = "real_input.txt"

    with open(FILENAME) as file:
        routes = [parse_route(line) for line in file]
        assert len(routes) == 2

    # part 1
    print("part 1: ", manhattan_distance(get_closest_intersection(
        routes[0],
        routes[1],
        get_route_intersections(routes[0], routes[1]),
        Part.PART_1
    )))

    # part 2
    closest_intersection = get_closest_intersection(
        routes[0],
        routes[1],
        get_route_intersections(routes[0], routes[1]),
        Part.PART_2
    )
    total_distance = sum(routes[i][closest_intersection] for i in range(2))
    print("part 2: ", total_distance)


if __name__ == "__main__":
    main()
