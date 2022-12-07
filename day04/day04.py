from enum import Enum


class Part(Enum):
    Part1 = 1
    Part2 = 2


def get_digit_counts(password: str) -> dict[int, int]:
    counts: dict[int, int] = dict()
    for c in password:
        num = int(c)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts


def meets_criteria(password: str, part: Part) -> bool:
    counts: dict[int, int] = get_digit_counts(password) \
        if part == Part.Part2 \
        else dict()

    found_double = False
    for i in range(1, len(password)):
        if password[i] < password[i - 1]:
            return False
        if part == Part.Part1 or (password[i] == password[i - 1] and counts[int(password[i])] == 2):
            found_double = True
    return found_double


def main() -> None:
    INPUT = "145852-616942"
    FROM, TO = [int(x) for x in INPUT.split("-")]
    for (i, part) in enumerate([Part.Part1, Part.Part2]):
        print(
            f"part {i + 1}: {sum(1 for x in range(FROM, TO + 1) if meets_criteria(str(x), part))}")


if __name__ == "__main__":
    main()
