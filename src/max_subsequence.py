import numpy as np


def calc_max_subsequence(alphabet: dict, str1: str, str2: str) -> tuple[int, str]:

    OPT = np.full((len(str1) + 1, len(str2) + 1), -1)

    OPT[0, :] = 0
    OPT[:, 0] = 0
    for i in range(1, len(OPT)):
        for j in range(1, len(OPT[0])):
            if str2[j - 1] not in alphabet:
                raise KeyError(f"'{str2[j - 1]}' is not defined in the given alphabet")
            if str1[i - 1] == str2[j - 1]:
                include = alphabet[str1[i - 1]] + OPT[i - 1, j - 1]
                exclude = max(OPT[i - 1, j], OPT[i, j - 1])
                OPT[i, j] = max(include, exclude)

            else:
                OPT[i, j] = max(OPT[i - 1, j], OPT[i, j - 1])
    subseq = []
    last_row = OPT[-1]
    for i in range(len(str2), 0, -1):
        if last_row[i] > last_row[i - 1]:
            subseq.append(str2[i - 1])

    return OPT[len(str1), len(str2)], "".join(subseq[::-1])
