from utils.input_reader import read_puzzle_input


def point_to_zero(puzzle_input: list[str]) -> int:
    pos = 50
    number_of_zeros = 0
    for rotation in puzzle_input:
        if "L" in rotation:
            val = int(rotation.split("L")[1])
            pos -= val
        elif "R" in rotation:
            val = int(rotation.split("R")[1])
            pos += val
        pos %= 100

        if pos == 0:
            number_of_zeros += 1

    return number_of_zeros


def main():
    puzzle_input = read_puzzle_input(2025)
    num_zeros = point_to_zero(puzzle_input)
    print(num_zeros)


if __name__ == "__main__":
    main()
