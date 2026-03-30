from src.max_subsequence import calc_max_subsequence


def test_short():

    test_dict = {
        "q": 2,
        "w": 4,
        "e": 5,
        "r": 11,
        "t": 7,
        "y": 3,
        "u": 16,
        "i": 8,
        "o": 2,
        "p": 13,
    }
    test_str1 = "qwtqweruioupqwewqeqwpe"
    test_str2a = "qwq"  # qwq
    test_str2b = "qwtq"  # qwtq
    test_str2c = "qwtqt"  # qwtq
    test_str2d = "pwweqq"  # pwweq
    test_str2e = "pu"  # u

    resaval, resaseq = calc_max_subsequence(test_dict, test_str1, test_str2a)
    resbval, resbseq = calc_max_subsequence(test_dict, test_str1, test_str2b)
    rescval, rescseq = calc_max_subsequence(test_dict, test_str1, test_str2c)
    resdval, resdseq = calc_max_subsequence(test_dict, test_str1, test_str2d)
    reseval, reseseq = calc_max_subsequence(test_dict, test_str1, test_str2e)
    assert resaval == 8
    assert resaseq == "qwq"
    assert resbval == 15
    assert resbseq == "qwtq"
    assert rescval == 15
    assert rescseq == "qwtq"
    assert resdval == 28
    assert resdseq == "pwweq"
    assert reseval == 16
    assert reseseq == "u"


def test_negative_alphabet():
    test_dict = {"a": -1, "b": -3, "c": -6}
    test_str1a = "aabc"
    test_str2b = "abc"

    resval, resseq = calc_max_subsequence(test_dict, test_str1a, test_str2b)  # ''
    assert resval == 0
    assert resseq == ""


def test_negative_and_some_positives():
    test_dict = {"a": -1, "b": -3, "c": -6, "d": 1, "e": 3}
    test_str1a = "aeabecabadb"
    test_str2b = "aebdeaac"

    resval, resseq = calc_max_subsequence(test_dict, test_str1a, test_str2b)  # ee
    assert resval == 6
    assert resseq == "ee"
