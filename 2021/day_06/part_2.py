from part_1 import main

if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        lines = [int(it) for it in (f.read().splitlines()[0]).split(",")]

    print(f"result = {main(lines, 256)}")
