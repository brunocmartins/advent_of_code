from utils.input_reader import read_puzzle_input


def point_to_zero(puzzle_input: list[str]) -> int:
    pos = 50
    number_of_zeros = 0
    for rotation in puzzle_input:
        dir_ = rotation[0]
        steps = int(rotation[1:])

        if dir_ == "R":
            first_click = 100 - pos if pos != 0 else 100
            crossings = 0 if steps < first_click else (steps - first_click) // 100 + 1
            pos = (pos + steps) % 100
        elif dir_ == "L":
            first_click = pos if pos != 0 else 100
            crossings = 0 if steps < first_click else (steps - first_click) // 100 + 1
            pos = (pos - steps) % 100

        number_of_zeros += crossings

    return number_of_zeros


def main():
    puzzle_input = read_puzzle_input(2025)
    num_zeros = point_to_zero(puzzle_input)
    print(num_zeros)


if __name__ == "__main__":
    main()
