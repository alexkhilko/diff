import argparse


def get_lcs(s1: str, s2: str) -> str:
    """
    Initial implementation that returns longest common subsequence
    between 2 strings.
    Leave here as a simple demonstrations of an algorithm that is used.
    """
    ROWS, COLUMNS = len(s2), len(s1)
    if ROWS == 0 or COLUMNS == 0:
        return ""
    dp = [[""] * (COLUMNS + 1) for _ in range(ROWS + 1)]
    for row in range(1, ROWS + 1):
        for col in range(1, COLUMNS + 1):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + s1[col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[ROWS][COLUMNS]


def _get_lcs_indexes(lines1: list[str], lines2: list[str]) -> list[tuple[int, int]]:
    ROWS, COLUMNS = len(lines2), len(lines1)
    if ROWS == 0 or COLUMNS == 0:
        return []
    # lcs[i, j] represents list of common subsequence line indexes between lines1[:i] and lines2[:j]
    lcs: list[list[list[tuple[int, int]]]] = [[[] for _ in range(COLUMNS + 1)] for _ in range(ROWS + 1)]
    for row in range(1, ROWS + 1):
        for col in range(1, COLUMNS + 1):
            if lines1[col - 1] == lines2[row - 1]:
                lcs[row][col] = lcs[row - 1][col - 1] + [(col - 1, row - 1)]
            else:
                lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])
    return lcs[ROWS][COLUMNS]


def get_diff(lines1: list[str], lines2: list[str]) -> tuple[list[str], list[str]]:
    indexes = _get_lcs_indexes(lines1, lines2)
    l1_common_indexes = {i[0] for i in indexes}
    l2_common_indexes = {i[1] for i in indexes}
    l1_diff = [s for idx, s in enumerate(lines1) if idx not in l1_common_indexes]
    l2_diff = [s for idx, s in enumerate(lines2) if idx not in l2_common_indexes]
    return (l1_diff, l2_diff)


def print_diff(lines1: list[str], lines2: list[str]) -> None:
    l1_diff, l2_diff = get_diff(lines1, lines2)
    for s in l1_diff:
        print(f"< {s}")
    print("---")
    for s in l2_diff:
        print(f"> {s}")


def read_file(filepath: str) -> list[str]:
    lines = []
    with open(filepath, "r", encoding="latin-1") as file_:
        for line in file_:
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='diff', description='Calculate difference between 2 files.',)
    parser.add_argument('file1')
    parser.add_argument('file2')
    args = parser.parse_args()
    print_diff(read_file(args.file1), read_file(args.file2))