import argparse
from io_ops import parse_hvlcs_file, output_results
from max_subsequence import calc_max_subsequence


def main():
    parser = argparse.ArgumentParser(description="Parses a given input file to determine its HVLCS.")
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input text file (e.g., inputs/file.in)"
    )

    args = parser.parse_args()

    try:
        # If we were able to successfully parse the file, calculate the HVLCS and its subsequence, and write them to an output file
        alphabet_values, a, b = parse_hvlcs_file(args.input_file)
        res: tuple[int, str] = calc_max_subsequence(alphabet_values, a, b)
        output_results(args.input_file, res)

    except FileNotFoundError:
        print(f"Error: The file '{args.input_file}' was not found.")
    except Exception as e:
        print(f"Error parsing file: {e}")


if __name__ == "__main__":
    main()