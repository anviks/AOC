from utils_anviks import parse_file_content
from collections import Counter


class Vent:
    def __init__(self, start: tuple[int, int], end: tuple[int, int]):
        self.start = start
        self.end = end

    def get_covered_coords(self):
        coords = []

        start_x, end_x = self.start[0], self.end[0]
        start_y, end_y = self.start[1], self.end[1]
        smaller_x, larger_x = sorted([start_x, end_x])
        smaller_y, larger_y = sorted([start_y, end_y])

        if start_x == end_x:
            for i in range(smaller_y, larger_y + 1):
                coords.append((start_x, i))
        elif start_y == end_y:
            for i in range(smaller_x, larger_x + 1):
                coords.append((i, start_y))
        else:
            range_end_x = end_x - start_x
            range_end_y = end_y - start_y
            step_x = 1 if range_end_x > 0 else -1
            step_y = 1 if range_end_y > 0 else -1
            for x, y in zip(range(0, range_end_x + step_x, step_x), range(0, range_end_y + step_y, step_y)):
                coords.append((start_x + x, start_y + y))

        return coords


def solution(part: int):
    data = parse_file_content('data.txt', ('\n', ' -> ', ','), int)
    vents = []
    covered_coords = []

    for vent in data:
        (start_x, start_y), (end_x, end_y) = vent

        if part == 1 and start_x != end_x and start_y != end_y:
            continue

        vents.append(
            Vent(
                (start_x, start_y),
                (end_x, end_y)
            ))

    for vent in vents:
        covered_coords.extend(vent.get_covered_coords())

    counts = Counter(covered_coords)

    return len([coord for coord in counts if counts[coord] > 1])


def main():
    print(solution(1))  # 7473
    print(solution(2))  # 24164

    vent = Vent((3, 3), (5, 1))
    print(vent.get_covered_coords())


if __name__ == '__main__':
    main()

