from src.max_subsequence import calc_max_subsequence

# Shared alphabet for all nontrivial tests
VALS = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 10, 'y': 20, 'z': 50}

def test_identical_strings():
    # Length: 30. Exact match.
    A = "abcde" * 6
    B = "abcde" * 6
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 90  # (1+2+3+4+5) * 6
    assert resseq == "abcde" * 6

def test_disjoint_strings():
    # Length: 30. No common characters.
    A = "abcde" * 6
    B = "xyz" * 10
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 0
    assert resseq == ""

def test_pure_subsequence_embedded():
    # Lengths: 25 and 35. 'A' is entirely inside 'B'.
    A = "z" * 25
    B = "a" * 5 + "z" * 25 + "b" * 5
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 1250  # 25 * 50
    assert resseq == "z" * 25

def test_short_high_value_vs_long_low_value():
    # Lengths: 201 and 30. The algorithm must prefer the single 'z' over matching 'a's.
    A = "a" * 100 + "z" + "a" * 100
    B = "z" * 30
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 50
    assert resseq == "z"

def test_uniform_characters_bounded_by_shortest():
    # Lengths: 25 and 35.
    A = "y" * 25
    B = "y" * 35
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 500  # 25 * 20
    assert resseq == "y" * 25

def test_interleaved_high_value():
    # Lengths: 50. High value 'z' block vs low value 'a' block.
    A = "a" * 25 + "z" * 25
    B = "z" * 25 + "a" * 25
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 1250  # Matches the 'z' block
    assert resseq == "z" * 25

def test_repeated_blocks_flipped():
    # Lengths: 30.
    A = "x" * 15 + "y" * 15
    B = "y" * 15 + "x" * 15
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 300  # Matches the 'y' block (15 * 20 = 300) instead of 'x' (15 * 10 = 150)
    assert resseq == "y" * 15

def test_sparse_matching():
    # Lengths: 50 and 43.
    A = "abcde" * 10
    B = "z" * 10 + "e" + "z" * 10 + "e" + "z" * 10 + "e" + "z" * 10
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 15  # Only the three 'e's can match
    assert resseq == "eee"

def test_prefix_suffix_mismatch():
    # Lengths: 40.
    A = "z" * 10 + "a" * 30
    B = "a" * 30 + "z" * 10
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 500  # The 'z' block (10 * 50 = 500) beats the 'a' block (30 * 1 = 30)
    assert resseq == "z" * 10

def test_partial_middle_match():
    # Lengths: 30.
    A = "c" * 30
    B = "c" * 10 + "d" * 10 + "c" * 10
    resval, resseq = calc_max_subsequence(VALS, A, B)
    assert resval == 60  # Matches the 20 'c's in B. (20 * 3)
    assert resseq == "c" * 20
