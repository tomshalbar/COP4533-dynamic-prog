from pathlib import Path


def parse_hvlcs_file(filepath) -> tuple | None:
    """
        Parses the HVLCS input file and returns the variables needed for the algorithm.

        Params:
            filepath --> filepath of input file to parse from the main directory of the project ('inputs/file.in')

        Returns:
            a tuple of values consisting of (alphabet map, A, B) if the input is valid, else it returns None (basic error handling)
    """
    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("Error: The provided file is empty.")
        return None

    # Parse K (number of characters in the alphabet)
    try:
        k: int = int(lines[0])
    except ValueError:
        print(f"Expected an integer for K on the first line, got: '{lines[0]}'")
        return None

    alphabet_values = {}

    # Parse the next K lines for characters and their values
    for i in range(1, k + 1):
        parts = lines[i].split()
        if len(parts) != 2:
            print(f"Expected '[character] [value]' on line {i + 1}, got: '{lines[i]}'")
            return None

        char, val = parts[0], int(parts[1])
        alphabet_values[char] = val

    # Parse String A and String B
    a: str = lines[k + 1]
    b: str = lines[k + 2]

    return alphabet_values, a, b


def output_results(input_file: str, res: tuple[int, str]) -> None:
    """
        Writes the resulting HVLCS and its subsequences to an output file (e.g. inputs/file.in -> outputs/file.out)

        Params:
            input_file -> Program's input file. (e.g. usg: if the input file is 'inputs/file.in', we convert it into 'outputs/file.out')
            res -> a tuple consisting of the HVLCS (int value), and its corresponding subsequence (str value)

        Returns:
            Nothing, just writes the data to a file
    """
    file_stem: str = str(Path(input_file).stem)
    output_file: str = "outputs/" + file_stem + ".out"
    with open(output_file, 'w') as out_file:
        out_file.write(f"{res[0]}\n")  # single integer on the first line
        out_file.write(f"{res[1]}\n")  # optimal subsequence on the next line

    print(f"Success! Results successfully written to '{output_file}'.")