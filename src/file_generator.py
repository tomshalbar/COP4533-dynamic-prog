VALS = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 10, 'y': 20, 'z': 50}

# The same string pairs from the nontrivial testing suite
test_pairs = [
    ("abcde" * 6, "abcde" * 6),
    ("abcde" * 6, "xyz" * 10),
    ("z" * 25, "a" * 5 + "z" * 25 + "b" * 5),
    ("a" * 100 + "z" + "a" * 100, "z" * 30),
    ("y" * 25, "y" * 35),
    ("a" * 25 + "z" * 25, "z" * 25 + "a" * 25),
    ("x" * 15 + "y" * 15, "y" * 15 + "x" * 15),
    ("abcde" * 10, "z" * 10 + "e" + "z" * 10 + "e" + "z" * 10 + "e" + "z" * 10),
    ("z" * 10 + "a" * 30, "a" * 30 + "z" * 10),
    ("c" * 30, "c" * 10 + "d" * 10 + "c" * 10)
]


def generate_input_files() -> None:
    """
        Generates 10 nontrivial input files from the given `VALS` and `test_pairs` above.

        Params:
            None

        Returns:
            Nothing, the generated files will then be used to run the algorithm and graph each runtime
    """
    for idx, (str_A, str_B) in enumerate(test_pairs, start=1):
        filename = f"inputs/test_{idx:02d}.in"

        with open(filename, 'w') as f:
            f.write(f"{len(VALS)}\n")
            for char, val in VALS.items():
                f.write(f"{char} {val}\n")
            f.write(f"{str_A}\n")
            f.write(f"{str_B}\n")

    print("Successfully generated 10 nontrivial input files in the 'inputs/' directory.")


if __name__ == "__main__":
    generate_input_files()