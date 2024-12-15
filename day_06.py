from collections import Counter


def parse_maze(file):
    start_pos = None
    maze = {}

    with open(file) as f:
        for i, line in enumerate(f.read().splitlines()):
            for j, item in enumerate(list(line)):
                pos = (i, j)
                if item == "^":
                    start_pos = pos
                    maze[pos] = "."
                else:
                    maze[pos] = item

    return start_pos, maze


def next_position(pos, direction):
    row, col = pos

    match direction:
        case "north":
            return (row - 1, col)
        case "south":
            return (row + 1, col)
        case "east":
            return (row, col + 1)
        case "west":
            return (row, col - 1)


def next_direction(direction):
    match direction:
        case "north":
            return "east"
        case "south":
            return "west"
        case "east":
            return "south"
        case "west":
            return "north"


def main():
    start_pos, maze = parse_maze("input/day_06.txt")
    distinct_pos = set([start_pos])

    curr_pos = start_pos
    curr_direction = "north"
    while (next_pos := next_position(curr_pos, curr_direction)) in maze:
        match maze[next_pos]:
            case ".":
                distinct_pos.add(next_pos)
                curr_pos = next_pos
            case "#":
                curr_direction = next_direction(curr_direction)

    # assert len(distinct_pos) == 41
    assert len(distinct_pos) == 5095


if __name__ == "__main__":
    main()
