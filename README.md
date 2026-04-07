# COP4533-dynamic-prog

**Team Members:**
1. Thomas Tavera, ID 38874789
2. Tom Shal-bar, ID 36397041

## Setup and Installation
```bash
git clone https://github.com/tomshalbar/COP4533-dynamic-prog.git
cd COP4533-dynamic-prog
python3 -m venv .venv
pip install -r requirements.txt
```

## Running the Algorithm
The program runs on a specific input file provided by the user.

The program expects the input file to be found in the `inputs/` directory.

_**python src/main.py <input_file>**_

Example usage:

```python src/main.py inputs/example_short.in```

The output would then be written to: `outputs/example_short.out`

## Running the Tests
The repository also includes a comprehensive unit testing suite using `pytest` that can be run with:

```python -m pytest```

# Question 1: Empirical Comparison
To generate the 10 nontrivial input files, run: 

```python src/file_generator.py```.

This will place 10 files into the `inputs/` directory in the form `test_01.in, ..., test_10.in`.

To then benchmark the runs and plot their time do the following command:

```python src/benchmark_and_plot.py```

# Questions 2 and 3:

[View Recurrence Equation and Big-Oh Work](./COP4533_Dynamic_Programming.pdf)

Just click the link to see our work in a PDF. 

