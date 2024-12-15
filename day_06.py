from collections import Counter


def parse_maze(file):
    start_pos = None
    maze = {}

    with open(file) as f:
        for i, line in enumerate(f.read().splitlines()):
            for j, item in enumerate(list(line)):
                p = (i, j)
                if item == "^":
                    start_pos = p
                    maze[p] = "."
                else:
                    maze[p] = item

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


def maze_combinations(maze):
    for p, v in maze.items():
        if v == ".":
            copy = maze.copy()
            copy[p] = "#"
            yield copy


def traverse(start_pos, maze):
    curr_pos = start_pos
    curr_direction = "north"
    yield (curr_pos, ".")
    while (next_pos := next_position(curr_pos, curr_direction)) in maze:
        match maze[next_pos]:
            case ".":
                curr_pos = next_pos
                yield (curr_pos, ".")
            case "#":
                curr_direction = next_direction(curr_direction)
                yield (curr_pos, "#")


def main():
    start_pos, maze = parse_maze("input/day_06_example.txt")

    distinct = set([p for p, v in traverse(start_pos, maze) if v == "."])

    assert len(distinct) == 41
    # assert len(distinct) == 5095

    num_loops = 0
    for m in maze_combinations(maze):
        visited = Counter()
        for p, v in traverse(start_pos, m):
            if v == "#":
                if visited[p] > 1:
                    num_loops += 1
                    break
                visited[p] += 1

    assert num_loops == 6
    # assert num_loops == 1933


if __name__ == "__main__":
    main()
