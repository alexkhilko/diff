import pytest
from diff.diff import get_lcs, get_diff


@pytest.mark.parametrize(
    "s1, s2, result",
    [
        ("ABCDEF", "ABCDEF", "ABCDEF"),
        ("ABC", "XYZ", ""),
        ("AABCXY", "XY", "XY"),
        ("", "", ""),
        ("abcdrau", "axdlau", "adau"),
    ],
)
def test_get_lcs(s1, s2, result):
    assert get_lcs(s1, s2) == result


@pytest.mark.parametrize(
    "lines1, lines2, result",
    [
        (
            ["my name is alex", "i'm a developer", "i'm 31 yo"],
            ["my name is alexander", "i'm a developer", "i'm 30 yo"],
            (["my name is alex", "i'm 31 yo"], ["my name is alexander", "i'm 30 yo"]),
        ),
        (
            [],
            [
                "my name is alexander",
            ],
            ([], ["my name is alexander"]),
        ),
        (
            [],
            [],
            ([], []),
        ),
        (
            ["a", "b", "c"],
            ["b", "d"],
            (["a", "c"], ["d"]),
        ),
    ],
)
def test_get_diff(lines1, lines2, result):
    act_result = get_diff(lines1, lines2)
    assert act_result == result
