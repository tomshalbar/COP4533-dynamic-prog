import os
import time
import matplotlib.pyplot as plt
from max_subsequence import calc_max_subsequence
from io_ops import parse_hvlcs_file, output_results


def main():
    input_dir = 'inputs/'

    # Grab all generated input files and sort them alphabetically (test_01.in, test_02.in, etc.)
    files = sorted([f for f in os.listdir(input_dir) if f.startswith('test_') and f.endswith('.in')])

    if not files:
        print(f"No 'test_x.in' file found in '{input_dir}'.")
        return

    file_names = []
    runtimes = []

    print("Running benchmarks...")
    print("-" * 30)

    for filename in files:
        filepath = os.path.join(input_dir, filename)

        # Parse the file and get the algorithm's running time for it
        alphabet_values, a, b = parse_hvlcs_file(filepath)
        start_time = time.perf_counter()
        res = calc_max_subsequence(alphabet_values, a, b)
        output_results(filepath, res)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        # Clean up the filename for the graph label (e.g., 'test_01.in' -> '01')
        clean_name = filename.replace('test_', '').replace('.in', '')

        file_names.append(clean_name)
        runtimes.append(elapsed_time)

        print(f"{filename}: {elapsed_time:.6f} seconds")

    # --- Plotting the Results ---
    print("-" * 30)
    print("Generating graph...")

    plt.figure(figsize=(10, 6))

    # Create the chart
    plt.plot(file_names, runtimes, color='crimson', marker='o', linestyle='-', linewidth=2, markersize=8)

    # Add labels and a title
    plt.xlabel('Test File Number', fontsize=12)
    plt.ylabel('Runtime (seconds)', fontsize=12)
    plt.title('Empirical Runtime Comparison of HVLCS Algorithm', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Save the graph as an image file
    output_image = 'runtime_graph.png'
    plt.savefig(output_image)
    print(f"Graph successfully saved as '{output_image}'.")

    # Display it
    plt.show()


if __name__ == "__main__":
    main()